import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error fetching results from Google Speech Recognition service: {e}")
        return ""

# Main function
def main():
    speak("Hello! How can I assist you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I assist you today?")
        elif "time" in query:
            now = datetime.datetime.now()
            time = now.strftime("%I:%M %p")
            speak(f"The current time is {time}")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
