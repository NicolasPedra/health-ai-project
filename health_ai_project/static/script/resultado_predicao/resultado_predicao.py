import json
from pyscript import document
import matplotlib.pyplot as plt

def consultar_predicao(): 
    predicao_paciente_db = json.loads(document.getElementById("predicao_paciente_db").textContent)

    valores: list[int] = [predicao_paciente_db['peso_idade'], 
                                predicao_paciente_db['peso_historico_familiar'],
                                predicao_paciente_db['peso_nodulo_palpavel'],
                                predicao_paciente_db['peso_tamanho_nodulo'],
                                predicao_paciente_db['peso_birads_usg'],
                                predicao_paciente_db['peso_birads_mamografia']]
    
    valores_negativos = obterValoresNegativos(valores)
    valores_positivos = obterValoresPositivos(valores)
    print(valores_negativos)
    print(valores_positivos)
    exibirGrafico(valores_negativos, valores_positivos)

def exibirGrafico(valores_negativos: list[int], valores_positivos: list[int]): 
    print('inicio')
    categorias = ['Idade', 'Histórico familiar', 'Nódulo Palpável', 'Tamanho do nódulo', 'BI-RADS USG', 'BI-RADS Mamografia']
    font_color = '#525252'
    hfont = {'fontname':'DejaVu Sans'}
    color_red = '#fd625e'
    color_blue = '#01b8aa'
    titulo_negativo = "Benigno"
    titulo_positivo = 'Maligno' 

    fig, axes = plt.subplots(figsize=(14, 7), ncols=2,sharey=True)
    fig.canvas.set_window_title('')
    fig.tight_layout()

    axes[0].barh(categorias, valores_negativos, align='center', color=color_blue, zorder=10)
    axes[0].set_title(titulo_negativo, fontsize=18, pad=15, color=color_blue, **hfont)
    axes[1].barh(categorias, valores_positivos, align='center', color=color_red, zorder=10)
    axes[1].set_title(titulo_positivo, fontsize=18, pad=15, color=color_red, **hfont)
    
    plt.gca().invert_yaxis()

    axes[0].set_xticks([0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100])
    axes[0].set(yticks=categorias, yticklabels=categorias)
    axes[0].yaxis.tick_left()
    axes[0].tick_params(axis='y', colors='white') # tick color

    axes[1].set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    for label in (axes[0].get_xticklabels() + axes[0].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)
    for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)
        
    plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)
    plt.show()
    print('fim')

def obterValoresPositivos(valores: list[int]):
    valores_positivos = []

    for valor in valores:
        if (valor >= 0):
            valores_positivos.append(valor * 100)
        else:
            valores_positivos.append(0)

    return valores_positivos

def obterValoresNegativos(valores: list[int]):
    valores_negativos = []

    for valor in valores:
        if (valor >= 0):
            valores_negativos.append(0)
        else:
            valores_negativos.append(valor * 100)
    
    return valores_negativos

consultar_predicao()