import PySimpleGUI as sg
import pandas as pd

def StartGui():
    layout = [
        [sg.Text("Insira o seu arquivo")],
        [sg.Input(readonly=True), sg.FileBrowse(file_types=(("Excel Document", "*.xlsx*"),))],
        [sg.Ok("Iniciar"), sg.Cancel("Sair")]
    ]

    janela = sg.Window("Insira sua planilha", layout)
    event,values = janela.read()
    
    caminho_pasta = values[0]

    if event == "Iniciar":
        janela.close()
        return caminho_pasta
    if event == None or sg.WIN_CLOSED or event == "Sair":
            exit()


def MainGUI(caminho_planilha: str):
    
    layout = [
        [sg.Output((90,30))],
        [sg.Text("O que deseja fazer ?", justification="center")],
        [sg.Button("Visualizar Dados"), sg.Button("Ver Amostra do Dado")]
    ]
    
    dados = pd.read_excel(caminho_planilha)
    janela = sg.Window("Tela Principal", layout)
    while True:
        event, values = janela.read()
        if event == None or sg.WIN_CLOSED:
            janela.close()
            exit()
        if event ==  "Visualizar Dados":
            print("-"*20)
            
            print("-"*10+" Planilha Total "+"-"*10)
            print(dados)
        elif event == "Ver Amostra do Dado":
            print("-"*20)
            print("-"*10+" Amostra de Dados "+"-"*10)
            print(dados.sample())