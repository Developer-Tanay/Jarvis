# core/assistant.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add project root to path

from core.recognizer import Recognizer
from core.speaker import Speaker
from modules import browser, system, program, player
from modules import time as time_module
from modules import weather as weather_module
from utils.google_genai import generate_response  # Import the Gemini API function

class Assistant:
    def __init__(self):
        self.recognizer = Recognizer()
        self.speaker = Speaker()

    def process_command(self, command):
        command = command.lower().strip()
        if not command:
            return None

        # Open favorite websites
        if command.startswith("open "):
            target = command.split("open ", 1)[1].strip()
            # Try browser websites
            if browser.open_website(target):
                self.speaker.speak(f"Opening {target}")
            # Try opening programs
            elif program.open_program(target):
                self.speaker.speak(f"Opening {target}")
            else:
                self.speaker.speak(f"Sorry, I can't open \"{target}\"")

        elif command.startswith("play "):
            key = command.split("play ", 1)[1].strip().strip('"')
            if player.play_song(key):
                self.speaker.speak(f"Playing {key}")
            else:
                self.speaker.speak(f"Sorry, couldn't find or play \"{key}\"")

        elif "jarvis" in command:
            self.speaker.speak("Ya")

        elif "shutdown" in command:
            self.speaker.speak("Shutting down system")
            system.shutdown_system()

        elif "time" in command:
            text = time_module.tell_time()
            self.speaker.speak(text)

        elif "weather" in command:
            summary = weather_module.get_weather()
            self.speaker.speak(summary)

        elif "tell me about" in command:
            topic = command.split("tell me about", 1)[1].strip()
            response = generate_response(f"Tell me about {topic}")  # Directly use Gemini API
            if response:
                self.speaker.speak(response)
            else:
                self.speaker.speak("Sorry, I couldn't fetch information about that topic.")

        elif command in ("quit", "exit", "stop"):
            self.speaker.speak("Goodbye!")
            return "EXIT"

        else:
            self.speaker.speak("I didn't understand that command.")

        return None