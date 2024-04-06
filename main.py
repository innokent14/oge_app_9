import random
from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from nambers.task_1 import ex_1
from nambers.task_2 import ex_2
from nambers.task_3 import ex_3
from nambers.task_4 import ex_4
from nambers.task_5 import ex_5
from nambers.task_6 import ex_6
from nambers.task_7 import ex_7
from nambers.task_8 import ex_8
from nambers.task_9 import ex_9
from nambers.task_10 import ex_10
from nambers.task_11 import ex_11
from nambers.task_12 import ex_12


class AuthorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Это приложение разработал AI-создатель"))


class TaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_answer = []
        self.answers = []

        self.height_text = 20
        self.spacing_box = 20

        layout = BoxLayout(orientation='vertical')

        scroll_view = ScrollView()
        self.task_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=100)
        self.task_layout.bind(minimum_height=self.task_layout.setter('height'))
        scroll_view.add_widget(self.task_layout)

        layout.add_widget(scroll_view)
        self.add_widget(layout)

        for i in range(12):
            task_box = BoxLayout(orientation='vertical', size_hint_y=None, pos_hint={"center_x": .5, "center_y": 1},
                                 spacing=self.spacing_box)
            task_box.add_widget(Label(text=f'Задание {i}', bold=10, color=(150 / 256, 160 / 256, 180 / 256)))
            data = eval(f'ex_{i + 1}()')
            self.answers.append(data['answer'])
            widget = eval(f'self.ex_{1}(task_box, data["data"])')
            entry = TextInput(hint_text=f'Ответ на {i + 1}-oe задание', size_hint=(None, None), height=30,
                              width=200, multiline=False, pos_hint={"center_x": .3, "center_y": 1})
            widget.add_widget(entry)
            self.entry_answer.append(entry)

            self.task_layout.add_widget(widget)
        self.task_layout.add_widget(Button(text='Завершить тест', size_hint=(None, None), width=200, height=40,
                                           on_press=self.answer, pos_hint={"center_x": .8, "center_y": 1}))

    def ex_1(self, box: BoxLayout, text_):
        text = text_format(text_)

        text_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=0,
                                height=len(text) * self.height_text)

        for i in text:
            if type(i) == dict:
                table = self.make_dict(i)
                box.add_widget(table)
                continue

            task_text = Label(text=i, color=(200 / 256, 195 / 256, 230 / 256),
                              pos_hint={"center_x": .5, "center_y": 1}, size_hint_y=None, height=self.height_text)
            text_layout.add_widget(task_text)
        box.add_widget(text_layout)

        box.height = len(text) * self.height_text + 50 + self.spacing_box * len(box.children)

        return box

    def answer(self, *args):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text="Твой результат по прохождении теста"))
        an_1 = [str(i.text).lower() for i in self.entry_answer]
        an_2 = [str(i).lower() for i in self.answers]
        score = 0

        for i in range(12):
            lay = BoxLayout(orientation='horizontal')

            color = (0, 1, 0) if str(an_1[i]) == str(an_2[i]) else (1, 0, 0)
            color = (136 / 256, 89 / 256, 240 / 256) if str(an_1[i]) == '' else color

            score = score + 1 if an_1[i] == an_2[i] else score

            lay.add_widget(Label(text=str(an_1[i] if an_1[i] != '' else 'Нет ответа'), color=color))
            lay.add_widget(Label(text=str(an_2[i]), color=color))
            layout.add_widget(lay)
        layout.add_widget(Label(text=f'ты набрал {score}\\12'))

        self.clear_widgets()
        self.add_widget(layout)

    def make_dict(self, data, orientation=''):
        list_label = list(data)

        cols = len(list_label)*2-1

        print(str(data[list_label[0]]))

        map_table = []

        table = GridLayout(cols=cols, size_hint=(None, None), width=200, height=80,
                           pos_hint={"center_x": .5, "center_y": 1})

        for i in list_label:
            table.add_widget(Label(text=i))
            if i != list_label[-1]:
                table.add_widget(Label(text='|\n|'))

        for i in range(cols):
            table.add_widget(Label(text='--------------------------'))

        for i in list_label:

            if type(data[list_label[0]]) == dict:
                l = len(list(data[list_label[0]]))
                continue

            table.add_widget(Label(text=str(data[i])))
            if i != list_label[-1]:
                table.add_widget(Label(text='|\n|'))

        return table


def text_format(text):
    out = []
    for elements in text:
        s = ''
        a = 0

        if type(elements) == dict:
            out.append(elements)
            continue

        for el in str(elements):
            a += 1
            s += el

            if a == 80:
                a = 0
                pause = s.rfind(' ')
                s = s[:pause:] + ' \n' + s[pause::]

        for ss in s.splitlines():
            out.append(ss)

    return out


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Кнопка для перехода на страницу об авторе
        author_button = Button(text="Об авторе", on_press=self.go_to_author)
        layout.add_widget(author_button)

        # Кнопка для перехода на страницу с заданиями
        task_button = Button(text="Вариант", on_press=self.go_to_tasks)
        layout.add_widget(task_button)

        self.add_widget(layout)

    def go_to_author(self, *args):
        self.manager.current = 'author'

    def go_to_tasks(self, *args):
        self.manager.current = 'task'


class TestApp(App):
    def build(self):
        Window.clearcolor = (36 / 256, 36 / 256, 36 / 256)
        # Создаем менеджер экранов
        sm = ScreenManager()

        # Добавляем экраны в менеджер
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AuthorScreen(name='author'))
        sm.add_widget(TaskScreen(name='task'))

        return sm


if __name__ == '__main__':
    TestApp().run()
