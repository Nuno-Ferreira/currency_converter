"""
My first application that converts any currency in seconds
"""
#from lib2to3.pytree import convert
import toga
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, Pack
import currency_converter


#lets start again but with toga

def build(app):
    c1_box = toga.Box()
    c2_box = toga.Box()
    m_box = toga.Box() #need to add a section for the amount that I want to convert
    mc_box = toga.Box() #for the amount converted
    box = toga.Box()

    c1_input = toga.TextInput()
    c2_input = toga.TextInput()
    #I need to create 3 inputs for the currencies and the amount
    m_input = toga.TextInput()
    mc_input = toga.TextInput(readonly=True)

    c1_label = toga.Label('Currency to convert from', style=Pack(text_align=LEFT))
    c2_label = toga.Label('Currency to convert to', style=Pack(text_align=LEFT))
    join_label = toga.Label('Converts to', style=Pack(text_align=RIGHT))
    m_label = toga.Label('Amount to convert', style=Pack(text_align=RIGHT))
    mc_label = toga.Label('Converted amount:', style=Pack(text_align=RIGHT))


    def convert(widget): #make this connnect to the currencyconverter script
        c1_input.value = currency_converter.currency_to_convert_from
        c2_input.value = currency_converter.currency_to_convert_to
        m_input.value = currency_converter.amount_to_convert
        if c1_input.value == int():
            return #maybe add a pop up error message saying it cant take any integers values


    button = toga.Button('Convert', on_press=convert)
# need to stylize the other 2 boxes

    c2_box.add(c2_input)
    c2_box.add(c2_label)

    c1_box.add(join_label)
    c1_box.add(c1_input)
    c1_box.add(c1_label)

    m_box.add(m_input)
    m_box.add(m_label)

    mc_box.add(mc_input)
    mc_box.add(mc_label)

    box.add(c2_box)
    box.add(c1_box)
    box.add(m_box)
    box.add(mc_box)
    box.add(button)


    #this where the styling happens, it looks similar to CSS
    #box styling(?)
    box.style.update(direction=COLUMN, padding_top=10)
    c2_box.style.update(direction=ROW, padding=5)
    c1_box.style.update(direction=ROW, padding=5)
    m_box.style.update(direction=ROW, padding=5)
    mc_box.style.update(direction=ROW, padding=5)

    #input styling
    c1_input.style.update(flex=1)
    c2_input.style.update(flex=1, padding_left=160)
    m_input.style.update()
    mc_input.style.update()

    #labels styling
    c1_label.style.update(width=100, padding_left=10)
    c2_label.style.update(width=100, padding_left=10)
    m_label.style.update(width=100, padding_left=10)
    mc_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=150, padding_right=10)

    #button styling
    button.style.update(padding=15, flex=1)

    return box


def main():
   return toga.App('Currency converter', 'something', startup=build)


#some instructions/clarifications on the styling
""""
This example shows off some more features of Toga’s Pack style engine. In this example app, we’ve set up an outer box that stacks vertically; inside that box, 
we’ve put 2 horizontal boxes and a button.

Since there’s no width styling on the horizontal boxes, they’ll try to fit the widgets they contain into the available space. 
The TextInput widgets have a style of flex=1, but the Label widgets have a fixed width; as a result, 
the TextInput widgets will be stretched to fit the available horizontal space. The margin and padding terms then ensure that the widgets 
will be aligned vertically and horizontally.

"""



#import android
#from android.util import Log
#from android.widget import LinearLayout
#from android.widget import Button
#from android.widget import TextView
#from android.view import Gravity
#import android.view


#this was a mistake // this is if I was trying ot build with VOC (another transpiler)
"""
class ButtonClick(implements=android.view.View[OnClickListener]):
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

    def onClick(self, view: android.view.View) -> void:
        self.callback(*self.args, **self.kwargs)


class CurrencyConverter:
    def __init__(self):
        self.activity = android.PythonActivity.setListener(self)
        self.buttons = []
        

    def onCreate(self):
        
        self.convert_button = Button(self._activity)
        self.convert_button.setText('Convert')
        self.convert_button.setOnClickListener(ButtonClick(self.convert_currency)) #this will make the connection for the app to convert
        vlayout.addView(self.convert_button)

        footer = TextView(self._activity) #this will set the footer and the self_activity will communicate with pythonactivity 
        footer = setText('Powered by Python')
        footer.setGravity(Gravity.CENTER) #this will position the text
        vlayout.addView(footer) #still need to find out what it does but maybe it adds it to the screen

    def convert_currency(self):
        self.activity
        self.message = None
        self.runScript()

    def runScript(self):


#might need this in the future to build the toga app

class CurrencyConverter(toga.App):
    def __init__(self):
        self.buttons = []
        

    def startup(self):
        
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)



        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def say_hello(self, widget):
        print("Hello,", self.name_input.value)
"""
