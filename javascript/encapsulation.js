class Account {
    constructor() {
        this._accountNumber = 0;
        this.balance = 0;
    }

    get accountNumber() {
        return this._accountNumber;
    }

    set accountNumber(number) {
        this._accountNumber = number
    }
}

const account1 = new Account();
console.log(account1.accountNumber);
account1.accountNumber = 16;
console.log(account1.accountNumber);
