import os
import json
from urllib.parse import quote  # 🔸 URL-safe 처리용

BASE_DIR = './data/digi_illustration'
OUTPUT_FILE = os.path.join(BASE_DIR, 'digimons.json')

def extract_info(folder):
    script_path = os.path.join(BASE_DIR, folder, 'script.json')
    if not os.path.isfile(script_path):
        return None
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return {
            'name': data.get('name'),
            'element': data.get('element'),
            'type': data.get('type'),
            'role': data.get('role', ''),
            'folderName': folder,
            'folderUrl': quote(folder),  # ✅ URL 인코딩된 폴더명
            'grade': data.get('grade', 25),
            'category': data.get('category', 'Z진화')
        }
    except Exception as e:
        print(f"[오류] {folder}/script.json: {e}")
        return None

def main():
    entries = []
    for folder in sorted(os.listdir(BASE_DIR)):
        full_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(full_path):
            info = extract_info(folder)
            if info:
                entries.append(info)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"✅ {OUTPUT_FILE} 생성 완료 ({len(entries)}개 디지몬)")

if __name__ == '__main__':
    main()
