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

from testPacker import e1


class AuthorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Это приложение разработал AI-создатель"))


class TaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_answer = []
        self.answers = []

        layout = BoxLayout(orientation='vertical')

        scroll_view = ScrollView()
        self.task_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.task_layout.bind(minimum_height=self.task_layout.setter('height'))
        scroll_view.add_widget(self.task_layout)

        layout.add_widget(scroll_view)
        self.add_widget(layout)

        for i in range(12):
            data = eval(f'ex_{i + 1}()')
            text = self.reformate_text(data['data'], i+1)
            weight_height = len(text.splitlines())

            for o in data['answer']:
                self.answers.append(o)

            task_box = BoxLayout(orientation='vertical', size_hint_y=None, pos_hint={"center_x": .5, "center_y": 1},
                                 height=100 + 25 * weight_height)

            task_nuber = Label(text=f'Задание {i + 1}', bold=40, color=(150 / 256, 160 / 256, 180 / 256))

            task_text = Label(text=text.splitlines()[0], color=(200 / 256, 195 / 256, 230 / 256),
                              pos_hint={"center_x": .5, "center_y": 1})
            if i+1 == 6:
                box_py = GridLayout(cols=2)
                box_py.add_widget(Label(text=text.splitlines()[1]))
                box_py.add_widget(Label(text=text.splitlines()[2]))

                task_box.add_widget(box_py)
            else:
                task_text = Label(text=text, color=(200 / 256, 195 / 256, 230 / 256),
                                  pos_hint={"center_x": .5, "center_y": 1})

            task_entry = TextInput(hint_text=f'Ответ на {i + 1}-oe задание', size_hint=(None, None), height=30,
                                   width=200, multiline=False, pos_hint={"center_x": .3, "center_y": 1})

            self.text_answer.append(task_entry)

            task_box.add_widget(task_nuber)
            task_box.add_widget(task_text)
            task_box.add_widget(task_entry)

            self.task_layout.add_widget(task_box)

            print(data['answer'])

        but_end = Button(text='Завершить тест', size_hint=(None, None), width=200, height=40,
                         on_press=self.answer, pos_hint={"center_x": .8, "center_y": 1})
        self.task_layout.add_widget(but_end)

    def reformate_text(self, text, number):
        inp = ''
        for elements in text:
            s = ''
            a = 0

            if type(elements) == dict:
                el = list(elements)
                l = []
                for i in range(len(el)):
                    ele = random.choice(el)
                    el.remove(ele)
                    l.append(ele)
                el = l

                if number == 2:
                    for i in range(len(el)):
                        inp += f'|  {el[i]} ==> {elements[el[i]]}  '
                    inp += '|\n'

                continue


            for el in str(elements):
                a += 1
                s += el
                if a == 80:
                    a = 0
                    pause = s.rfind(' ')
                    s = s[:pause:] + ' \n' + s[pause::]
            inp += s + ' \n'

        return inp

    def answer(self, *args):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text="Твой результат по прохождении теста"))
        an_1 = [str(i.text).lower() for i in self.text_answer]
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