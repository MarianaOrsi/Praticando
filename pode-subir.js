/* A pessoa deve medir mais de 1.40m e menos de 2 metros.
Se a pessoa medir menos de 1.40m, deverá ir acompanhada.
Se a pessoa medir menos de 1.20m, não poderá subir, nem acompanhada. */

/* Em caso de autorização, exiba a mensagem: "Acesso autorizado" ou 
"Acesso autorizado somente com acompanhante"
Em caso de impedimento, exiba a mensagem: "Acesso negado."" */



function podeSubir(x, y) {
    let altura = x;
    let acompanhada = y;
    if (altura > 1.40 && altura <= 2) {
        return "Acesso autorizado."
    } else if (altura <= 1.40 && altura >= 1.20 && acompanhada) {
        return "Acesso autorizado somente com acompanhante."
    } else {
        return "Acesso negado."
    }
}

console.log(podeSubir(1.40, true));