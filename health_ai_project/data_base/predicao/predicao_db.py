from data_base.predicao.predicao_ob import Predicao
import sqlite3

class PredicaoDB():

    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.conectar()
        self.criar_tabela_predicao()
        self.limpar_tabela()
        self.inserir_dados_tabela_predicao()
        # self.listar_todos()
   
    def conectar(self):
        self.connection = sqlite3.connect('test_database') 
        self.cursor = self.connection.cursor()

    def criar_tabela_predicao(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS PREDICAO (
                    ID_PREDICAO INT NOT NULL PRIMARY KEY,
                    PRONTUARIO_FK VARCHAR(40),
                    PREDICAO TINYINT(1) NOT NULL,
                    PORCENTAGEM_BENIGNO FLOAT NOT NULL,
                    PESO_IDADE FLOAT NOT NULL,
                    PESO_TAMANHO_NODULO FLOAT NOT NULL, 
                    PESO_HISTORICO_FAMILIAR FLOAT NOT NULL,
                    PESO_NODULO_PALPAVEL FLOAT NOT NULL,
                    PESO_BIRADS_USG FLOAT,
                    PESO_BIRADS_MAMOGRAFIA FLOAT,
                    FOREIGN KEY(PRONTUARIO_FK) REFERENCES DADOS_PACIENTE(PRONTUARIO)
                    );
            ''')
        
            self.connection.commit()
        except:
            print("CREATE TABLE EXCEPTION")
        
    def inserir_dados_tabela_predicao(self):
        try:
            self.cursor.execute('''
            INSERT INTO PREDICAO VALUES 
                (1, "132435465", 1, 0.53, 0.05, 0.10, -0.19, 0.03, 0.40, 0.26),
                (2, "243546576", 0, 98.78, -0.05, -0.09, -0.17, -0.03, -0.16, -0.15),
                (3, "354657687", 1, 5.30, 0.04, 0.10, 0.19, 0.02, 0.38, -0.16),
                (4, "465768798", 0, 86.34, -0.05, 0.10, 0.18, 0.03, -0.17, -0.15)
            ''')
         
            self.connection.commit()
        except:
            print("INSERT EXCEPTION")

    def listar_todos(self):
        self.cursor.execute(f'''
          SELECT * FROM PREDICAO 
          ''')

        itens = self.cursor.fetchall()

        for item in itens:
            print(item)

    def obter_predicao_paciente(self, prontuario: int):
        self.cursor.execute(f'''
          SELECT  ID_PREDICAO, 
                  PRONTUARIO_FK,
                  PREDICAO,
                  PORCENTAGEM_BENIGNO,        
                  PESO_IDADE,
                  PESO_TAMANHO_NODULO,
                  PESO_HISTORICO_FAMILIAR,
                  PESO_NODULO_PALPAVEL,
                  PESO_BIRADS_USG,
                  PESO_BIRADS_MAMOGRAFIA                            
             FROM 
                  PREDICAO 
               WHERE 
                  PRONTUARIO_FK == {prontuario} 
             ORDER BY 
                  ID_PREDICAO 
             DESC LIMIT 1
          ''')

        itens = self.cursor.fetchall()
        return Predicao(itens[0][1], itens[0][2], itens[0][3], itens[0][4], itens[0][5], itens[0][6], itens[0][7], itens[0][8], itens[0][9])
    
    def limpar_tabela(self):
        self.cursor.execute(f'''
          DELETE FROM PREDICAO
          ''')