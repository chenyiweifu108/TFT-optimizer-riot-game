import requests
import json

urls = {
    "champions": "https://raw.communitydragon.org/latest/cdragon/tft/en_us.json",
    "traits": "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/tfttraits.json",
    "items": "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/tftitems.json"
}

for name, url in urls.items():
    try:
        print(f"🔎 Trying {name} from {url}")
        r = requests.get(url, timeout=10)
        data = r.json()
        with open(f"tft_{name}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved {name} ({len(data)} entries)")
    except Exception as e:
        print(f"❌ Failed {name}: {e}")
