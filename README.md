# Jarvis: Voice-Controlled AI Desktop Assistant 🤖

---

## 🚀 Features

- 🎙️ Voice interaction (speech-to-text & text-to-speech)
- 🚀 Launch apps & websites by voice
- 🎵 Play local songs or open YouTube links
- 🤖 Answer questions using the Google Gemini API
- 🌦️ Tell you the time and weather
- ⏻ System commands (shutdown, restart, logout)
- 🚪 Exit gracefully with “exit”, “quit”, or “stop”

---

## 🧱 Built With

- SpeechRecognition – for listening to commands  
- pyttsx3 – for speaking responses  
- playsound3 – for audio playback  
- Google Gemini API – for answering queries
- Python standard libraries: subprocess, json, webbrowser  
- Modular design following best practices

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Developer-Tanay/Jarvis.git
   cd Jarvis
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # On Mac/Linux: source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Gemini API key:

   - Create a `.env` file in the project root:
     ```bash
     echo GEMINI_API_KEY=your-api-key > .env
     ```
   - Replace `your-api-key` with your actual Gemini API key (get it from Google Cloud Console or Gemini API dashboard).

5. Configure your favorites:

   Edit `config/lists.json` to customize:

   - **programs** (e.g., `"vscode": "C:\\...\\Code.exe"`)
   - **websites** (e.g., `"youtube": "https://youtube.com"`)
   - **songs** (e.g., `"chill": "C:\\Music\\chill.mp3"` or YouTube links)

6. Launch Jarvis:

   ```bash
   python main.py
   ```

---

## 🎙️ Usage Examples

- **Open apps/websites**:
  “Open VSCode” → launches VS Code  
  “Open YouTube” → opens your browser

- **Play music**:
  “Play believer” → plays MP3 file or opens YouTube link

- **Ask questions**:
  “Tell me about quantum physics” → queries the Gemini API, reads result

- **System commands**:
  “What's the time?” | “What's the weather?”  
  “Shutdown” | “Restart” | “Logout” | “Exit”

---

## 🧩 Project Structure

```
Jarvis-Voice-Assistant/
├─ config/
│   ├─ lists.json        # User-customizable favorites
│   ├─ lists_loader.py   # Loads and validates JSON
│   └─ settings.py       # Configuration settings
├─ core/
│   ├─ assistant.py      # Main logic and voice loop
│   ├─ recognizer.py     # Speech recognition
│   └─ speaker.py        # Text-to-speech
├─ modules/
│   ├─ browser.py        # Opens websites
│   ├─ player.py         # Plays songs/YouTube
│   ├─ program.py        # Launches programs
│   ├─ system.py         # OS commands
│   ├─ time.py           # Tells the time
│   └─ weather.py        # Fetches weather info
├─ utils/
│   └─ google_genai.py   # Integrates Google Gemini API
├─ .env                 # Environment variables (e.g., Gemini API key)
├─ .gitignore           # Git ignore file
├─ main.py              # Entry point
├─ requirements.txt     # Dependencies
├─ LICENSE              # MIT License
└─ README.md            # You're here!
```

---

## 📌 Contribution

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature/foo`)
5. Submit a pull request

Please add unit tests and update documentation for new features.

---

## 🛣️ Roadmap

- Hotword activation (e.g., “Hey Jarvis”)
- Pause/stop playback commands
- GUI integration using PyQt/Tkinter
- Packaging as executable with PyInstaller or Docker

---

## 🙋 Credits

Built and maintained by **Tanay Paul** – [GitHub Profile](https://github.com/Developer-Tanay)  
Inspired by popular voice assistant frameworks and community contributions.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For questions or support, reach out via [GitHub Issues](https://github.com/Developer-Tanay/Jarvis/issues) or email **[pault4245@gmail.com](mailto:pault4245@gmail.com)**.

---

**Thank you for using Jarvis!** 🎉