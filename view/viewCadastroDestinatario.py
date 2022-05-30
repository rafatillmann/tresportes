from array import array
from tkinter import CENTER
import PySimpleGUI as sg
from view.view import View
from model.destinatario import Destinatario

class ViewDestinatario(View):
    
    def __init__(self):
        super().__init__()
        
    def display(self, destinatario: Destinatario = None):
    
        if destinatario:
            
            layoutForm = [[sg.Text("Cadastro", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(destinatario.nome, key='nome')],
                          [sg.Text('CPF', size=(15, 1)), sg.InputText(destinatario.cpf, key='cpf')],
                          [sg.Text('Senha', size=(15, 1)), sg.InputText(destinatario.senha, key='senha')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.InputText(destinatario.email, key='email')],
                          [sg.Text('Endereço', size=(15, 1)), sg.InputText(destinatario.endereco, key='endereco')],
                          [sg.Text('Complemento', size=(15, 1)), sg.InputText(destinatario.complemento, key='complemento')],
                          [sg.Text('Telefone', size=(15, 1)), sg.InputText(destinatario.telefone, key='telefone')],
                          ]
        
        else:
            layoutForm = [[sg.Text("Cadastro", font=('Arial', 14, 'bold'))],
                          [sg.Text('Nome', size=(15, 1)), sg.InputText(key='nome')],
                          [sg.Text('CPF', size=(15, 1)), sg.InputText(key='cpf')],
                          [sg.Text('Senha', size=(15, 1)), sg.InputText(key='senha')],
                          [sg.Text('E-mail', size=(15, 1)),
                           sg.InputText(key='email')],
                          [sg.Text('Endereço', size=(15, 1)), sg.InputText(key='endereco')],
                          [sg.Text('Complemento', size=(15, 1)), sg.InputText(key='complemento')],
                          [sg.Text('Telefone', size=(15, 1)), sg.InputText(key='telefone')],
                          ]
        
        layout = [layoutForm, [sg.Button('Cadastrar', key='save')]]
        
        window = sg.Window('Destinatário', layout,
                           default_element_size=(30, 1), margins=(50, 10), element_justification=CENTER)
        
        button, values = window.read()
        
        window.close()
        
        return button, values
