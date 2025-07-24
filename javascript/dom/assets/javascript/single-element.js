// const obj = document.getElementById('detach');
const obj = document.querySelector("li.first-item");
console.log(obj.textContent);

function changeValue() {
    const obj = document.querySelector("li.first-item");
    obj.textContent = "Teste";
    obj.classList.add("detach");
}