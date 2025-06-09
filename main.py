from core.assistant import Assistant
import speech_recognition as sr

def main():
    assistant = Assistant()
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Initializing Jarvis...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ready!")

    while True:
        with mic as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=None)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            result = assistant.process_command(command)

            if result == "EXIT":
                break
            
        except sr.UnknownValueError:
            # Not understood; optionally ignore
            pass
        except sr.RequestError as e:
            print(f"API request failed; {e}")

if __name__ == "__main__":
    main()
