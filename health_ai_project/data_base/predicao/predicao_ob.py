
import json

class Predicao:
    prontuario: str
    predicao: int
    porcentagem_benigno: float
    peso_idade: float
    peso_tamanho_nodulo: float
    peso_historico_familiar: float
    peso_nodulo_palpavel: float
    peso_birads_usg: float
    peso_birads_mamografia: float
    
    def __init__(self, prontuario, predicao, porcentagem_benigno,
                 peso_idade, peso_tamanho_nodulo, peso_historico_familiar, 
                 peso_nodulo_palpavel, peso_birads_usg, peso_birads_mamografia):
        self.prontuario = prontuario
        self.predicao = predicao
        self.porcentagem_benigno = porcentagem_benigno
        self.peso_idade = peso_idade
        self.peso_historico_familiar = peso_historico_familiar
        self.peso_nodulo_palpavel = peso_nodulo_palpavel
        self.peso_tamanho_nodulo = peso_tamanho_nodulo
        self.peso_birads_usg = peso_birads_usg
        self.peso_birads_mamografia = peso_birads_mamografia

    def __array__(self) -> list:
        return [self.porcentagem_benigno, self.peso_idade, self.peso_historico_familiar, 
                self.peso_nodulo_palpavel, self.peso_tamanho_nodulo,
                self.peso_birads_usg, self.peso_birads_mamografia]
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)