
# 🤖 Brother's AI — Your Personal Voice Assistant

**Brother's AI** is a lightweight, Python-based **voice-controlled desktop assistant**. It's built with a clean, modular design, allowing it to understand speech, respond with a natural voice, and perform helpful tasks.

This assistant uses core Python libraries like `speech_recognition`, `pyttsx3`, and `sounddevice` to bring intelligent voice interactions to your desktop, acting as a great foundation for a more complex AI project.

---

## 🧠 Core Features

* 🎙️ **Speech Recognition:** Understands spoken commands using the Google Speech Recognition API.
* 🗣️ **Text-to-Speech:** Provides clear, natural-sounding voice replies using `pyttsx3`.
* 🕒 **Time & Date:** Responds to queries for the current time and date.
* 🌐 **Web Search:** Can open a browser and search Google for any spoken query.
* 📂 **Application Launcher:** Opens installed desktop applications (e.g., "Open Chrome") via voice command.
* 🔴 **Voice Recorder:** Includes a function to record 10-second audio clips and save them as `.wav` files.
* 👋 **Personalized Greetings:** Greets the user appropriately based on the time of day.
* ❌ **Safe Exit:** Can be terminated gracefully with "exit" or "goodbye" commands.

---

## ⚙️ Installation & Setup

Make sure you have **Python 3.8+** installed.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/brothers-ai.git](https://github.com/yourusername/brothers-ai.git)
    cd brothers-ai
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Refer to used libraries mentioned below and install them respectively. 

    > **Note:** The `sounddevice` library may require you to install system-level dependencies like `portaudio`. If you encounter an error, please see the [sounddevice documentation](https://python-sounddevice.readthedocs.io/en/latest/installation.html) for guidance.

4.  **Run the assistant:**
    ```bash
    python main.py
    ```

---

## 🗂️ Project Structure



brothers-ai/
│
├── main.py               \# The core application logic
├── recordings/            \# (Optional) Directory for saved voice recordings
└── README.md              \# Project documentation



## 🎮 Example Commands

Here are a few commands you can try:

| Command | Function |
| :--- | :--- |
| What’s the time? | Tells the current time. |
| What’s today’s date? | Tells today’s date. |
| Open Chrome  | Opens the Google Chrome application. |
| Search Python tutorials | Performs a Google search for "Python tutorials". |
| Record my voice | Records 10 seconds of audio. |
| Exit / Goodbye | Exits the assistant gracefully. |


## 🧩 Technologies Used

* **Python 3**
* **Libraries:**
    * `speech_recognition` (for Google Speech API)
    * `pyttsx3` (for text-to-speech)
    * `sounddevice` (for audio I/O)
    * `wavio` (for saving audio files)
    * `datetime`, `os`, `webbrowser` (standard libraries)

## 🚀 Future Enhancements

* **Offline Recognition:** Integrate an offline model like `Vosk` for commands that don't need the web.
* **API Integration:** Connect to a generative AI (like Gemini or ChatGPT) for advanced Q&A.
* **Calendar & Reminders:** Add functionality to set reminders and read calendar events.
* **Music Control:** Implement controls for Spotify or local music playback.



## 👨‍💻 Author

**Abhijeet Krishna Budhak**

*🎓 Computer Science Engineer* *📍 Ballarpur Institute of Technology*


 “Turning code into companions that listen and respond.”



## 📄 License

This project is open-source and available under the **MIT License**.
