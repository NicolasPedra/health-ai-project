
import json


class DadosPaciente:
    prontuario: str
    idade: int
    historico_familiar: int
    nodulo_palpavel: int
    tamanho_nodulo: float
    birads_usg: int
    birads_mamografia: int

    def __init__(self, prontuario, idade, historico_familiar, nodulo_palpavel, tamanho_nodulo, birads_usg, birads_mamografia):
        self.prontuario = prontuario
        self.idade = idade
        self.historico_familiar = historico_familiar
        self.nodulo_palpavel = nodulo_palpavel
        self.tamanho_nodulo = tamanho_nodulo
        self.birads_usg = birads_usg
        self.birads_mamografia = birads_mamografia

    def __array__(self) -> list:
        return [self.idade, self.historico_familiar, self.nodulo_palpavel, 
                self.tamanho_nodulo, self.birads_usg, self.birads_mamografia]
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)