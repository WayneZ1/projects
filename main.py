from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','width',350)
Config.set('graphics','height',500)
class MyApp(App):
    def build(self):
        self.form='0'
        bl=BoxLayout(orientation='vertical')
        gl=GridLayout(cols=4)

        self.lbl=Label(text='0',font_size=40,halign='right',text_size=(350-50,500*.4-50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7',on_press=self.add_number))
        gl.add_widget(Button(text='8',on_press=self.add_number))
        gl.add_widget(Button(text='9',on_press=self.add_number))
        gl.add_widget(Button(text='x',on_press=self.add_operation))

        gl.add_widget(Button(text='4',on_press=self.add_number))
        gl.add_widget(Button(text='5',on_press=self.add_number))
        gl.add_widget(Button(text='6',on_press=self.add_number))
        gl.add_widget(Button(text='-',on_press=self.add_operation))

        gl.add_widget(Button(text='1',on_press=self.add_number))
        gl.add_widget(Button(text='2',on_press=self.add_number))
        gl.add_widget(Button(text='3',on_press=self.add_number))
        gl.add_widget(Button(text='+',on_press=self.add_operation))

        gl.add_widget(Button(text='C',on_press=self.add_operation))
        gl.add_widget(Button(text='0',on_press=self.add_number))
        gl.add_widget(Button(text='.',on_press=self.add_number))
        gl.add_widget(Button(text='=',on_press=self.calc_rez))

        bl.add_widget(gl)
        return bl
    def add_number(self,instance):
        if self.form=='0':
            self.form=''
        self.form+=str(instance.text)
        self.update_label()

    def add_operation(self,instance):
        if str(instance.text)=='x':
             self.form+='*'
        elif str(instance.text).lower() == 'c':
             self.form = '0'
        else:
            self.form+=str(instance.text)
        self.update_label()
    def update_label(self):
        self.lbl.text=self.form
    def calc_rez(self,instance):
        self.lbl.text=str(eval(self.lbl.text))
        self.form='0'
if __name__=="__main__":
    MyApp().run()