import os

BASE_DIR = '/Users/junuk/Downloads/digimon-codex-kr/data/digi_illustration'

def rename_ilst_images():
    for folder in os.listdir(BASE_DIR):
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(folder_path):
            continue

        for filename in os.listdir(folder_path):
            if filename.endswith('_ilst.png') and not filename.startswith('_'):
                new_name = '_ilst.png'
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)

                # 덮어쓰지 않도록 기존 파일 확인
                if os.path.exists(new_path):
                    print(f'❌ 이미 존재함: {new_path}, 건너뜀')
                    continue

                os.rename(old_path, new_path)
                print(f'✅ {filename} → {new_name}')

if __name__ == '__main__':
    rename_ilst_images()
