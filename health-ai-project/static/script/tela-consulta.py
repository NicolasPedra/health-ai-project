from matplotlib import gridspec
from pyscript import window, document
import matplotlib.pyplot as plt
import numpy as np

def submit(event):
    # form = document.getElementById("form")

    # if (form.checkValidity() == False):
    #     event.preventDefault()
    #     event.stopPropagation()

    # form.classList.add('was-validated')
    exibirGraficos([10, 20, 45, 15, 5, 5])

def exibirGraficos(valores: list[int]): 
    
    colors = [ 'red', 'burlywood', 'lawngreen', 'slategrey', 'gold', "indianred"]
    f1 = plt.figure(1, figsize=(10, 4.7), layout='constrained')
    categories = ['Idade', 'Histórico familiar', 'Nódulo Palpável', 'Tamanho do nódulo', 'BI-RADS USG', 'BI-RADS Mamografia']

    plt.bar(categories, valores, color=colors)
    plt.show()

    print('\n' * 5)

    f2 = plt.figure(2, figsize=(10, 4.7), layout='constrained')
    plt.pie(valores, labels=categories, autopct='%1.1f%%', colors=colors)
    plt.show()
    
