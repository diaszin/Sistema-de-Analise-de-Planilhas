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
    dados = pd.read_excel(caminho_planilha)
    titulos_planilha = ["Todos"]
    for titulo in dados.columns:
        titulos_planilha.append(titulo)
    
    tab_layout_1 = [
        [sg.OptionMenu(titulos_planilha, titulos_planilha[0])]
    ]
    
    tabgroup_layout = [
        [sg.Tab("Dados por titulo", tab_layout_1)]
    ]
    
    
    layout = [
        [sg.Multiline(disabled=True, size=(80,30), key="-output-")],
        [sg.TabGroup(tabgroup_layout, size=(30,30))],
        [sg.Text("O que deseja fazer ?", justification="center")],
        [sg.Button("Visualizar Dados"), sg.Button("Ver Amostra do Dado")]
    ]
    
    janela = sg.Window("Tela Principal", layout)
    while True:
        event, values = janela.read()
        if event == None or sg.WIN_CLOSED:
            janela.close()
            exit()
        if event ==  "Visualizar Dados":
            if values[0] == "Todos" and values[1] == "Dados por titulo":
                janela['-output-'].update(dados.to_string())
            elif values[1] == "Dados por titulo":
                frase = f"{values[0]}\n"
                for chave, valor in dados[values[0]].items():
                    frase += f"Na linha {(chave+1)} = {valor}\n"    
                janela["-output-"].update(frase)
        elif event == "Ver Amostra do Dado":
                if values[0] == "Todos" and values[1] =="Dados por titulo":
                    janela['-output-'].update(dados.sample())
                elif values[1] == "Dados por titulo":
                    amostra_dados_valor = dados[values[0]].sample()
                    for chave, valor in amostra_dados_valor.items():
                        frase  = f"Amostra de Dados da Coluna: {values[0]}\nResultado: Linha {chave} - {valor}"
                    janela["-output-"].update(frase)
                    
                
        print(event, values)


def LoginGUI():
    from process.login import LoginProcess
    
    
    coluna_centralizada = [
        [sg.Text("Username"), sg.Input(size=(20,2), do_not_clear=False, focus=True)],
        [sg.Text("Password"), sg.Input(password_char="*", size=(20,2), do_not_clear=False)],
        [sg.OK("Entrar", size=(10,1), button_color="green"), sg.Cancel("Sair", size=(10,1), button_color="red")],
        [sg.Button("Cadastrar")]
    ]
    
    layout_login = [
        [sg.Column(coluna_centralizada, element_justification="c", vertical_alignment="c")]
    ]
    
    janela = sg.Window("Entrar", layout_login)
    while True:
        event, values = janela.read()
        if event == None or sg.WIN_CLOSED:
            exit(0)
        if event == "Entrar":
            logou = LoginProcess(event, values) #Verificando se o usuário estar cadastrado no banco de dados
            if(logou == True):
                janela.close()
                return True
            elif logou == False:
                janela.disappear()
                evento_popup = sg.Popup("Usuário ou senha incorretos, clique em OK para tentar novamente !")
                if evento_popup == "OK":
                    janela.reappear()
                else:
                    exit(0)
        elif event == "Cadastrar":
            janela.hide()
            CadastrarGUI()
            janela.UnHide()
                
def CadastrarGUI():
    
    from process.cadastrar import CadastrarProcess
    
    elemento = [
        [sg.Text("Username"), sg.Input(size=(20,2))],
        [sg.Text("Senha"), sg.Input(size=(20,2), password_char="*")],
        [sg.Text("Confirme sua senha"), sg.Input(size=(20,2), password_char="*")],
        [sg.OK("Cadastrar"), sg.Cancel("Voltar para o Login")]
    ]
    
    layout = [
        [sg.Column(elemento, element_justification="c", vertical_alignment="c")]
    ]
    
    janela = sg.Window("Cadastrar Usuário", layout)
    while True:
        event, values = janela.read()
        if event == None or sg.WIN_CLOSED or event == "Voltar para o Login":
            janela.close()
            break
        if event == "Cadastrar":
            USUARIO, SENHA, SENHA_CONFIRM = values[0], values[1], values[2]
            if SENHA != SENHA_CONFIRM:
                janela.disappear()
                event_popup = sg.Popup("Senha inseridas não são iguais !\nTente Novamente", "ERRO")
                if event_popup == "OK":
                    janela.reappear()
                if event_popup == None:
                    break
            else:
                retorno = CadastrarProcess(USUARIO, SENHA)
                if(retorno == True):
                    evento_popup = sg.Popup("Cadastrado com Sucesso !\nAperte em OK para continuar !")
                    
                else:
                    sg.Popup("Erro no Cadastro, Tente Novamente")
                             