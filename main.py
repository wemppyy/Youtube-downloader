import os
import yt_dlp
from time import sleep

# Налаштування завантаження
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio',
    'outtmpl': 'videos/%(title)s.%(ext)s',
    'quiet': True,
    'noplaylist': True,
    'no_warnings': True,
}

# Створення папки для відео
os.makedirs('videos', exist_ok=True)

# Відкриття файлу з посиланнями
with open('links.txt', 'r') as file:
    links = [link.strip() for link in file.readlines()]

# Завантаження відео з прогресом
for idx, link in enumerate(links, start=1):
    print(f"[{idx}/{len(links)}] Завантаження: {link}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"✅ Відео {idx} завантажено успішно.\n")
    except Exception as e:
        print(f"❌ Помилка при завантаженні {link}: {e}\n")
    sleep(0.5)

print("Усі завантаження завершено! 🎉\n")
input("Натисніть Enter для виходу...")