from pyscript import window, document


def submit(event):
    form = document.getElementById("form")

    if (form.checkValidity() == False):
        event.preventDefault()
        event.stopPropagation()

    form.classList.add('was-validated')