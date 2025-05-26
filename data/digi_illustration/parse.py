import json
from urllib.parse import quote

with open('/Users/junuk/Downloads/digimon-codex-kr/data/digi_illustration/digimons.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    name = item.get('name')
    item['folderName'] = name
    item['folderUrl'] = quote(name)

with open('digimons_kor.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
