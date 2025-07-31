const title = document.getElementById("title");
const subtitle = document.getElementById("subTitle");

console.log("title: ", title?.innerText);
console.log("subtitle: ", subtitle?.innerText);
console.log("subtitle: color", subtitle?.style.color);

if (subtitle) {
    subtitle.style.color = "red";
}
