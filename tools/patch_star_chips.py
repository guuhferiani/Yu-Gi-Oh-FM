import os
import struct
import shutil

ORIGINAL_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
ORIGINAL_CUE = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).cue")

MOD_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")
MOD_CUE = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).cue")

SECTOR_SIZE = 2352
HEADER_SIZE = 24
WA_MRG_LBA = 10102
TABLE_OFFSET_IN_WA = 0xFB9800  # Offset exato da tabela de 722 cartas

# Lista de cartas famosas para rebalancear no primeiro teste:
# (ID da Carta 1-based, Nome, Novo Custo de Star Chips)
CARDS_TO_REBALANCE = [
    (1, "Dragão Branco de Olhos Azuis (Blue-Eyes)", 200),
    (4, "Dragão Bebê (Baby Dragon)", 30),
    (35, "Mago Negro (Dark Magician)", 150),
    (82, "Dragão Negro de Olhos Vermelhos (Red-Eyes)", 150),
    (336, "Raigeki", 100),
    (657, "Megamorfo (Megamorph)", 100),
]

def calculate_bin_offset_for_card(card_id):
    """
    Calcula o offset físico absoluto dentro do arquivo .BIN para o registro da carta.
    card_id é 1-based (1 = Blue-Eyes).
    Cada registro tem 8 bytes: [4 bytes custo uint32][4 bytes senha].
    """
    card_byte_in_wa = TABLE_OFFSET_IN_WA + (card_id * 8)
    sector_in_wa = card_byte_in_wa // 2048
    byte_in_sector = card_byte_in_wa % 2048

    abs_lba = WA_MRG_LBA + sector_in_wa
    abs_bin_offset = (abs_lba * SECTOR_SIZE) + HEADER_SIZE + byte_in_sector
    return abs_bin_offset

def apply_patch():
    print(f"--- Iniciando Criação da ROM Modificada ---")
    
    # 1. Criar cópia de trabalho da ROM se não existir
    if not os.path.exists(MOD_BIN):
        print(f"Criando cópia limpa para modificação: {MOD_BIN}...")
        shutil.copyfile(ORIGINAL_BIN, MOD_BIN)
        print("Cópia concluída!")
    else:
        print(f"Arquivo de trabalho encontrado: {MOD_BIN}")

    # 2. Criar arquivo .cue correspondente
    cue_content = f'FILE "{os.path.basename(MOD_BIN)}" BINARY\n  TRACK 01 MODE2/2352\n    INDEX 01 00:00:00\n'
    with open(MOD_CUE, "w", encoding="utf-8") as cue_f:
        cue_f.write(cue_content)
    print(f"Arquivo CUE gerado: {MOD_CUE}")

    # 3. Aplicar as alterações no arquivo MOD_BIN
    with open(MOD_BIN, "r+b") as f:
        for card_id, name, new_cost in CARDS_TO_REBALANCE:
            offset = calculate_bin_offset_for_card(card_id)
            
            # Ler dados atuais
            f.seek(offset)
            curr_data = f.read(8)
            curr_cost = struct.unpack("<I", curr_data[:4])[0]
            password_hex = curr_data[4:].hex()
            # Inverter bytes para formato de senha legível (little-endian BCD)
            password = "".join(reversed([password_hex[i:i+2] for i in range(0, len(password_hex), 2)]))

            # Gravar novo custo (uint32)
            f.seek(offset)
            f.write(struct.pack("<I", new_cost))

            print(f"Card #{card_id:03d} - {name}:")
            print(f"   Offset no BIN: 0x{offset:X}")
            print(f"   Senha: {password}")
            print(f"   Custo Anterior: {curr_cost:,} -> NOVO CUSTO: {new_cost} Star Chips\n")

    print(">>> Patch de custos aplicado com SUCESSO total! <<<")

if __name__ == "__main__":
    apply_patch()
