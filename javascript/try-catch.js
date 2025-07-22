function countLetters(product) {
    try {
        console.log(product.productName.length);
    } catch(err) {
        console.log(err);
    } finally {
        console.log("Finally");
    }
}

function printError() {
    throw new Error("teste");
}

const product = {
    productNam: "Notebook",
    price: 1200,
}

countLetters(product);
printError();