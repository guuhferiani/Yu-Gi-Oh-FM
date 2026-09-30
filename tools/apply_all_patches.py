import os
import shutil
import subprocess
import sys

ROM_CLEAN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
ROM_MOD = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")

def main():
    print("=" * 65)
    print("   Yu-Gi-Oh! Forbidden Memories — Overhaul Mod Builder")
    print("=" * 65)

    if not os.path.exists(ROM_CLEAN) and not os.path.exists(ROM_MOD):
        print(f"\n[ERRO] Nenhuma ROM encontrada em: {ROM_CLEAN}")
        print("Coloque a sua imagem limpa (.bin) na pasta 'rom/' para prosseguir.")
        sys.exit(1)

    if not os.path.exists(ROM_MOD):
        print(f"\n[1/5] Criando cópia de trabalho: {ROM_MOD}...")
        shutil.copyfile(ROM_CLEAN, ROM_MOD)
    else:
        print(f"\n[1/5] ROM de trabalho detectada: {ROM_MOD}")

    print("\n[2/5] Aplicando custos justos de Star Chips...")
    import patch_star_chips
    patch_star_chips.main()

    print("\n[3/5] Injetando 39 novas fusões balanceadas na ROM...")
    import inject_fusions
    inject_fusions.main()

    print("\n[4/5] Neutralizando bônus de Estrelas Guardiãs (+-500)...")
    import patch_guardian_stars
    patch_guardian_stars.patch_pc_executable()
    patch_guardian_stars.patch_ps1_rom()

    print("\n[5/5] Gerando descrições das cartas com fórmulas de fusão...")
    import generate_card_descriptions
    generate_card_descriptions.generate_text_listing()

    print("\n" + "=" * 65)
    print("   >>> SUCESSO! O MOD FOI APLICADO COM 100% DE SUCESSO! <<<")
    print("=" * 65)
    print("\nPara jogar no PC: execute JOGAR_PC.bat")
    print("Para jogar no Android: envie rom/Yu-Gi-Oh! Forbidden Memories (Mod).bin/.cue\n")

if __name__ == "__main__":
    main()
