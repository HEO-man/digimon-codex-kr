import os

BASE_DIR = '/Users/junuk/Downloads/digimon-codex-kr/data/digi_illustration'

def rename_ilst_images():
    for folder in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(folder_path):
            continue

        for filename in os.listdir(folder_path):
            if filename == '_ilst.png':
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, 'ilst.png')

                # 충돌 방지
                if os.path.exists(new_path):
                    print(f'❌ ilst.png 이미 존재함 → 건너뜀: {new_path}')
                    continue

                os.rename(old_path, new_path)
                print(f'✅ {filename} → ilst.png')

if __name__ == '__main__':
    rename_ilst_images()
