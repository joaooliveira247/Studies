let productName = "Notebook";
let price = 1200;

/*
const product = {
    productName: productName,
    price: price,
    showProduct: function(){
        console.log(`ProductName: ${this.productName}, Price: ${this.price}`)
    }
 }
*/

const product = {
    productName,
    price,
    showProduct(){
        console.log(`ProductName: ${this.productName}, Price: ${this.price}`)
    }
}

product.showProduct();