import json
from pyscript import document
import matplotlib.pyplot as plt


#=============== ÍNICIO - MÓDULOS =============#
class DadosPaciente:
    idade: int
    historico_familiar: bool
    nodulo_palpavel: bool
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
#=============== FIM - MÓDULOS =============#


def consultar(event):
    # form = document.getElementById("form")

    # if (form.checkValidity() == False):
    #     event.preventDefault()
    #     event.stopPropagation()

    # form.classList.add('was-validated')

    dados_paciente = obterDadosPaciente()
    print(dados_paciente.__array__())

    exibirGraficos([15, 10, 25, 20, 10, 20])

def voltar(event):
    navegar('form', '/', 'GET')

def obterDadosPaciente() -> DadosPaciente:
    idade = document.getElementById("idade").value
    historico = str2bool(document.getElementsByName("historico")[0].value)
    nodulo_palpavel = str2bool(document.getElementsByName("nodulo-palpavel")[0].value)
    tamanho_nodulo = document.getElementById("tamanho-nodulo").value
    birads_usg = document.getElementById("bi-rads-usg").value
    birads_mamografia = document.getElementById("bi-rads-mamografia").value
 
    return DadosPaciente(idade, historico, nodulo_palpavel, tamanho_nodulo, birads_usg, birads_mamografia)

def exibirGraficos(valores: list[int]): 
    
    colors = [ 'red', 'burlywood', 'lawngreen', 'slategrey', 'gold', "indianred"]
    f1 = plt.figure(1, figsize=(10, 4.7), layout='constrained')
    categories = ['Idade', 'Histórico familiar', 'Nódulo Palpável', 'Tamanho do nódulo', 'BI-RADS USG', 'BI-RADS Mamografia']

    plt.bar(categories, valores, color=colors)
    plt.show()

    f2 = plt.figure(2, figsize=(10, 4.7), layout='constrained')
    plt.pie(valores, labels=categories, autopct='%1.1f%%', colors=colors)
    plt.show()

def navegar(id_form, rota, metodo):
    form = document.getElementById(id_form)
    form.action = rota
    form.method = metodo
    form.submit()