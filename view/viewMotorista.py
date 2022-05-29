
from turtle import width
import PySimpleGUI as sg


class ViewMotorista():

    def options(self):
        sg.theme('Dark Gray 3')
        sg.set_options(element_padding=(0, 0))

        tab1_layout = [[sg.T('This is inside tab 1')]]

        tab2_layout = [[sg.T('This is inside tab 2')],
                       [sg.In(key='in')]]

        layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('Tab 2', tab2_layout)]], tooltip='TIP2')],
                  [sg.Button('Read')]]

        window = sg.Window('My window with tabs', layout,
                           default_element_size=(12, 1))

        window.read()

# menu_def = [['Criar nova rota'],
#             ['Pesquisar'],
#             ['Visualizar finalizadas']]

# layout = [
#     [sg.Menu(menu_def, tearoff=False)],
#     [sg.Text("Windows-like program, Windows-like program")],
#     [sg.Output(size=(60, 20))]

# ]

# window = sg.Window("Motorista",
#                    layout)
# window.Read()
