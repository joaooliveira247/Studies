interface User {
    id: number;
    name: string;
}

const user: Readonly<User> = {
    id: 1,
    name: "Maria",
};

console.log(user);
