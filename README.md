**🎬 YouTube Downloader (Audio/Video)**

This is a simple command-line Python application that allows

 users to download YouTube videos or extract audio in MP3 format.
 
  It uses the powerful `yt-dlp` library and supports input validation and error handling.

**🔗 GitHub Repository:**  
[https://github.com/Pepuhove/python-app-development.git](https://github.com/Pepuhove/python-app-development.git)

---

**📦 Features**

- ✅ Download YouTube **videos** in the best available quality  
- ✅ Download **audio only** (MP3 format)  
- ✅ Automatically creates a `downloads/` folder  
- ✅ Validates user input for download type  
- ✅ Gracefully handles common errors  

---

**🔧 Requirements**

- Python 3.7 or higher  
- `yt-dlp` Python package  
- `ffmpeg` installed and available in your system PATH (for audio conversion)

---

**🚀 Installation**

**1. Clone the repository**
```bash
git clone https://github.com/Pepuhove/python-app-development.git
cd python-app-development
2. Install dependencies


pip install yt-dlp
3. Install ffmpeg

Windows (using Chocolatey)
Run PowerShell as Administrator:


choco install ffmpeg
Linux (Debian/Ubuntu)


sudo apt update && sudo apt install ffmpeg
macOS (using Homebrew)


brew install ffmpeg
💻 Usage


python youtube_downloader.py
Sample Flow:

Enter YouTube URL: https://youtu.be/example


Choose download type:
1. Video
2. Audio only
Enter 1 or 2: 2


⏳ Downloading...
✅ Download completed successfully.
Downloads will be saved to the downloads/ directory.


⚠️ Error Handling

Invalid YouTube URL → handled with a friendly error

Missing ffmpeg → informs the user if audio conversion fails

Invalid input (e.g. letters or wrong numbers) → prompts the user to try again

📄 License

This project is open-source and available under the MIT License.


🙌 Credits


Built with ❤️ using yt-dlp
