interface User {
    id: number;
    name: string;
    email: string;
    isAdmin: boolean;
}

function updateUser(user: User, updates: Partial<User>): User {
    return { ...user, ...updates };
}

// Exemplo de uso:
const user: User = {
    id: 1,
    name: "João",
    email: "joao@email.com",
    isAdmin: false,
};

const updated = updateUser(user, {
    name: "João Silva",
    email: "silva@email.com",
});

console.log(updated);
