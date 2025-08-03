class User {
    constructor(
        private name: string,
        private age: number,
        private bio?: string
    ) {}

    setBio(bio: string): void {
        this.bio = bio;
    }

    getBio(): string {
        return this.bio || "undefined bio";
    }
}

const user = new User("john", 18);
console.log(user.getBio());
