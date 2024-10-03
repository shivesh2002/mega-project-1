
# if __name__=="__main__":
#     speak("intializing jarvis...")
#     while True: 
#         #listen for the wake word sharmaji
#         #obtain audio from the microphone
#         r = sr.Recognizer()
        
        
#         print("recongizing...")
#         try:
#             with sr.Microphone() as source:
#                  print("listening...")
#                  audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             command = r.recognise_google(audio) 
#             print(command)
#         except Exception as e:
#             print("error; {0}".format(e))