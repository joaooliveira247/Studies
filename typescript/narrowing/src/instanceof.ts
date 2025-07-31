class BankAccount {
    protected holder: string;
    protected balance: number;

    constructor(holder: string, balance: number) {
        this.holder = holder;
        this.balance = balance;
    }

    public getHolder(): string {
        return this.holder;
    }
}

class CheckingAccount extends BankAccount {
    private overdraftLimit: number;

    constructor(holder: string, balance: number, overdraftLimit: number) {
        super(holder, balance);
        this.overdraftLimit = overdraftLimit;
    }

    public getOverdraftLimit(): number {
        return this.overdraftLimit;
    }
}

class SavingAccount extends BankAccount {
    private interestRate: number;

    constructor(holder: string, balance: number, interestRate: number) {
        super(holder, balance);
        this.interestRate = interestRate;
    }

    public getInterestRate(): number {
        return this.interestRate;
    }
}

const a = new BankAccount("John", 15000);
const b = new CheckingAccount("Peter", 5000, 10000);

console.log(a);
console.log(a instanceof BankAccount);
console.log(b instanceof BankAccount);
