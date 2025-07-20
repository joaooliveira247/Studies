const names = ["Ana", "Lucas", "Beatriz", "Rafael", "Mariana", "Gabriel", "Juliana", "Pedro", "Camila", "Thiago"];

function load() {
    let htmlNames = [];
    for (i in names) {
        htmlNames.push(`<li class="list-group-item">${names[i]}</li>`);
    }
    const html = htmlNames.join("\n");
    document.getElementById("list-group").innerHTML = html;
}

function search() {
    const name = document.getElementById("name").value;

    for (i in names) {
        if (names[i] == name) {
            document.getElementById("list-group").innerHTML = `<li class="list-group-item">${names[i]}</li>`
            return;
        }
    }
    document.getElementById("list-group").innerHTML = "<li class='list-group-item'>Usuário não encontrado</li>"
}