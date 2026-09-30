import os

MOD_DIR = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "mods", "overhaul-mod")
TEXT_FILE = os.path.join(MOD_DIR, "text.txt")

# Hex ID is 0xD100 + Card ID
def make_hex_id(cid):
    return f"D{0x100 + cid:03X}"

CARDS_RECIPES = [
    (1, "Blue-eyes White Dragon", [
        "FUSOES OLHOS AZUIS:",
        "+ Olhos Azuis x3 = D. Supremo",
        "+ Maquina = Dragao Cibernetico",
        "+ Equipa c/ Tesouro do Dragao"
    ]),
    (4, "Baby Dragon", [
        "FUSOES DRAGAO BEBE:",
        "+ Mago do Tempo = D. Milenar",
        "+ D. Zumbi = Maldicao Dragao",
        "+ Agua = Serpente Marinha"
    ]),
    (16, "Time Wizard", [
        "FUSOES MAGO DO TEMPO:",
        "+ Dragao Bebe = Dragao Milenar",
        "+ Guerreiro = Espadachim Chama",
        "+ Doma = Mago do Caos"
    ]),
    (22, "Summoned Skull", [
        "FUSOES CAVEIRA INVOCADA:",
        "+ D. Olhos Vermelhos = B. Skull Dragon",
        "+ Guerreiro = Cavaleiro Zumbi",
        "+ Magia = Demonio do Abismo"
    ]),
    (26, "Battle Ox", [
        "FUSOES FERA / GUERREIRO:",
        "+ Dragao = Dragao Boi Furioso",
        "+ Zumbi = Boi Espectral Zumbi",
        "+ Maquina = Ciborgue Minotauro"
    ]),
    (31, "Koumori Dragon", [
        "FUSOES DRAGAO TREVAS:",
        "+ Trovao = Dragao do Trovao",
        "+ Trovao (Forte) = D. 2 Cabecas",
        "+ Zumbi = Dragao Zumbi"
    ]),
    (32, "Two-headed King Rex", [
        "FUSOES DINOSSAURO:",
        "+ Dragao = Dragao Braquiossauro",
        "+ Maquina = Ciborgue T-Rex",
        "+ Equipa c/ Presas de Fera"
    ]),
    (35, "Dark Magician", [
        "FUSOES MAGO NEGRO:",
        "+ Dragao = Cavaleiro Magico",
        "+ Trevas = Fantasma Magico",
        "+ Fogo = Mago da Chama Solar"
    ]),
    (50, "Basic Insect", [
        "FUSOES INSETO:",
        "+ Maquina = Besouro Canhao",
        "+ Kuwagata = Kwagar Hercules",
        "+ Planta = Louva-a-Deus Floresta"
    ]),
    (52, "Hercules Beetle", [
        "FUSOES BESOURO HERCULES:",
        "+ Maquina = Hercules Mecanico",
        "+ Fera = Quimera da Floresta",
        "+ Equipa c/ Canhao Laser"
    ]),
    (62, "Harpie Lady", [
        "FUSOES HARPIA:",
        "+ Dragao = Dragao Mascote Harpia",
        "+ Besta Alada = Aguia Suprema",
        "+ Equipa c/ Escudo Cibernetico"
    ]),
    (63, "Harpie Lady Sisters", [
        "FUSOES IRMAS DE HARPIA:",
        "+ Dragao = Dragao Mascote Harpia",
        "+ Montanha = Bônus de Campo",
        "+ Equipa c/ Vento Favoravel"
    ]),
    (69, "Water Omotics", [
        "FUSOES AGUA / MARES:",
        "+ Dragao = Serpente dos Picos",
        "+ Trovao = Tubarao Eletrico",
        "+ Planta = Alga Gigante"
    ]),
    (79, "Megazowler", [
        "FUSOES DINOSSAURO DEFENSIVO:",
        "+ Dragao = Dragao Rastejante",
        "+ Zumbi = Fera Fossil Zumbi",
        "+ Equipa c/ Ermos (Wasteland)"
    ]),
    (81, "Crawling Dragon 2", [
        "FUSOES DRAGAO RASTEJANTE:",
        "+ Trovao = Dragao 2 Cabecas",
        "+ Fogo = Dragao de Fogo Alado",
        "+ Zumbi = Dragao Zumbi"
    ]),
    (82, "Red-eyes B. Dragon", [
        "FUSOES OLHOS VERMELHOS:",
        "+ D. Meteoro = D. Meteoro Negro",
        "+ Caveira Invocada = B. Skull",
        "+ Maquina = Dragao Metalico"
    ]),
    (84, "Reaper of the Cards", [
        "FUSOES CEIFADOR DE CARTAS:",
        "+ Guerreiro = Cavaleiro Cadáver",
        "+ Mago = Mago do Oculto",
        "+ Trevas = Lorde do Abismo"
    ]),
    (93, "Zanki", [
        "FUSOES GUERREIRO ZANKI:",
        "+ Zumbi = Zumbi Blindado",
        "+ Maquina = Soldado Cibernetico",
        "+ Fogo = Espadachim da Chama"
    ]),
    (114, "White Magical Hat", [
        "FUSOES MAGO DA LUZ:",
        "+ Trevas = Mago Fantasma",
        "+ Fogo = Guerreiro da Chama",
        "+ Fada = Rainha Mágica da Luz"
    ]),
    (297, "Cyber Soldier of Darkworld", [
        "FUSOES SOLDADO CIBERNETICO:",
        "+ Guerreiro = Giga-Tech Wolf",
        "+ Dragao = Dragao Metalico",
        "+ Equipa c/ Fabrica de Conversao"
    ]),
    (388, "Pendulum Machine", [
        "FUSOES MAQUINA PENDULO:",
        "+ Zumbi = Maquina Cadáverica",
        "+ Guerreiro = Rei das Maquinas",
        "+ Equipa c/ 7 Completo"
    ]),
    (407, "Machine King", [
        "FUSOES REI DAS MAQUINAS:",
        "+ Guerreiro = Ciborgue Mestre",
        "+ Dragao = Dragao de Aco Supremo",
        "+ Equipa c/ Metalmorfo"
    ]),
    (412, "Giga-tech Wolf", [
        "FUSOES LOBO CIBERNETICO:",
        "+ Guerreiro = Cavaleiro Mecanico",
        "+ Dragao = Dragao Cibernetico",
        "+ Zumbi = Lobo Metalico Fantasma"
    ]),
    (466, "Skull Red Bird", [
        "FUSOES BESTA ALADA:",
        "+ Harpia = Aguia Suprema de Voo",
        "+ Dragao = Dragao Alado Vermelho",
        "+ Equipa c/ Vento Favoravel"
    ]),
    (480, "Kuwagata Alpha", [
        "FUSOES INSETO KUWAGATA:",
        "+ Besouro Hercules = Kwagar Hercules",
        "+ Maquina = Besouro Canhao",
        "+ Equipa c/ Floresta (Forest)"
    ])
]

def generate_text_listing():
    lines = ["@bank descriptions\n"]
    for cid, name, desc_lines in CARDS_RECIPES:
        hid = make_hex_id(cid)
        lines.append(f"[{hid}]  # #{cid:03d} {name}")
        for dl in desc_lines:
            lines.append(dl)
        lines.append("{end}\n")
    
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print(f"Gerado com sucesso: {TEXT_FILE} com {len(CARDS_RECIPES)} cartas essenciais!")

if __name__ == "__main__":
    generate_text_listing()
