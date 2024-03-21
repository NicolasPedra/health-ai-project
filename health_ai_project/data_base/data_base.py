import mysql.connector
from mysql.connector import Error
from static.script.tela_consulta import DadosPaciente

def criar_conexao(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def criar_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def executar_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def ler_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def criar_tabela_paciente(connection):
    table_query = """
            CREATE TABLE DADOS_PACIENTE (
            PRONTUARIO INT PRIMARY KEY,
            IDADE INT NOT NULL,
            HISTORICO_FAMILIAR TINYINT(1) NOT NULL,
            NODULO_PALPAVEL TINYINT(1) NOT NULL,
            TAMANHO_NODULO FLOAT NOT NULL, 
            BIRADS_USG INT,
            BIRADS_MAMOGRAFIA INT
            );
    """
    executar_query(connection, table_query)
    
def inserir_dados_tabela_paciente(connection):
    insert_query = """
        INSERT INTO DADOS_PACIENTE VALUES
        (132435465, 31, 1, 1, 11.2, 0, 0),
        (243546576, 44,  0,  1, 1.2, NULL, 1), 
        (354657687, 75, 1,  0, 2.2, NULL, NULL),
        (465768798, 63,  0, 1, 9.1, 2, 3),
        (576879809, 22, 1, 0, 7, 4, NULL),
        (687980921, 37, 0, 1, 6.4, 3, 5);
        """
    
    executar_query(connection, insert_query)

def criar_base():
    connection = criar_conexao("localhost", "root", "1234")
    criar_database(connection, "CREATE DATABASE HEALTH_AI")

    criar_tabela_paciente(connection)
    inserir_dados_tabela_paciente(connection)

def obter_dados_paciente(prontuario: int):
    connection = criar_conexao("localhost", "root", "1234")

    results = ler_query(connection, f"SELECT * FROM DADOS_PACIENTE WHERE PRONTUARIO == {prontuario} LIMIT 1")

    return DadosPaciente(results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5])