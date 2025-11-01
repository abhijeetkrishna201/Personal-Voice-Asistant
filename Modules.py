import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import datetime
import random
import wavio
import sounddevice as sd
import time

# --- Initialization (Done only ONCE) ---
try:
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("AI Initialized. Microphone is ready.")
except Exception as e:
    print(f"Error during initialization: {e}")
    print("Please ensure you have a microphone connected and necessary drivers.")
    exit()

# --- Configuration ---
AI_NAME = "Brother's AI"
USERNAME = "sir"
CREATED_BY = "Mr. Abhijeet Krishna Budhak"
DYNAMIC_VALUE=" ."
# --- Helper Functions ---

def speak(text):
    """Queues text to be spoken (does not block)."""
    print(f"{AI_NAME}: {text}")
    engine.say(text)
 

def listen_for_command():
    """Listens for a command and returns it as text."""
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"{USERNAME}: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.{DYNAMIC_VALUE}")
            engine.runAndWait() # Speak the error now
            return None
        except Exception as e:
            speak(f"An unexpected error occurred: {e}")
            engine.runAndWait() # Speak the error now
            return None

# --- Core Feature Functions ---

def greet_user():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12: greeting = "Good morning"
    elif 12 <= hour < 18: greeting = "Good afternoon"
    else: greeting = "Good evening"
    
    speak(f"Hello {USERNAME}, {greeting}. I am {AI_NAME}, created by {CREATED_BY}. How may I help you today?")

def get_time():
    """Tells the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p") 
    engine.say(" ... ")
    speak(f"The current time is {DYNAMIC_VALUE} {current_time}")

def get_date():
    """Tells the current date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

    engine.say(" ... ")
    speak(f"Today is {DYNAMIC_VALUE} {current_date}")

def open_application(command):
    """Opens an application by name (for Windows)."""
    app_name = command.replace("open", "").strip()
    if not app_name:
        engine.say(" ... ")
        speak("Which application would you like to open?")
        return
        
    try:
        os.startfile(f"{app_name}.exe")

    except FileNotFoundError:
        speak(f"Sorry, I could not find the application named {app_name}.")
    except Exception:
        speak(f"Sorry, an error occurred while trying to open {app_name}.")
    

def search_web(command):
    """Searches Google for the given query."""
    search_query = command.replace("search", "").strip()
    if not search_query:
        speak("What would you like me to search for?")
        return

    url = f"https://www.google.com/search?q={search_query}"
    speak(f"Searching Google for {search_query}...")
    webbrowser.open(url)
    
def record_audio():
    """Records audio for 10 seconds and saves it as a .wav file."""
    speak("Starting a 10-second recording now.")
    samplerate = 44100
    duration = 10
    
    try:
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
        sd.wait()
        
        random_num = random.randint(100, 999)
        filename = f"voice_rec_{random_num}.wav"
        wavio.write(filename, recording, samplerate, sampwidth=2)
        speak(f"Recording saved as {filename}.")
    except Exception as e:
        speak("Sorry, I could not record audio..")
        print(f"Recording Error: {e}")

# --- Main Execution Loop ---

if __name__ == "__main__":
    greet_user()
    engine.runAndWait() # Speak the initial greeting

    while True:
        command = listen_for_command()
        
        if command:
            # --- Command Processing ---
            if "open" in command:
                open_application(command)
                engine.runAndWait()
            
            elif "time" in command:
                get_time()
                engine.runAndWait()

            elif "date" in command:
                get_date()
                engine.runAndWait()
                
            elif "search" in command:
                search_web(command)
                engine.runAndWait()
                
            elif "record" in command :
                record_audio()
                engine.runAndWait()

            elif "exit" in command or "terminate" in command or "goodbye" in command or "close" in command:
                engine.say(" ... ")
                speak(f"Goodbye, {USERNAME}! Have a great day. Thank You!")
                print("Exiting ..........")
                print("Thank You ..........")
                engine.runAndWait() # Speak the goodbye message before exiting
                time.sleep(5) 
                break
                
            else:
                engine.say(" ... ")
                speak("I'm not sure how to handle that command.")
                engine.runAndWait()