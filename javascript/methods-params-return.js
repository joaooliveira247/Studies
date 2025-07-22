class User {
    constructor(email, passwd) {
        this.email = email;
        this.passwd = passwd;
    }

    logIn() {
        return "Fake JWT";
    }

    discount(coupon) {
        return coupon;
    }
}