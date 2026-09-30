import os
import json
import struct

MOD_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")
ORIGINAL_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
MOD_JSON_PATH = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "mods", "overhaul-mod", "mod.json")

SECTOR_SIZE = 2352
HEADER_SIZE = 24
WA_MRG_LBA = 10102
DROPS_BASE_WA_OFFSET = 0xE99800
DUELIST_DATA_SIZE = 6144 # 3 sectors x 2048 bytes

OPPONENTS_MAP = {
    'Simon Muran': 0,
    'Teana': 1,
    'Jono': 2,
    'Villager 1': 3,
    'Villager 2': 4,
    'Villager 3': 5,
    'Seto': 6,
    'Heishin': 7,
    'Rex Raptor': 8,
    'Weevil Underwood': 9,
    'Mai Valentine': 10,
    'Bandit Keith': 11,
    'Shadi': 12,
    'Yami Bakura': 13,
    'Pegasus': 14,
    'Isis': 15,
    'Kaiba': 16,
    'Mage Soldier': 17,
    'Jono 2nd': 18,
    'Teana 2nd': 19,
    'Ocean Mage': 20,
    'High Mage Secmeton': 21,
    'Forest Mage': 22,
    'High Mage Anubisius': 23,
    'Mountain Mage': 24,
    'High Mage Atenza': 25,
    'Desert Mage': 26,
    'High Mage Martis': 27,
    'Meadow Mage': 28,
    'High Mage Kepura': 29,
    'Labyrinth Mage': 30,
    'Seto 2nd': 31,
    'Guardian Sebek': 32,
    'Guardian Neku': 33,
    'Heishin 2nd': 34,
    'Seto 3rd': 35,
    'DarkNite': 36,
    'Nitemare': 37,
    'Duel Master K': 38,
}

def read_wa_slice_from_bin(bin_path, wa_offset, length):
    start_sector = wa_offset // 2048
    offset_in_sector = wa_offset % 2048
    sectors_needed = (offset_in_sector + length + 2047) // 2048

    buf = bytearray()
    with open(bin_path, "rb") as f:
        for s in range(sectors_needed):
            f.seek((WA_MRG_LBA + start_sector + s) * SECTOR_SIZE + HEADER_SIZE)
            buf.extend(f.read(2048))
    return bytes(buf[offset_in_sector:offset_in_sector + length])

def write_wa_slice_to_bin(bin_path, wa_offset, data_to_write):
    length = len(data_to_write)
    start_sector = wa_offset // 2048
    offset_in_sector = wa_offset % 2048
    
    written = 0
    with open(bin_path, "r+b") as f:
        curr_sector = start_sector
        curr_offset_in_sector = offset_in_sector
        while written < length:
            chunk_size = min(length - written, 2048 - curr_offset_in_sector)
            f.seek((WA_MRG_LBA + curr_sector) * SECTOR_SIZE + HEADER_SIZE + curr_offset_in_sector)
            f.write(data_to_write[written:written + chunk_size])
            written += chunk_size
            curr_sector += 1
            curr_offset_in_sector = 0

def build_modified_pool(original_weights, mod_cards):
    new_weights = list(original_weights)
    target_indices = {int(cid) - 1: int(weight) for cid, weight in mod_cards.items()}
    new_weight_total = sum(target_indices.values())
    if new_weight_total >= 2048:
        raise ValueError(f"Soma dos novos pesos ({new_weight_total}) excede o limite do jogo (2048)!")

    remaining_budget = 2048 - new_weight_total
    other_sum = sum(new_weights[i] for i in range(722) if i not in target_indices)

    for idx, w in target_indices.items():
        new_weights[idx] = w

    if other_sum > 0:
        for i in range(722):
            if i not in target_indices and new_weights[i] > 0:
                scaled = int(round(new_weights[i] * remaining_budget / other_sum))
                if scaled == 0 and new_weights[i] > 0:
                    scaled = 1
                new_weights[i] = scaled

    # Adjust rounding differences
    total = sum(new_weights[:722])
    diff = 2048 - total
    if diff != 0:
        best_i = -1
        best_w = -1
        for i in range(722):
            if i not in target_indices and new_weights[i] > best_w:
                best_w = new_weights[i]
                best_i = i
        if best_i != -1:
            new_weights[best_i] += diff

    assert sum(new_weights[:722]) == 2048, f"Soma do pool ({sum(new_weights[:722])}) diferente de 2048!"
    return new_weights

def patch_all_drops():
    print("=" * 65)
    print("   Gravando Tabelas de Drop Rebalanceadas Diretamente na ROM")
    print("=" * 65)

    if not os.path.exists(MOD_BIN):
        print(f"[ERRO] ROM modificada não encontrada: {MOD_BIN}")
        return False

    with open(MOD_JSON_PATH, "r", encoding="utf-8") as f:
        mod_config = json.load(f)

    drops_config = mod_config.get("drops", {})
    source_bin = ORIGINAL_BIN if os.path.exists(ORIGINAL_BIN) else MOD_BIN

    total_patched = 0
    for duelist_name, pools in drops_config.items():
        if duelist_name not in OPPONENTS_MAP:
            print(f"[AVISO] Duelista '{duelist_name}' não mapeado, ignorando...")
            continue

        opp_idx = OPPONENTS_MAP[duelist_name]
        opp_base_wa = DROPS_BASE_WA_OFFSET + (opp_idx * DUELIST_DATA_SIZE)

        # Ler dados originais do duelista
        duelist_data = read_wa_slice_from_bin(source_bin, opp_base_wa, DUELIST_DATA_SIZE)
        pow_raw = duelist_data[1460:1460+1460]
        tec_raw = duelist_data[4380:4380+1460]

        pow_weights = list(struct.unpack("<730H", pow_raw))
        tec_weights = list(struct.unpack("<730H", tec_raw))

        # Modificar POW se especificado
        if "pow" in pools and pools["pow"]:
            new_pow = build_modified_pool(pow_weights, pools["pow"])
            new_pow_bytes = struct.pack("<730H", *new_pow)
            write_wa_slice_to_bin(MOD_BIN, opp_base_wa + 1460, new_pow_bytes)

        # Modificar TEC se especificado
        if "tec" in pools and pools["tec"]:
            new_tec = build_modified_pool(tec_weights, pools["tec"])
            new_tec_bytes = struct.pack("<730H", *new_tec)
            write_wa_slice_to_bin(MOD_BIN, opp_base_wa + 4380, new_tec_bytes)

        total_patched += 1
        print(f"  [OK] #{opp_idx:02d} {duelist_name:22s} -> Drops POW e TEC gravados na ROM!")

    print(f"\n[SUCESSO] Total de {total_patched} duelistas rebalanceados gravados na ROM!")
    return True

if __name__ == "__main__":
    patch_all_drops()
