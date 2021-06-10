from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.config import Config
from random import randint
#All import modules

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Disable multi-touch emulation
Window.size = (400, 200)
Window.clearcolor = (1, 1, 1, 1)
#Set size Windows and color BackGround in White
def conv(text):
    if isinstance(text, list):
        return "".join(text)
    return list(text)
#This function is designed for comfortable work with a string, converts text to a list and vice versa
class Content(BoxLayout):
	'''
		Creator: Fixiny1
		Version: 0.9.8
		Password Generator

	'''
    inputnum = ObjectProperty()
    output = ObjectProperty()
    num = ObjectProperty()
    lower = ObjectProperty()
    bigger = ObjectProperty()

    def generate_password(self): 	#Function at the push of a button
        num = self.num.active
        lower = self.lower.active
        bigger = self.bigger.active
        try:
            len_pass = int(self.inputnum.text)
            if not num and not lower and not bigger:
                self.output.text = "Please active one checkbox"
            else:
                password = []
                while len(password) < len_pass:
                	#Check lenght password
                    while True:
                        caracter = chr(randint(ord('0'), ord('z')))
                        if ord(caracter) in range(ord('A'), ord('Z')) and bigger:
                            break
                        if ord(caracter) in range(ord('a'), ord('z')) and lower:
                            break
                        if ord(caracter) in range(ord('0'), ord('9')) and num:
                            break
                        #Check all CheckBox

                    password.append(caracter)
                self.output.text = conv(password)
        except:
            self.output.text = "Please don't insert string"


class GenerateApp(App):
    def build(self):
        return Content()

if __name__ == "__main__":
    GenerateApp().run()