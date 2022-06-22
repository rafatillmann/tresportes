from array import array
from tkinter import BOTTOM, CENTER
from view.view import View
import PySimpleGUI as sg


class ViewRota(View):

    def __init__(self):
        super().__init__()

    def options(self, inicial_list: array):

        cards = self.cards(inicial_list)

        layout = [[sg.Text('Rotas', font=('Arial', 20, 'bold'))],
                  [sg.Button('Criar nova rota', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                      'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [sg.Column(cards, scrollable=True,
                             vertical_scroll_only=True, size=(None, 400), key='select')]

                  ]

        window = self.window(layout)

        while True:
            button, values = window.read()

            if button == 'search':
                new_values = []
                search = values['input']
                for object in inicial_list:
                    if search.lower() in f'Rota {object.id}'.lower():
                        new_values.append(object)

                window.close()
                layout = self.refresh_cards(new_values)
                window = self.window(layout)
            else:
                break

        window.close()

        return button, values

    def display(self):
        layout = [[sg.Text('Criar nova rota', font=('Arial', 20, 'bold'))],
                  [sg.Text('Cargas', font=('Arial', 14, 'bold'))],
                  [sg.Text('Nenhuma carga adicionada',
                           font=('Arial', 10, 'bold')), self.button('Adicionar', 'add')],
                  [self.white_button('Descartar', 'cancel'),
                   self.button('Concluir', 'save')]
                  ]

        window = self.window(layout)

        button, values = window.read()

        if button == 'add':
            values['loads'] = self.select_load()

        window.close()

        return button, values

    def review(self):
        pass

    def finish(self):
        pass

    def select_load(self):
        layout = [[sg.Text('Selecione as cargas do percurso', font=('Arial', 20, 'bold'))],
                  [self.multiple_list([1, 2, 3, 4])],
                  [self.white_button('Voltar', 'back'), self.button(
                      'Selecionar', 'sel')]
                  ]

        window = self.window(layout)

        button, values = window.read()

        window.close()

        return values

    def cards(self, list):
        cards = []
        for item in list:
            info = [[sg.Text(f'Rota {item.id}', font=('Arial', 12, 'bold'), background_color='#D9D9D9')],
                    [sg.Text('Entregas', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')],
                    [sg.Text('Motorista', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')]]
            buttons = [[self.button('Editar', f'edit:{item.id}'),
                        self.button('Visualizar', f'view:{item.id}')]]

            card = [[sg.Column(info, background_color='#D9D9D9', pad=((0, 100), (0, 0))), sg.Column(
                buttons, vertical_alignment=BOTTOM, background_color='#D9D9D9')]]

            cards.append(
                [sg.Column(card, background_color='#D9D9D9', justification=CENTER, pad=((0, 5), (0, 10)), )])

        return cards

    def refresh_cards(self, list):

        cards = self.cards(list)

        return [[sg.Text('Rotas', font=('Arial', 20, 'bold'))],
                [sg.Button('Criar nova rota', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                    'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
                [sg.Input(size=(20, 5), key='input', expand_x=True)],
                [sg.Column(cards, scrollable=True,
                           vertical_scroll_only=True, size=(None, 400), key='select')]

                ]
