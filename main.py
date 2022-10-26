from gui import StartGui, MainGUI, LoginGUI


if LoginGUI() == True:
    caminho = StartGui() # Iniciando uma interface para captar o caminho do documento excel
    MainGUI(caminho)