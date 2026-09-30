import os
import json

MOD_DIR = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "mods", "overhaul-mod")
MANIFEST_PATH = os.path.join(MOD_DIR, "mod.json")

# Lista de fusões expandidas organizadas por famílias
EXPANDED_FUSIONS = [
    # --- 1. Fusões Icônicas do Anime ---
    {"with": ["Baby Dragon", "Time Wizard"], "result": "Thousand Dragon"},
    {"with": ["Baby Dragon", "Dragon Zombie"], "result": "Curse of Dragon"},
    {"with": ["Time Wizard", "Kojikocy"], "result": "Flame Swordsman"},
    {"with": ["Time Wizard", "Swordsman of Landstar"], "result": "Flame Swordsman"},
    {"with": ["Time Wizard", "Celtic Guardian"], "result": "Flame Swordsman"},
    {"with": ["Time Wizard", "Armored Lizard"], "result": "Curse of Dragon"},
    {"with": ["Red-eyes B. Dragon", "Meteor Dragon"], "result": "Meteor B. Dragon"},
    {"with": ["Red-eyes B. Dragon", "Summoned Skull"], "result": "B. Skull Dragon"},
    {"with": ["Gaia the Fierce Knight", "Curse of Dragon"], "result": "Gaia the Dragon Champion"},
    {"with": ["Celtic Guardian", "Silver Fang"], "result": "Wolf Axwielder"},

    # --- 2. Família Guerreiros & Zumbis ---
    {"with": ["Swordsman of Landstar", "Skull Servant"], "result": "Zombie Warrior"},
    {"with": ["Kojikocy", "Shadow Specter"], "result": "Zombie Warrior"},
    {"with": ["Armored Lizard", "Clown Zombie"], "result": "Armored Zombie"},
    {"with": ["Celtic Guardian", "Dragon Zombie"], "result": "Armored Zombie"},
    {"with": ["Battle Ox", "Dragon Zombie"], "result": "Skull Knight"},
    {"with": ["Garoozis", "Dragon Zombie"], "result": "Skull Knight"},
    {"with": ["Axe Raider", "Clown Zombie"], "result": "Skull Knight"},

    # --- 3. Família Guerreiros & Máquinas (Ciborgues) ---
    {"with": ["Swordsman of Landstar", "Mechanical Spider"], "result": "Cyber Soldier"},
    {"with": ["Kojikocy", "Bat"], "result": "Cyber Soldier"},
    {"with": ["Celtic Guardian", "Blocker"], "result": "Giga-tech Wolf"},
    {"with": ["Battle Ox", "Blast Juggler"], "result": "Cyber Saurus"},
    {"with": ["Garoozis", "Cyber-Stein"], "result": "Metal Dragon"},

    # --- 4. Família Magos & Ocultismo (Fogo / Trevas) ---
    {"with": ["Phantom Dewan", "Fire Reaper"], "result": "Flame Swordsman"},
    {"with": ["Genin", "Hinotama Soul"], "result": "Flame Swordsman"},
    {"with": ["Doma The Angel of Silence", "Flame Manipulator"], "result": "Flame Swordsman"},
    {"with": ["Genin", "Shadow Specter"], "result": "Magical Ghost"},
    {"with": ["Phantom Dewan", "Skull Servant"], "result": "Magical Ghost"},
    {"with": ["Doma The Angel of Silence", "Time Wizard"], "result": "Dark Magician"},
    {"with": ["Phantom Dewan", "Time Wizard"], "result": "Dark Magician"},

    # --- 5. Família Mares & Oceanos (Água + Dragão / Trovão) ---
    {"with": ["Water Omotics", "Baby Dragon"], "result": "Kairyu-Shin"},
    {"with": ["Enchanting Mermaid", "Koumori Dragon"], "result": "Spike Seadra"},
    {"with": ["Water Omotics", "Crawling Dragon"], "result": "Aqua Dragon"},
    {"with": ["Arlownay", "Water Omotics"], "result": "Enchanting Mermaid"},

    # --- 6. Família Natureza & Insetos (Inseto + Máquina / Fera + Planta) ---
    {"with": ["Basic Insect", "Mechanical Spider"], "result": "Hercules Beetle"},
    {"with": ["Gokibore", "Blocker"], "result": "Hercules Beetle"},
    {"with": ["Alinsection", "Blast Juggler"], "result": "Kwagar Hercules"},
    {"with": ["Dark Plant", "Silver Fang"], "result": "Nekogal 2"},
    {"with": ["Arlownay", "Wolf"], "result": "Queen of Autumn Leaves"},
    {"with": ["Dark Plant", "Mystical Elf"], "result": "Queen of Autumn Leaves"}
]

def inject_fusions():
    if not os.path.exists(MANIFEST_PATH):
        print(f"Erro: Arquivo {MANIFEST_PATH} não encontrado!")
        return

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest["fusions"] = EXPANDED_FUSIONS

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)

    print(f"Injeção de Fusões concluída!")
    print(f"Total de Novas Fusões Ativas: {len(EXPANDED_FUSIONS)}")
    for i, fus in enumerate(EXPANDED_FUSIONS, 1):
        print(f"  {i:02d}. {fus['with'][0]} + {fus['with'][1]} -> {fus['result']}")

if __name__ == "__main__":
    inject_fusions()
