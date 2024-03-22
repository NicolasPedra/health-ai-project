from pyscript import document
import matplotlib.pyplot as plt
 

def submit(event):
    form = document.getElementById("form")

    if (form.checkValidity() == False):
        event.preventDefault()
        event.stopPropagation()

    form.classList.add('was-validated')
