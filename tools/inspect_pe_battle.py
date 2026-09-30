import os
import struct

EXE_PATH = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "memories-pc.exe")
SYMBOLS_PATH = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "symbols", "30cd519a.txt")

def inspect_pe():
    with open(EXE_PATH, "rb") as f:
        data = f.read()

    # Read PE header to convert RVA to file offset
    e_lfanew = struct.unpack("<I", data[0x3C:0x40])[0]
    pe_header = data[e_lfanew:]
    num_sections = struct.unpack("<H", pe_header[6:8])[0]
    opt_header_size = struct.unpack("<H", pe_header[20:22])[0]
    image_base = struct.unpack("<I", pe_header[52:56])[0]
    print(f"Image Base: 0x{image_base:08X}, Sections: {num_sections}")

    section_table_offset = e_lfanew + 24 + opt_header_size
    sections = []
    for i in range(num_sections):
        sec = data[section_table_offset + i*40 : section_table_offset + (i+1)*40]
        name = sec[:8].decode("ascii", errors="ignore").strip("\x00")
        vsize = struct.unpack("<I", sec[8:12])[0]
        vaddr = struct.unpack("<I", sec[12:16])[0]
        raw_size = struct.unpack("<I", sec[16:20])[0]
        raw_offset = struct.unpack("<I", sec[20:24])[0]
        sections.append((name, vaddr, vsize, raw_offset, raw_size))
        print(f"Section {name:<8}: VAddr 0x{vaddr:08X} - 0x{vaddr+vsize:08X} | File Offset 0x{raw_offset:08X}")

    def rva_to_offset(rva):
        for name, vaddr, vsize, raw_offset, raw_size in sections:
            if vaddr <= rva < vaddr + vsize:
                return raw_offset + (rva - vaddr)
        return None

    # Find Duel_CalcGuardianStarBonus
    target_syms = ["Duel_CalcGuardianStarBonus", "Duel_CalcBattleAttack", "Duel_CalcBattleDefense", "Duel_CalcGuardianStarMatchup"]
    with open(SYMBOLS_PATH, "r") as sf:
        for line in sf:
            parts = line.strip().split()
            if len(parts) >= 3 and parts[2] in target_syms:
                vaddr = int(parts[0], 16)
                size = int(parts[1], 16)
                name = parts[2]
                rva = vaddr - image_base
                foff = rva_to_offset(rva)
                print(f"\nFunção: {name} (VA: 0x{vaddr:08X}, RVA: 0x{rva:08X}, File Offset: 0x{foff:08X}, Size: {size})")
                code_bytes = data[foff:foff+size]
                print(f"Bytes: {code_bytes.hex()}")

if __name__ == "__main__":
    inspect_pe()
