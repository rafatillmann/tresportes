from array import array
from tkinter import BOTTOM, CENTER, TOP
from view.view import View
import PySimpleGUI as sg


class ViewCarga(View):

    def __init__(self):
        super().__init__()

    def options(self, inicial_list: array):

        cards = self.cards(inicial_list)

        layout = [[sg.Text('Cargas', font=('Arial', 20, 'bold'))],
                  [sg.Button('Criar nova carga', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                      'Arial', 10, 'bold'))],
                  [sg.Input(size=(20, 5), key='input', expand_x=True)],
                  [sg.Column(cards, scrollable=True,
                             vertical_scroll_only=True, sbar_relief='solid', size=(500, 400), key='select')]

                  ]

        window = self.window(layout)

        while True:
            button, values = window.read()

            if button == 'search':
                new_values = []
                search = values['input']
                for object in inicial_list:
                    if search.lower() in f'Carga {object.id}'.lower():
                        new_values.append(object)

                window.close()
                layout = self.refresh_cards(new_values)
                window = self.window(layout)
            else:
                break

        window.close()

        return button, values

    def inicial(self):
        info = [
            [sg.Text('Cadastro', font=('Arial', 20, 'bold'))],
        ]

        layoutLoadForm = [
            [sg.Text('Informações da carga', size=(30, 1))],
            [sg.Text('Descrição', size=(20, 1))],
            [sg.InputText(key='descricao')],
            [sg.Text('Carga', size=(20, 1))],
            [sg.InputText(key='categoria')],
            [sg.Text('Peso', size=(20, 1))],
            [sg.InputText(key='peso')],
            [sg.Text('Largura', size=(20, 1))],
            [sg.InputText(key='largura')],
            [sg.Text('Altura', size=(20, 1))],
            [sg.InputText(key='altura')],
            [sg.Text('Comprimento', size=(20, 1))],
            [sg.InputText(key='comprimento')],
        ]

        layoutReceiverForm = [
            [sg.Text('Informações do destinatário', size=(30, 1))],
            [sg.Text('CPF/CNPJ', size=(20, 1))],
            [sg.InputText(key='cpf')],
            [sg.Text('Nome', size=(20, 1))],
            [sg.InputText(key='nome')],
            [sg.Text('Endereço', size=(20, 1))],
            [sg.InputText(key='endereco')],
        ]

        layout = [[sg.Column(info)], [sg.Column(layoutLoadForm), sg.Column(layoutReceiverForm)], [self.white_button('Descartar', 'cancel'),
                                      self.button('Concluir', 'save', disableb=False)]]

        window = self.window(layout)

        button, values = window.read()

        window.close()

        return button, values

    def edit(self, route):
        road = self.road()
        loads = self.loads([1, 2, 3, 4])
        layout = [[sg.Text('Revisão', font=('Arial', 20, 'bold'))],
                  [sg.Column(road, vertical_alignment=TOP),
                   sg.Column(loads, vertical_alignment=TOP)],
                  [sg.Sizer(v_pixels=80)],
                  [self.white_button('Descartar', 'cancel'),
                   self.button('Concluir', 'save')]
                  ]

        window = self.window(layout)

        button, values = window.read()

        window.close()

        return button, values

    def select_load(self, list):
        layout = [[sg.Text('Selecione as cargas do percurso', font=('Arial', 20, 'bold'))],
                  [self.multiple_list(list)],
                  [self.white_button('Voltar', 'back'), self.button(
                      'Selecionar', 'sel')]
                  ]

        window = self.window(layout)

        button, values = window.read()

        window.close()

        return button, values

    def finish(self, inicial_list: array):
        cards = self.cards(inicial_list, finish=True)

        layout = [[sg.Text('Cargas', font=('Arial', 20, 'bold'))],
                  [sg.Button('Criar nova carga', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                      'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
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
                    if search.lower() in f'Carga {object.id}'.lower():
                        new_values.append(object)

                window.close()
                layout = self.refresh_cards(new_values, finish=True)
                window = self.window(layout)
            else:
                break

        window.close()

        return button, values

    # ---------- components ------------

    def cards(self, list, finish=False):
        cards = []
        for item in list:
            info = [[sg.Text(f'Carga {item.id}', font=('Arial', 12, 'bold'), background_color='#D9D9D9')],
                    [sg.Text('Entregas', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')],
                    [sg.Text('Nenhum motorista alocado', font=('Arial', 10, 'bold'),
                             background_color='#D9D9D9')]]
            buttons = [[self.button('Editar', f'edit:{item.id}') if not finish else None,
                        self.button('Visualizar', f'view:{item.id}')]]

            card = [[sg.Column(info, background_color='#D9D9D9', pad=((0, 100), (0, 0))), sg.Column(
                buttons, vertical_alignment=BOTTOM, background_color='#D9D9D9')]]

            cards.append(
                [sg.Column(card, background_color='#D9D9D9', justification=CENTER, pad=((0, 5), (0, 10)), )])

        return cards

    def refresh_cards(self, list, finish=False):

        cards = self.cards(list, finish)

        return [[sg.Text('Cargas', font=('Arial', 20, 'bold'))],
                [sg.Button('Criar nova carga', key='insert', font=('Arial', 10, 'bold')), sg.Button('Pesquisar', key='search', font=(
                    'Arial', 10, 'bold')), sg.Button('Visualizar finalizadas', key='finish', font=('Arial', 10, 'bold'))],
                [sg.Input(size=(20, 5), key='input', expand_x=True)],
                [sg.Column(cards, scrollable=True,
                           vertical_scroll_only=True, size=(None, 400), key='select')]

                ]

    def road(self):
        info = [[sg.Sizer(500)],
                [sg.Text('dfdfdfdfdfd', font=('Arial', 10, 'bold'),
                         background_color='#D9D9D9')],
                [sg.Image(source='./assets/points.png',
                          background_color='#D9D9D9')],
                [sg.Text('fsfsfsdfsfsdfs', font=('Arial', 10, 'bold'),
                         background_color='#D9D9D9')]]

        card = [
            [sg.Text('Percurso', font=('Arial', 14, 'bold'))], [
                sg.Column(info, background_color='#D9D9D9', element_justification=CENTER)]]

        return card

    def loads(self, list):
        cards = []
        for item in list:
            info = [[sg.Sizer(500)],
                    [sg.Text(f'kjddjksdj', font=('Arial', 10, 'bold'), background_color='#D9D9D9'), sg.Text(
                        f'kjddkskdsksskskjksdj', font=('Arial', 10, 'bold'), background_color='#D9D9D9')],
                    ]

            cards.append(
                [sg.Column(info, background_color='#D9D9D9')])

        loads = [[sg.Text('Cargas', font=('Arial', 14, 'bold'))],
                 [sg.Column(cards, scrollable=True, vertical_scroll_only=True,
                            sbar_arrow_width=5, sbar_width=5, sbar_relief='solid')],
                 [self.white_button('Editar', 'edit')]]

        return loads
