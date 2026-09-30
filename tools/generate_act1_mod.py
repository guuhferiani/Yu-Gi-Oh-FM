import os
import json

MOD_DIR = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "mods", "overhaul-mod")
os.makedirs(MOD_DIR, exist_ok=True)

manifest = {
    "id": "overhaul-mod",
    "name": "Forbidden Memories Overhaul",
    "version": "1.0",
    "author": "Antigravity & Gustavo",
    "description": "Rebalanceamento do Ato 1 (Egito Inicial): Drops justos com Baby Dragon, Time Wizard, Dark Magician e Blue-Eyes, além de fusões lógicas.",
    "enabled": True,
    "restart": False,
    "drops": {
        "Simon Muran": {
            "pow": {
                "Time Wizard": 120,
                "Phantom Dewan": 120,
                "Genin": 120,
                "Doma The Angel of Silence": 80,
                "Dark Magician": 40
            },
            "tec": {
                "Raigeki": 60,
                "Dian Keto the Cure Maiden": 100,
                "Red Medicine": 150,
                "Sparks": 150
            }
        },
        "Jono": {
            "pow": {
                "Baby Dragon": 180,
                "Time Wizard": 120,
                "Swordsman of Landstar": 150,
                "Kojikocy": 120,
                "Armored Lizard": 100,
                "Red-eyes B. Dragon": 40
            },
            "tec": {
                "Kunai with Chain": 100,
                "Legendary Sword": 100,
                "Salamandra": 80
            }
        },
        "Teana": {
            "pow": {
                "Mystical Elf": 160,
                "Harpie Lady": 120,
                "Water Omotics": 140,
                "Arlownay": 140,
                "Dark Plant": 140
            },
            "tec": {
                "Dian Keto the Cure Maiden": 120,
                "Silver Bow and Arrow": 100
            }
        },
        "Seto": {
            "pow": {
                "Battle Ox": 160,
                "Koumori Dragon": 160,
                "Crawling Dragon": 120,
                "Ryu-kishin Powered": 100,
                "Blue-eyes White Dragon": 40
            },
            "tec": {
                "Dragon Treasure": 120,
                "Dark Hole": 80
            }
        }
    },
    "fusions": [
        {"with": ["Baby Dragon", "Time Wizard"], "result": "Thousand Dragon"},
        {"with": ["Baby Dragon", "Dragon Zombie"], "result": "Curse of Dragon"},
        {"with": ["Time Wizard", "Kojikocy"], "result": "Flame Swordsman"}
    ]
}

manifest_path = os.path.join(MOD_DIR, "mod.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4, ensure_ascii=False)

print(f"Mod Overhaul gerado com sucesso em: {manifest_path}")
