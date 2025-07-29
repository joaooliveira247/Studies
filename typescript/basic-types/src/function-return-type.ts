type CartItem = {
    id: number;
    price: number;
};

type ShoppingCart = {
    cartItems: CartItem[];
};

type Address = {
    cep: string;
    default: boolean;
};

type Addresses = {
    addresses: Address[];
};

type Customer = {
    addresses: Addresses;
};

const shoppingCart: ShoppingCart = {
    cartItems: [
        { id: 1, price: 100 },
        { id: 2, price: 200 },
        { id: 3, price: 300 },
    ],
};

const addresses: Addresses = {
    addresses: [
        { cep: "00000-000", default: false },
        { cep: "00000-001", default: true },
        { cep: "00000-002", default: false },
    ],
};

const customer: Customer = {
    addresses: addresses,
};

export function calculateTotal(cart: ShoppingCart): number {
    const total = shoppingCart.cartItems.reduce(
        (acc, item) => acc + item.price,
        0
    );
    return total;
}

export function getMainAddress(customer: Customer): Address | undefined {
    return customer.addresses.addresses.find((address) => address.default);
}

const total = calculateTotal(shoppingCart);

console.log(total);
