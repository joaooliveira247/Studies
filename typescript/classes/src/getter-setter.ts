class User2 {
    constructor(
        private name: string,
        private age: number,
        private _bio?: string
    ) {}

    // setter
    set bio(bio: string) {
        this._bio = bio;
    }
    // getter
    get bio(): string {
        return this._bio || "undefined bio";
    }
}

const user2 = new User2("john", 18);
console.log(user2.bio);
