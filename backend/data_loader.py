import json
import os

# 计算 data/static 的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_PATH = os.path.join(BASE_DIR, "data", "static")

def load_json(filename):
    path = os.path.join(STATIC_PATH, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load {filename}: {e}")
        return {}

def load_all_data():
    print("🔹 Loading static TFT data...")
    champions = load_json("tft_champions.json")
    traits = load_json("tft_traits.json")
    items = load_json("tft_items.json")

    print(f"✅ Loaded {len(champions)} champions, {len(traits)} traits, {len(items)} items")
    return champions, traits, items

if __name__ == "__main__":
    load_all_data()
