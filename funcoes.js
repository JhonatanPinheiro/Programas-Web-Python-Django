function gritar(){
    alert("Ahhhhhhhhhhhhhhhh");
}


function perguntar(){
    var nome;
    nome = prompt("Qual é o seu nome? ");
    alert("Olá" + nome);
}

function mudar_texto(){
    var h1 = document.getElementsByTagName("h1");

    if(h1[0].innerText == "Geek University"){
        h1[0].innerText = "Evolua seu lado Geek!";
    }else{
        h1[0].innerText = "Geek University";
    }

}


function incrementar(){
    var p1  = document.getElementById("p1");

    p1.innerText = parseInt(p1.innerText) + 1;
}

