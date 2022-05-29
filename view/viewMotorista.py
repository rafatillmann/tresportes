
from array import array
from turtle import width
from xml.dom.pulldom import default_bufsize
import PySimpleGUI as sg

sg.theme('System Default 1')
sg.set_options(element_padding=(0, 0))


class ViewMotorista():

    def options(self, list: array):

        layout = [[sg.Button('Cadastrar motoristas', key='insert'), sg.Button('Pesquisar'), sg.Button('Motoristas excluídos')],
                  [sg.Table(list, ['Motoristas'],
                            expand_x=True, expand_y=True,
                            justification="center",
                            auto_size_columns=True,
                            num_rows=len(list))]]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(12, 1))

        button, values = window.read()
        window.close()

        return button

    def insert(self):

        layoutForm = [[sg.Text("Informações do motorista", font=('Arial', 14, 'bold'))],
                      [sg.Text('Nome', size=(15, 1)), sg.InputText(
                          key='name')],
                      [sg.Text('CPF', size=(15, 1)), sg.InputText(
                          key='name')],
                      [sg.Text('E-mail', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text('Carga horária', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text("Informações do veículo",
                               font=('Arial', 14, 'bold'))],
                      [sg.Text('Tipo', size=(15, 1)), sg.InputText(
                          key='name')],
                      [sg.Text('Marca', size=(15, 1)), sg.InputText(
                          key='name')],
                      [sg.Text('Modelo', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text('Placa', size=(15, 1)), sg.InputText(
                          key='name')],
                      [sg.Text('Capacidade', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text('Larg. Máx.', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text('Comp. Máx.', size=(15, 1)),
                       sg.InputText(key='name')],
                      [sg.Text('Atura Máx.', size=(15, 1)),
                       sg.InputText(key='name')]
                      ]
        layout = [layoutForm, [sg.Button('Excluir'), sg.Button(
            'Cancelar'), sg.Button('Cadastrar')]]

        window = sg.Window('Motoristas', layout,
                           default_element_size=(30, 1))

        window.read()
        window.close()

    def update(self):
        pass
