function setarRadio(name){
    var radios = document.getElementsByName(name)

    for (var i = 0; i < radios.length; i++) {  
      if (radios[i].value == radios[i].getAttribute('selecionado'))
          radios[i].checked = true
    }
}

function setarSelectOption(id){
  var options = document.getElementById(id).options

  for (var i = 0; i < options.length; i++) {  
    if (options[i].value == document.getElementById(id).getAttribute('selecionado'))
        options[i].selected = true
  }
}