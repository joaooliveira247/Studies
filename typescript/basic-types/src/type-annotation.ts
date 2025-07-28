let product: string = "Microwave";

let price: number = 647.52;

// product.toUpperCase();

// price.toFixed(0);


export function display(product: string, price: number): void {
    console.log(product.toUpperCase(), price.toFixed(0));
}

display(product, price);