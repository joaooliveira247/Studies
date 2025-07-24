// const obj = document.getElementsByName("sign-up-form");
const obj = document.forms;
document.signupform.email.placeholder = "teste";
console.log(obj);

function setValues() {
    document.signupform.name.value = "John";
    document.signupform.email.value = "John@email.com";
    document.signupform.gender.value = "male";
}