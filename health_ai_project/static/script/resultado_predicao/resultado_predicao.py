import json
from pyscript import document
import matplotlib.pyplot as plt

def consultar_predicao(): 
    predicao_paciente_db = json.loads(document.getElementById("predicao_paciente_db").textContent)

    print(predicao_paciente_db)
    exibirGraficos([predicao_paciente_db['peso_idade'] * 100, 
                    predicao_paciente_db['peso_historico_familiar'] * 100,
                    predicao_paciente_db['peso_nodulo_palpavel'] * 100,
                    predicao_paciente_db['peso_tamanho_nodulo'] * 100,
                    predicao_paciente_db['peso_birads_usg'] * 100,
                    predicao_paciente_db['peso_birads_mamografia'] * 100])

def voltar(event):
    navegar('form', '/dados_paciente', 'GET')

def exibirGraficos(valores: list[int]): 
    categories = ['Idade', 'Histórico familiar', 'Nódulo Palpável', 'Tamanho do nódulo', 'BI-RADS USG', 'BI-RADS Mamografia']
    font_color = '#525252'
    facecolor = '#eaeaf2'
    hfont = {'fontname':'DejaVu Sans'}
    color_red = '#fd625e'
    color_blue = '#01b8aa'
    titulo_negativo = "Benigno"
    titulo_positivo = 'Maligno'
    valores_negativos = []
    valores_positivos = []

    for valor in valores:
        if (valor >= 0):
            valores_positivos.append(valor)
            valores_negativos.append(0)
        else:
            valores_positivos.append(0)
            valores_negativos.append(valor)


    fig, axes = plt.subplots(figsize=(14, 7), ncols=2,sharey=True)
    fig.canvas.set_window_title('')
    fig.tight_layout()

    axes[0].barh(categories, valores_negativos, align='center', color=color_blue, zorder=10)
    axes[0].set_title(titulo_negativo, fontsize=18, pad=15, color=color_blue, **hfont)
    axes[1].barh(categories, valores_positivos, align='center', color=color_red, zorder=10)
    axes[1].set_title(titulo_positivo, fontsize=18, pad=15, color=color_red, **hfont)
    
    # If you have positive numbers and want to invert the x-axis of the left plot
    # To show data from highest to lowest
    plt.gca().invert_yaxis()

    axes[0].set_xticks([0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100])
    axes[0].set(yticks=categories, yticklabels=categories)
    axes[0].yaxis.tick_left()
    axes[0].tick_params(axis='y', colors='white') # tick color

    axes[1].set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    for label in (axes[0].get_xticklabels() + axes[0].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)
    for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)
        
    plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)
    plt.show()

def navegar(id_form, rota, metodo):
    form = document.getElementById(id_form)
    form.action = rota
    form.method = metodo
    form.submit()

consultar_predicao()