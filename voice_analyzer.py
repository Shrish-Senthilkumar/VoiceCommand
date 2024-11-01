import speech_recognition as sr
import pyttsx3 
import numpy as np 
from nltk.stem import PorterStemmer
from pydub import AudioSegment
import io
# Initialize the recognizer 
r = sr.Recognizer() 
 
# Function to convert text to
# speech
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

while(1):    
    ps = PorterStemmer() 
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2)
            

            audio = AudioSegment.from_mp3("C:\\Users\\shris\\Downloads\\IMG_8791.mp3")
            extracted = audio[1:10]
            buffer = io.BytesIO()
            extracted.export(buffer, format="wav")
            buffer.seek(0)
            
            #r =
            print(type(audio2))
            print(type(audio))
            print(type(buffer))
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            spokenWords = np.array(MyText.split())
                        
            commands = ["speed", "go to", "exit", "start",""]

            for i in commands:
                for j in range(len(spokenWords)-1):
                    if(ps.stem(spokenWords[j]) == i):
                        print(i)
                    if((ps.stem(spokenWords[j]) + " " + ps.stem(spokenWords[j + 1]) == i)):
                        print(i)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
