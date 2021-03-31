
import gnupg

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty
from kivy.uix.slider import Slider
from kivy.graphics import *
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp, sp

import os

os.environ['KIVY_METRICS_DENSITY'] = '2.5'

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        Window.size = (dp(800), dp(500))
        self.message = ""

        with self.canvas.before:
            Color(0, 0.05, 0.15)
            Rectangle(pos=(0, 0), size=(dp(2000), dp(2000)))

        self.screen1()

    def screen1(self, *args):
    	self.clear_widgets()

    	self.padAnchor0 = AnchorLayout(size_hint=(1, 0.7)) #Value Display
    	self.out = TextInput(multiline=True, size_hint=(0.95, 0.9), font_size = dp(20))
    	self.padAnchor0.add_widget(self.out)
    	self.add_widget(self.padAnchor0)


    	bottom = BoxLayout(orientation='horizontal', size_hint=(1, 0.3)) #Botttom Bar

    	self.padAnchor1 = AnchorLayout(size_hint_y=0.5, anchor_x='right') #Passcode Enter
    	self.textinput1 = TextInput(hint_text='password', size_hint_y=None, height=dp(30), size_hint_x=None, width=dp(250), font_size=dp(20), multiline=False)
    	self.padAnchor1.add_widget(self.textinput1)
    	bottom.add_widget(self.padAnchor1)

    	self.padAnchor2 = AnchorLayout(size_hint_y=0.5, size_hint_x=0.3, anchor_x='center') #Passcode Submit Button
    	self.password = Button(size_hint_y=None, height=dp(30), size_hint_x=None, width=dp(100), text='submit')
    	self.password.bind(on_press=self.display)
    	self.padAnchor2.add_widget(self.password)
    	bottom.add_widget(self.padAnchor2)

    	self.padAnchor3 = AnchorLayout(size_hint_y=0.5, size_hint_x=0.3, anchor_x='center') #Change passcode button
    	self.change = Button(size_hint_y=None, height=dp(30), size_hint_x=None, width=dp(150), text='change passcode')
    	self.change.bind(on_press=self.screen2)
    	self.padAnchor3.add_widget(self.change)
    	bottom.add_widget(self.padAnchor3)

    	self.padAnchor4 = AnchorLayout(size_hint_y=0.5, size_hint_x=0.3, anchor_x='center') #Save Button
    	self.save = Button(size_hint_y=None, height=dp(30), size_hint_x=None, width=dp(100), text='modify')
    	self.save.bind(on_press=self.screen3)
    	self.padAnchor4.add_widget(self.save)
    	bottom.add_widget(self.padAnchor4)

    	self.add_widget(bottom)

    def screen2(self, *args):
    	if not self.test(): #Make sure password is inputted and correct
    		return 

    	self.clear_widgets()

    	mainBar = BoxLayout(orientation='horizontal')

    	self.padAnchor1 = AnchorLayout(size_hint_y=1, size_hint_x=0.6, anchor_x='right') #Passcode Enter
    	self.newpass = TextInput(hint_text='new password', size_hint_y=None, height=dp(30), size_hint_x=0.6, font_size=dp(20), multiline=False)
    	self.padAnchor1.add_widget(self.newpass)
    	mainBar.add_widget(self.padAnchor1)

    	self.padAnchor2 = AnchorLayout(size_hint_y=1, size_hint_x=0.2, anchor_x='center') #Submit button
    	self.submit = Button(text='submit', size_hint_y=None, size_hint_x=None, height=dp(30), width=dp(100))
    	self.submit.bind(on_press=self.resavePass)
    	self.padAnchor2.add_widget(self.submit)
    	mainBar.add_widget(self.padAnchor2)

    	self.padAnchor3 = AnchorLayout(size_hint_y=1, size_hint_x=0.2, anchor_x='left') #Home button
    	self.home = Button(text='home', size_hint_y=None, size_hint_x=None, height=dp(30), width=dp(100))
    	self.home.bind(on_press=self.screen1)
    	self.padAnchor3.add_widget(self.home)
    	mainBar.add_widget(self.padAnchor3)

    	self.add_widget(mainBar)

    def screen3(self, *args):
    	if not self.test(): #Make sure password is inputted and correct
    		return 

    	self.clear_widgets()

    	mainBar = BoxLayout(orientation='vertical')

    	self.padAnchor1 = AnchorLayout(anchor_x='center', size_hint_y=0.7) #Passcode Enter
    	self.newText = TextInput(multiline=True, size_hint=(0.95, 0.9), font_size = dp(20), text=self.message)
    	self.padAnchor1.add_widget(self.newText)
    	mainBar.add_widget(self.padAnchor1)

    	self.padAnchor2 = AnchorLayout(anchor_x='center', size_hint_y=0.15) #Submit button
    	self.submit = Button(text='submit', size_hint_y=None, size_hint_x=None, height=dp(30), width=dp(100))
    	self.submit.bind(on_press=self.resaveText)
    	self.padAnchor2.add_widget(self.submit)
    	mainBar.add_widget(self.padAnchor2)

    	self.padAnchor3 = AnchorLayout(anchor_x='center', size_hint_y=0.15) #Home button
    	self.home = Button(text='home', size_hint_y=None, size_hint_x=None, height=dp(30), width=dp(100))
    	self.home.bind(on_press=self.screen1)
    	self.padAnchor3.add_widget(self.home)
    	mainBar.add_widget(self.padAnchor3)

    	self.add_widget(mainBar)


    def resaveText(self, *args): #Save cipher after changing passcode
    	passcode = self.passcode
    	gpg = gnupg.GPG()
    	self.message = self.newText.text
    	newCipher =  str(gpg.encrypt(self.message, recipients=None, symmetric='AES256', passphrase=passcode, armor=True))

    	outFile = open("keys2.txt.gpg", "wb")
    	outFile.write(newCipher.encode('ascii'))
    	outFile.close()

    	self.screen1()

    def resavePass(self, *args): #Save cipher after changing passcode
    	passcode = self.newpass.text
    	gpg = gnupg.GPG()
    	newCipher =  str(gpg.encrypt(self.message, recipients=None, symmetric='AES256', passphrase=passcode, armor=True))

    	outFile = open("keys2.txt.gpg", "wb")
    	outFile.write(newCipher.encode('ascii'))
    	outFile.close()

    	self.screen1()

    def test(self, *args):
        gpg = gnupg.GPG()
        inFile = open("keys2.txt.gpg", "rb")

        self.passcode = self.textinput1.text if self.textinput1.text else '0' 
        passcode = self.passcode
        self.textinput1.text = "" #reset password input bar
        message = str(gpg.decrypt_file(inFile, passphrase=passcode))
        inFile.close()

        if message == "":
            self.out.text = "FAIL"
            with self.canvas.before:
            	Color(0.45, 0, 0.05)
            	Rectangle(pos=(0, 0), size=(dp(2000), dp(2000)))
            return False
        else:
        	self.message = message
        	with self.canvas.before:
        		Color(0, 0.05, 0.15)
        		Rectangle(pos=(0, 0), size=(dp(2000), dp(2000)))

        return True

    	
    def display(self, *args):
        print(self.textinput1.text)

        gpg = gnupg.GPG()
        inFile = open("keys2.txt.gpg", "rb")

        passcode = self.textinput1.text if self.textinput1.text else '0' 
        self.textinput1.text = ""
        message = str(gpg.decrypt_file(inFile, passphrase=passcode))
        inFile.close()

        if message == "":
            self.out.text = "FAIL"
            with self.canvas.before:
            	Color(0.45, 0, 0.05)
            	Rectangle(pos=(0, 0), size=(dp(2000), dp(2000)))
        else:
            self.out.text = message
            self.message = message
            with self.canvas.before:
            	Color(0, 0.05, 0.15)
            	Rectangle(pos=(0, 0), size=(dp(2000), dp(2000)))


class MyApp(App):

    def build(self):
        self.title = 'Password Manager'
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()