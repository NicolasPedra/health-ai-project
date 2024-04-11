from data_base.paciente.paciente_ob import DadosPaciente
import sqlite3

class PacienteDB():

    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.conectar()
        self.criar_tabela_paciente()
        # self.limpar_tabela()
        # self.inserir_dados_tabela_paciente()
        # self.listar_todos()
   
    def conectar(self):
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
                ("132435465", 53, 0, 1, 24, 5,  5),
                ("243546576", 48, 0, 0, 13, 41, 4),
                ("354657687", 50, 1, 1, 80, 43, 4),
                ("465768798", 43, 1, 1, 33, 41, 4)
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
          SELECT  PRONTUARIO, 
                  IDADE,
                  HISTORICO_FAMILIAR,
                  NODULO_PALPAVEL,
                  TAMANHO_NODULO,
                  BIRADS_USG,
                  BIRADS_MAMOGRAFIA                            
             FROM 
                  DADOS_PACIENTE 
               WHERE 
                  PRONTUARIO == {prontuario} 
               LIMIT 1
          ''') 
        
        itens = self.cursor.fetchall()

        return DadosPaciente(itens[0][0], itens[0][1], itens[0][2], itens[0][3], itens[0][4], itens[0][5], itens[0][6])
    
    def limpar_tabela(self):
        self.cursor.execute(f'''
          DELETE FROM DADOS_PACIENTE
          ''')