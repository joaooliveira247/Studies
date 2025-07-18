function calcBetterPrice() {
    let alcohol = document.getElementById("alcool").value;
    let gasoline = document.getElementById("gasolina").value;

    if (alcohol != ""){
        if ( gasoline != "") {
            let calcResult = alcohol / gasoline

            if (calcResult >= 0.7) {
                document.getElementById("resultado").innerHTML = "Melhor usar gasolina";
            } else {
                document.getElementById("resultado").innerHTML = "melhor usar álcool";
            }
        } else {
            alert("Campo gasoline não pode estar vazio")
        }
    } else {
        alert("Campo álcool não pode estar vazio")
    }
}