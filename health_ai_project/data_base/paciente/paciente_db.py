from data_base.paciente.paciente_ob import DadosPaciente
import sqlite3
import pandas as pd

# ('132435465', 31, 1, 1, 11.2, 0, 0)
# ('243546576', 44, 0, 1, 1.2, None, 1)
# ('354657687', 75, 1, 0, 2.2, None, None)
# ('465768798', 63, 0, 1, 9.1, 2, 3)
# ('576879809', 22, 1, 0, 7.0, 4, None)
# ('687980921', 37, 0, 1, 6.4, 3, 5)
# ('775566334', 55, 1, 1, 2.4, 1, 2)

class PacienteDB():

    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.criar_base()
        self.criar_tabela_paciente()
        # self.inserir_dados_tabela_paciente()
        # self.listar_todos()
   
    def criar_base(self):
        self.connection = sqlite3.connect('test_database') 
        self.cursor = self.connection.cursor()

    def criar_tabela_paciente(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS DADOS_PACIENTE (
                    PRONTUARIO VARCHAR(40) PRIMARY KEY,
                    IDADE INT NOT NULL,
                    HISTORICO_FAMILIAR TINYINT(1) NOT NULL,
                    NODULO_PALPAVEL TINYINT(1) NOT NULL,
                    TAMANHO_NODULO FLOAT NOT NULL, 
                    BIRADS_USG INT,
                    BIRADS_MAMOGRAFIA INT
                    );
            ''')
        
            self.connection.commit()
        except:
            print("CREATE TABLE EXCEPTION")
        
    def inserir_dados_tabela_paciente(self):
        try:
            self.cursor.execute('''
            INSERT INTO DADOS_PACIENTE VALUES 
                ("775566334", 55, 1, 1, 2.4, 1, 2)
            ''')
         
            self.connection.commit()
        except:
            print("INSERT EXCEPTION")

    def listar_todos(self):
        self.cursor.execute(f'''
          SELECT * FROM DADOS_PACIENTE 
          ''')

        itens = self.cursor.fetchall()

        for item in itens:
            print(item)

    def obter_dados_paciente(self, prontuario: int):
        self.cursor.execute(f'''
          SELECT * FROM DADOS_PACIENTE WHERE PRONTUARIO == {prontuario} LIMIT 1
          ''')

        itens = self.cursor.fetchall()

        return DadosPaciente(itens[0][0], itens[0][1], itens[0][2], itens[0][3], itens[0][4], itens[0][5], itens[0][6])