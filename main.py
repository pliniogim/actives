import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import db_actives as dba


class MyApp(App):
    def build(self):
        # db connect
        db = dba.ActivesDatabase()
        db.database_init()
        db.create_actives(act_id=1, name="A001")
        db.create_actives(act_id=2, name="A003")
        db.update_actives(act_id=2, new_name="A002")
        db.create_actives(act_id=3, name="A003")
        db.create_actives(act_id=4, name="A004a")
        layout = BoxLayout(orientation='vertical')
        input_name = TextInput()
        button_create = Button(text='create')
        layout.add_widget(input_name)
        layout.add_widget(button_create)
        db.delete_actives(act_id=4)
        return layout


if __name__ == '__main__':
    MyApp().run()
