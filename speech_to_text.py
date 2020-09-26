from speech_recognition import *

while(True):
  recognizer = Recognizer() # Creating a Recognizer object to have access to it's functions
  with Microphone() as source: 
    print("Say something: ")
    get_audio = recognizer.listen(source) # Variable to hold the audio input
    try:
      audio_to_text = r.recognize_google(get_audio) # Converting audio to text via google API
      print('{}'.format(audio_to_text))
      if(audio_to_text) == 'stop': break # Condition to stop the program form running
    except:
      print("Can you repeat?? Couldn't listen clearly") # exception in case the audio is not listen clearly
