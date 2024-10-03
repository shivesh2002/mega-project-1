import speech_recognition as sr
import webbrowser
import pyttsx3
 
recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")



if __name__=="__main__":
    speak("intializing jarvis...")
    while True: 
        
        
        print("recongizing...")
        try:
            with sr.Microphone() as source:
                 print("listening...")
                 audio = recogniser.listen(source, timeout=2, phrase_time_limit=1)
            word = recogniser.recognize_google(audio) 
            if(word.lower()=="jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active..")
                    audio = recogniser.listen(source)
                    command = recogniser.recognize_google(audio)
                    processcommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")