import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []

    def __init__(self, name = None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name
        
        print("Listening now...")

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    @property  
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.say(sentence)
    
    def listen(self):
        print("Please say your request")
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it!")
        
        phrase = self.r.recognize_google(audio, show_all= False, language = 'en-USA')
        sentence = "Got it! You said the following" + phrase
        self.say(sentence)
        print("You said", phrase)
        return phrase
        
        
        
    
