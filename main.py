from kivy.app import App
from kivmob import KivMob,TestIds
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
from kivymd.uix.button import MDRectangleFlatIconButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.


KV="""

<SettingsScreen>:
    MDFloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
       
        MDLabel:
            id:l1
            text:"00:00:00"
            pos_hint:{'center_x': 0.5, 'center_y': 0.9}
            halign:"center"
            theme_text_color:"Custom"
            text_color:"#FF00FF"
            bold:True
            font_size:150

        

        MDIconButton:
            id:play
            text:"Play"
            icon:"play"
            pos_hint:{'center_x': 0.4, 'center_y': 0.2}
            icon_color:(0, 0, 0 ,1)
            text_color: (0, 0, 0 ,1)
            md_bg_color:"#9933CC"
            opposite_colors:True
            on_release:root.startbt(*args)
        


       
        MDIconButton:
            id:exit
            text:"Exit"
            icon:"logout"
            pos_hint:{'center_x': 0.6, 'center_y': 0.2}
            icon_color:(0, 0, 0 ,1)
            text_color: (0, 0, 0 ,1)
            md_bg_color:"#9933CC"
            opposite_colors:True
            on_release:root.exitbt(*args)

            
            
        
            
         
"""

# Declare both screens
class MenuScreen(Screen):
    pass




    def goout(self,*args):
        exit()
class SettingsScreen(Screen):
    startflag = 0







    def startbt(self, instance):
        if self.startflag==0:
            self.ids.l1.disabled = True
            self.startflag = 1
        else:
            self.ids.l1.disabled = False
            self.startflag = 0








    def exitbt(self, instance):
        exit()
    #


class TestApp(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)







    def build(self):
        # Create the screen manager
        self.theme_cls.material_style = "M3"
        self.title = "Trendlogic24"


        global sm

        sm = ScreenManager()
        # sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))


        return sm

    def on_start(self):
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_once(self.login, 0)



    def login(self, *args):

           sm.current = "settings"
           # sm.current = "menu"






if __name__ == '__main__':
    TestApp().run()