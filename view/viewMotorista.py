from array import array
from pickle import TRUE
from tkinter import BOTTOM, CENTER, TOP
from view.view import View
import PySimpleGUI as sg


class ViewMotorista(View):
    def __init__(self):
        super().__init__()

    def options(self, inicial_list: array):

        cards = self.cards(inicial_list)

        layout = [[sg.Text('Rotas', font=('Arial', 20, 'bold'))],
                  [sg.Button('Pesquisar', key='search', font=(
                      'Arial', 10, 'bold'), border_width=0), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'), border_width=0)],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [sg.Column(cards, scrollable=True,
                             vertical_scroll_only=True, sbar_relief='solid', size=(None, 400), key='select')]

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

    def view(self, route, roads, loads):
        road = self.road(roads)
        loads = self.loads(loads, view=True)
        layout = [[sg.Text(f'Rota {route.id}', font=('Arial', 20, 'bold'))],
                  [sg.Column(road, vertical_alignment=TOP),
                   sg.Column(loads, vertical_alignment=TOP)],
                  [sg.Sizer(v_pixels=80)],
                  [self.button('Voltar', 'back')]
                  ]

        window = self.window(layout)

        button, values = window.read()

        window.close()

        return button, values

    # Components

    # ---------- components ------------

    def cards(self, list, finish=False):
        cards = []
        for item in list:
            info = [[sg.Text(f'Rota {item.id}', font=(
                'Arial', 12, 'bold'), background_color='#D9D9D9')]]

            buttons = [[self.button('Visualizar', f'view:{item.id}')]]

            card = [[sg.Column(info, background_color='#D9D9D9', pad=((0, 100), (0, 0))), sg.Column(
                buttons, vertical_alignment=BOTTOM, background_color='#D9D9D9')]]

            cards.append(
                [sg.Column(card, background_color='#D9D9D9', justification=CENTER, pad=((0, 5), (0, 10)), )])

        return cards

    def refresh_cards(self, list, finish=False):

        cards = self.cards(list, finish)

        return [[sg.Text('Rotas', font=('Arial', 20, 'bold'))],
                [sg.Button('Pesquisar', key='search', font=(
                    'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
                [sg.Input(size=(20, 5), key='input', expand_x=True)],
                [sg.Column(cards, scrollable=True,
                           vertical_scroll_only=True, size=(None, 400), key='select')]

                ]

    def road(self, roads):
        if roads:
            road = roads[0]
            info = [[sg.Sizer(500)],
                    [sg.Text(road.pontoA.endereco, font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')],
                    [sg.Image(source='./assets/points.png',
                              background_color='#D9D9D9')],
                    [sg.Text(road.pontoB.endereco, font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')]]

            card = [
                [sg.Text('Percurso', font=('Arial', 14, 'bold'))], [
                    sg.Column(info, background_color='#D9D9D9', element_justification=CENTER)]]

            return card
        else:
            info = [[sg.Sizer(500)],
                    [sg.Text('Nenhum percuso em andamento, rota finalizada', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9'), sg.Sizer(v_pixels=100)]]

            card = [
                [sg.Text('Percurso', font=('Arial', 14, 'bold'))], [
                    sg.Column(info, background_color='#D9D9D9', element_justification=CENTER)]]

            return card

    def loads(self, list, view=True):
        cards = []
        for item in list:
            info = [[sg.Sizer(500)],
                    [sg.Text(item, font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')],
                    ]

            cards.append(
                [sg.Column(info, background_color='#D9D9D9')])

        loads = [[sg.Text('Cargas', font=('Arial', 14, 'bold'))],
                 [sg.Column(cards, scrollable=True, vertical_scroll_only=True,
                            sbar_arrow_width=5, sbar_width=5, sbar_relief='solid', size=(None, 100))],
                 [self.white_button('Editar', 'edit') if not view else sg.Text('')]]

        return loads
