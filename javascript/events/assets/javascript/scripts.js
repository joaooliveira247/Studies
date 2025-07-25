function exec() {
    console.log("Run");
}

// const button = document.getElementById("button");
// button.onclick = exec;

const button = document.querySelector("[button-action]");
button.addEventListener("click", exec);
// button.onclick = exec;