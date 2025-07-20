function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function motivationPhrases() {
    const phrases = [
    "Você é mais forte do que imagina e capaz de ir além do que sonha.",
    "Desafios são oportunidades disfarçadas de obstáculos.",
    "O sucesso é a soma de pequenos esforços repetidos diariamente.",
    "Não espere por motivação, crie disciplina.",
    "Cada dia é uma nova chance de recomeçar com mais sabedoria.",
    "O medo é só um degrau antes da conquista.",
    "Acredite em você mesmo, mesmo quando ninguém mais acreditar.",
    "Grandes jornadas começam com o primeiro passo."
    ];

    let max = phrases.length;

    document.getElementById("phrase").innerHTML = phrases[getRandomInt(max)];
}