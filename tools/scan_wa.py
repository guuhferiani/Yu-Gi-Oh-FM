import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def scan_wa_mrg():
    be_cost = struct.pack("<I", 999999)
    print(f"Buscando padrão 999.999 ({be_cost.hex()}) em WA_MRG.MRG...")
    
    # WA_MRG starts at LBA 10102, size 37748736 (18432 sectors)
    wa_lba = 10102
    wa_size = 37748736
    sectors = (wa_size + 2047) // 2048

    matches = []
    with open(ROM_PATH, "rb") as f:
        # Read in chunks of 512 sectors (1MB data)
        chunk_sectors = 512
        for start_s in range(0, sectors, chunk_sectors):
            count = min(chunk_sectors, sectors - start_s)
            buf = bytearray()
            for s in range(count):
                f.seek((wa_lba + start_s + s) * SECTOR_SIZE + HEADER_SIZE)
                buf.extend(f.read(2048))
            
            # Search in this 1MB buffer
            pos = 0
            while True:
                pos = buf.find(be_cost, pos)
                if pos == -1:
                    break
                abs_offset = start_s * 2048 + pos
                matches.append(abs_offset)
                pos += 1
            if len(matches) > 50:
                break

    print(f"Total de ocorrências em WA_MRG: {len(matches)}")
    for m in matches[:10]:
        print(f"Offset em WA_MRG: 0x{m:X} ({m})")

if __name__ == "__main__":
    scan_wa_mrg()
