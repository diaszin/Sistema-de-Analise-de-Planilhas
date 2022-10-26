import mysql.connector


def CadastrarProcess(username, senha):
    
    __meudb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password=""
    )
    
    try:
        __cursor = __meudb.cursor()
        __cursor.execute("USE usuarios")
        __cursor.execute("INSERT INTO users (nome,senha, ativo) VALUES (%s, %s, %s)", (username, senha, True))
    except:
        return False
    else:
        __meudb.commit()
        return True
    
    
    
print(f"Módulo {__name__} carregado")
