import json
from pyscript import document
import matplotlib.pyplot as plt


#=============== ÍNICIO - MÓDULOS =============#
class DadosPaciente:
    idade: int
    historico_familiar: int
    nodulo_palpavel: int
    tamanho_nodulo: float
    birads_usg: int
    birads_mamografia: int

    def __init__(self, idade, historico_familiar, nodulo_palpavel, tamanho_nodulo, birads_usg, birads_mamografia):
        self.idade = idade
        self.historico_familiar = historico_familiar
        self.nodulo_palpavel = nodulo_palpavel
        self.tamanho_nodulo = tamanho_nodulo
        self.birads_usg = birads_usg
        self.birads_mamografia = birads_mamografia

    def __array__(self) -> list:
        return [self.idade, self.historico_familiar, self.nodulo_palpavel, 
                self.tamanho_nodulo, self.birads_usg, self.birads_mamografia]
    
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def intNull(valor):
    try:
        return int(valor)
    except ValueError:
        return None
#=============== FIM - MÓDULOS =============#

def submit(event):
    # form = document.getElementById("form")

    # if (form.checkValidity() == False):
    #     event.preventDefault()
    #     event.stopPropagation()

    # form.classList.add('was-validated')

    # dados_paciente_tela = obterDadosPacienteTela()
    # dados_paciente_db = json.loads(document.getElementById("dados_paciente_db").textContent)

    # alterado = verificarAlteracaoPaciente(dados_paciente_db, dados_paciente_tela)
    # print(dados_paciente_tela.__array__())
    navegar('form', '/dados_paciente', 'POST')

def obterDadosPacienteTela() -> DadosPaciente:
    idade = int(document.getElementById("idade").value)
    historico = int(document.querySelector('input[name="historico"]:checked').value)
    nodulo_palpavel = int(document.querySelector('input[name="nodulo-palpavel"]:checked').value)
    tamanho_nodulo = float(document.getElementById("tamanho-nodulo").value)
    birads_usg = intNull(document.getElementById("bi-rads-usg").value)
    birads_mamografia = intNull(document.getElementById("bi-rads-mamografia").value)
 
    return DadosPaciente(idade, historico, nodulo_palpavel, tamanho_nodulo, birads_usg, birads_mamografia)

def verificarAlteracaoPaciente(dados_paciente_db, dados_paciente_tela: DadosPaciente) -> bool:
    for attr, valor in dados_paciente_tela.__dict__.items():
        if (str(dados_paciente_db[attr]) != str(valor)):
            print(attr)
            print(dados_paciente_db[attr])
            print(valor)
            return False
    
    return True

def navegar(id_form, rota, metodo):
    form = document.getElementById(id_form)
    form.action = rota
    form.method = metodo
    form.submit()
