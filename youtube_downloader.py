import yt_dlp
import os

def create_downloads_folder():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

def get_download_choice():
    while True:
        print("\nChoose download type:")
        print("1. Video")
        print("2. Audio only")
        choice = input("Enter 1 or 2: ").strip()

        if not choice.isdigit():
            print("❌ Invalid input. Please enter a number (1 or 2).")
            continue

        choice = int(choice)
        if choice not in [1, 2]:
            print("❌ Invalid choice. Please enter 1 for video or 2 for audio.")
            continue

        return choice

def main():
    create_downloads_folder()

    video_url = input("Enter YouTube URL: ").strip()
    if not video_url:
        print("❌ No URL provided. Exiting.")
        return

    try:
        choice = get_download_choice()

        if choice == 1:
            # Video download options
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/%(title)s.%(ext)s'
            }
        else:
            # Audio-only options
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

        print("\n⏳ Downloading...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("✅ Download completed successfully.")

    except Exception as e:
        print(f"❌ Download error: {e}")

if __name__ == "__main__":
    main()
