import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")

def inspect_bin(rom_path):
    if not os.path.exists(rom_path):
        print(f"Arquivo não encontrado: {rom_path}")
        return

    size = os.path.getsize(rom_path)
    print(f"Tamanho do arquivo BIN: {size} bytes ({size / (1024*1024):.2f} MB)")

    with open(rom_path, "rb") as f:
        # Check first sector sync pattern
        first_16 = f.read(16)
        # Standard CD-ROM sync pattern: 00 FF FF FF FF FF FF FF FF FF FF 00
        sync_pattern = b"\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00"
        is_raw = first_16.startswith(sync_pattern)
        sector_size = 2352 if is_raw else 2048
        data_offset = 24 if is_raw else 0 # Mode 2 Form 1 header usually 24 bytes (12 sync + 3 header + 1 subheader + 8 subheader) or Mode 1 (16 bytes)

        print(f"Tipo de setor detectado: {'RAW 2352 bytes (Mode 2 / Mode 1)' if is_raw else 'ISO 2048 bytes'}")
        
        # Check Mode: byte 15 in RAW is mode
        if is_raw:
            f.seek(15)
            mode = f.read(1)[0]
            print(f"Modo CD-ROM: Mode {mode}")
            # Mode 1 has 16 bytes header; Mode 2 Form 1 has 24 bytes header
            # Usually PS1 uses Mode 2 (XA), data starts at offset 24
            data_offset = 24 if mode == 2 else 16

        # Seek to Primary Volume Descriptor (LBA 16)
        pvd_lba = 16
        f.seek(pvd_lba * sector_size + data_offset)
        pvd = f.read(2048)

        if len(pvd) >= 6 and pvd[1:6] == b"CD001":
            print("Identificador ISO9660 PVD confirmado: 'CD001'")
            sys_id = pvd[8:40].decode("ascii", errors="replace").strip()
            vol_id = pvd[40:72].decode("ascii", errors="replace").strip()
            print(f"System ID: {sys_id}")
            print(f"Volume ID: {vol_id}")

            # Root directory record is at offset 156 in PVD (34 bytes)
            root_rec = pvd[156:190]
            root_lba = struct.unpack("<I", root_rec[2:6])[0]
            root_size = struct.unpack("<I", root_rec[10:14])[0]
            print(f"Root Directory LBA: {root_lba}, Tamanho: {root_size} bytes")

            # Parse root directory
            print("\n--- Arquivos na raiz do disco ISO9660 ---")
            files = []
            f.seek(root_lba * sector_size + data_offset)
            dir_data = f.read(root_size)
            pos = 0
            while pos < len(dir_data):
                rec_len = dir_data[pos]
                if rec_len == 0:
                    # Sector boundary or padding
                    # Align to next 2048 block
                    next_block = ((pos // 2048) + 1) * 2048
                    if next_block <= pos or next_block >= len(dir_data):
                        break
                    pos = next_block
                    continue

                record = dir_data[pos:pos+rec_len]
                file_lba = struct.unpack("<I", record[2:6])[0]
                file_size = struct.unpack("<I", record[10:14])[0]
                flags = record[25]
                name_len = record[32]
                name = record[33:33+name_len].decode("ascii", errors="replace").split(";")[0]

                is_dir = (flags & 2) != 0
                if name not in ("\x00", "\x01", ""):
                    files.append({
                        "name": name,
                        "is_dir": is_dir,
                        "lba": file_lba,
                        "size": file_size,
                        "offset_bin": file_lba * sector_size
                    })
                    print(f"{'[DIR] ' if is_dir else '[FILE]'} {name:<18} | LBA: {file_lba:<6} | Tamanho: {file_size:<10} bytes | Offset: 0x{file_lba * sector_size:X}")

                pos += rec_len

            # Inspecionar subdiretórios encontrados (ex: DATA)
            for f_info in files:
                if f_info["is_dir"]:
                    print(f"\n--- Arquivos dentro de {f_info['name']} (LBA {f_info['lba']}) ---")
                    f.seek(f_info["lba"] * sector_size + data_offset)
                    sub_data = f.read(f_info["size"])
                    sub_pos = 0
                    while sub_pos < len(sub_data):
                        r_len = sub_data[sub_pos]
                        if r_len == 0:
                            next_b = ((sub_pos // 2048) + 1) * 2048
                            if next_b <= sub_pos or next_b >= len(sub_data):
                                break
                            sub_pos = next_b
                            continue
                        sub_rec = sub_data[sub_pos:sub_pos+r_len]
                        s_lba = struct.unpack("<I", sub_rec[2:6])[0]
                        s_size = struct.unpack("<I", sub_rec[10:14])[0]
                        s_flags = sub_rec[25]
                        s_nlen = sub_rec[32]
                        s_name = sub_rec[33:33+s_nlen].decode("ascii", errors="replace").split(";")[0]
                        s_isdir = (s_flags & 2) != 0
                        if s_name not in ("\x00", "\x01", ""):
                            print(f"{'[DIR] ' if s_isdir else '[FILE]'} {s_name:<20} | LBA: {s_lba:<6} | Tamanho: {s_size:<10} bytes | Offset: 0x{s_lba * sector_size:X}")
                        sub_pos += r_len

            return files
        else:
            print("Aviso: PVD CD001 não encontrado no setor 16.")

if __name__ == "__main__":
    inspect_bin(ROM_PATH)
