import mysql.connector


def LoginProcess(event, values):
    EVENT, VALUES = event, values
    
    USUARIO, SENHA = VALUES[0], VALUES[1]
    __meudb = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password=""
    )
    
    __cursor = __meudb.cursor()
    __cursor.execute("USE usuarios")
    __cursor.execute("SELECT * FROM users")
    
    if EVENT == "Entrar":  
        __resultado = __cursor.fetchall()
        for item in __resultado:
            if item[0] == USUARIO and item[1] == SENHA:
                return True
        
        return False
    elif EVENT == None or "Sair": 
        exit(0)
    
    
    
print(f"Módulo {__name__} carregado")