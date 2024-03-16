from pyscript import window, document
import matplotlib.pyplot as plt
import numpy as np
import sys


def submit(event):
    # form = document.getElementById("form")

    # if (form.checkValidity() == False):
    #     event.preventDefault()
    #     event.stopPropagation()

    # form.classList.add('was-validated')
    exibirGrafico([10, 20, 45, 15, 5, 5])

def exibirGrafico(valores: list[int]): 
    plt.figure(1, figsize=(10, 4.7), layout='constrained')
    categories = ['Idade', 'Histórico familiar', 'Nódulo Palpável', 'Tamanho do nódulo', 'BI-RADS USG', 'BI-RADS Mamografia']

    plt.bar(categories, valores)
    plt.show()
