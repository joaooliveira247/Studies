type CartItem = {
    id: number;
    price: number;
};

type ShoppingCart = {
    cartItems: CartItem[];
};

const shoppingCart: ShoppingCart = {
    cartItems: [
        { id: 1, price: 100 },
        { id: 2, price: 200 },
        { id: 3, price: 300 },
    ],
};

export function calculateTotal(cart: ShoppingCart): void {
    const total = shoppingCart.cartItems.reduce(
        (acc, item) => acc + item.price,
        0
    );
    console.log(total);
}

calculateTotal(shoppingCart);
