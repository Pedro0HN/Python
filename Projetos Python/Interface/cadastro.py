from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar login? ')],
    [sg.Button('Entrar')]
]
#janela

janela = sg.Window('Tela de login',layout)

#ler os eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if  eventos == 'Entrar':
        if valores['usuario'] == 'Pedro' and valores['senha'] == '123':
            print(f"Ola {valores['usuario']},seja bem vindo")