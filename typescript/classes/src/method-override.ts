class PaymentMethod {
    processPayment(amount: number): void {
        console.log(`Process Payment | USD: ${amount}`);
    }
}

class CreditCartPayment extends PaymentMethod {
    override processPayment(amount: number): void {
        console.log(`Process Payment with Credit Card | USD: ${amount}`);
    }
}

const payment1 = new PaymentMethod();
payment1.processPayment(1200);

const payment2 = new PaymentMethod();
payment1.processPayment(3600);
