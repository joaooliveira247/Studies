class Product {
    private productName: string;
    private price: number;

    constructor(productName: string, price: number) {
        this.productName = productName;
        this.price = price;
    }

    showDetails(): void {
        console.log(`${this.productName} | USD: ${this.price}`);
    }
}

const product = new Product("Smatphone", 3750.55);
product.showDetails();
