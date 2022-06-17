from array import array
from tkinter import CENTER
from view.view import View
import PySimpleGUI as sg


class ViewRota(View):

    def __init__(self):
        super().__init__()

    def options(self, list: array):

        cards = []
        for item in list:
            info = [[sg.Text(item, font=('Arial', 12, 'bold'), background_color='#D9D9D9')],
                    [sg.Text('Entregas', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')],
                    [sg.Text('Motorista', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')]]
            buttons = [[sg.Button('Editar', key='edit', font=(
                        'Arial', 10, 'bold'), size=(10, 1)), sg.Button('Visualizar', key='edit', font=(
                            'Arial', 10, 'bold'), size=(10, 1))]]
            card = [[sg.Column(info), sg.Column(buttons)]]
            cards.append(
                [sg.Column(card, background_color='#D9D9D9', justification=CENTER, pad=(0, 5), )])

        layout = [[sg.Text('Rotas', font=('Arial', 20, 'bold'))],
                  [sg.Button('Criar nova rota', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                      'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [sg.Column(cards, scrollable=True,
                             vertical_scroll_only=True, expand_x=True, size=(None, 400))]

                  ]

        window = self.window(layout)

        while True:
            button, values = window.read()

            if button == 'search':
                new_values = []
                search = values['input']
                for object in list:
                    if search in object.nome.lower():
                        new_values.append(object)
                window['select'].update(new_values)
            else:
                break

        window.close()

        return button, values
