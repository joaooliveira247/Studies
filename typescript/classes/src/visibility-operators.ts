class Product2 {
    public productName: string;
    protected price: number;
    private stock: number;

    constructor(productName: string, price: number, stock: number) {
        this.productName = productName;
        this.price = price;
        this.stock = stock;
    }
}

class Eletronic extends Product2 {
    showDetails(): void {
        // stock can't be acessed 'cause it's private
        console.log(`${this.productName} | USD: ${this.price}`);
    }
}
