import os
import struct

PC_EXE = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "memories-pc.exe")
ROM_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")

SECTOR_SIZE = 2352
HEADER_SIZE = 24
SLUS_LBA = 25

def patch_pc_executable():
    print("--- 1. Neutralizando no Executavel de PC (memories-pc.exe) ---")
    if not os.path.exists(PC_EXE):
        print(f"Erro: {PC_EXE} nao encontrado!")
        return

    # Duel_CalcGuardianStarBonus (VA: 0x01BD2816, File Offset: 0x00240216)
    # Duel_CalcGuardianStarMatchup (VA: 0x01BD2B76, File Offset: 0x00240576)
    targets = [
        (0x00240216, "Duel_CalcGuardianStarBonus"),
        (0x00240576, "Duel_CalcGuardianStarMatchup"),
    ]
    
    # x86 patch: xor eax, eax (31 c0); ret (c3); nop (90); nop (90)
    patch = b"\x31\xc0\xc3\x90\x90"

    with open(PC_EXE, "r+b") as f:
        for offset, name in targets:
            f.seek(offset)
            orig = f.read(len(patch))
            print(f"[{name}] Offset 0x{offset:08X} - Original: {orig.hex()} -> Novo: {patch.hex()}")
            f.seek(offset)
            f.write(patch)

    print(">>> Executavel de PC neutralizado: Bonus e Matchup de Estrela Guardiana retornam SEMPRE 0! <<<\n")

def patch_ps1_rom():
    print("--- 2. Neutralizando na ROM do PS1 (.bin / SLUS_014.11) ---")
    if not os.path.exists(ROM_BIN):
        print(f"Erro: {ROM_BIN} nao encontrado!")
        return

    # In SLUS_014.11:
    # Duel_CalcGuardianStarMatchup starts at SLUS offset 0x1D380 (BIN offset 0x2FE28)
    # Duel_CalcGuardianStarBonus starts at SLUS offset 0x1D3F4 (BIN offset 0x2FE9C)
    #
    # MIPS stub:
    #   0x03E00008  jr ra
    #   0x00001021  move v0, zero (addu v0, zero, zero)
    #
    mips_stub = struct.pack("<II", 0x03E00008, 0x00001021)

    targets = [
        (0x2FE28, "Duel_CalcGuardianStarMatchup (SLUS 0x1D380)"),
        (0x2FE9C, "Duel_CalcGuardianStarBonus   (SLUS 0x1D3F4)"),
    ]

    with open(ROM_BIN, "r+b") as f:
        for bin_offset, name in targets:
            f.seek(bin_offset)
            orig = f.read(8)
            orig_w0, orig_w1 = struct.unpack("<II", orig)
            f.seek(bin_offset)
            f.write(mips_stub)
            new_w0, new_w1 = struct.unpack("<II", mips_stub)
            print(f"[{name}] BIN Offset 0x{bin_offset:08X}:")
            print(f"   Original: 0x{orig_w0:08X} 0x{orig_w1:08X}")
            print(f"   Modificado: 0x{new_w0:08X} 0x{new_w1:08X} (jr ra; move v0, zero)")

    print(">>> ROM do PS1 (.bin) neutralizada: Bonus de Estrelas Guardianas agora e SEMPRE ZERO! <<<")

if __name__ == "__main__":
    patch_pc_executable()
    patch_ps1_rom()
