# Import the required module for text  
#If you receive errors such as No module named win32com.client, 
# No module named win32, or No module named win32api, you will need to additionally install pypiwin32.

#pip install pyttsx3

# to speech conversion
import pyttsx3
  
# init function to get an engine instance for the speech synthesis 



def say(input_string):
    engine = pyttsx3.init()

    # say method on the engine that passing input text to be spoken
    engine.say(input_string)
  
    # run and wait method, it processes the voice commands. 
    engine.runAndWait()