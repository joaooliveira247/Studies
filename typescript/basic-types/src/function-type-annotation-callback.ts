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

type ApplyDiscountFn = (total: number, discount: number) => number;

const applyDiscount: ApplyDiscountFn = (
    total: number,
    discount: number
): number => {
    return total - total * discount;
};

type calculateTotalFn = (
    sC: ShoppingCart,
    callback: ApplyDiscountFn
) => number;

let calculateTotal: calculateTotalFn = function (
    cart: ShoppingCart,
    discountCallback: ApplyDiscountFn
): number {
    const total = shoppingCart.cartItems.reduce(
        (acc, item) => acc + item.price,
        0
    );
    return discountCallback(total, 0.1);
};

type AddressOrUndefined = (c: Customer) => Address | undefined;

let getMainAddress: AddressOrUndefined;

getMainAddress = function (customer: Customer): Address | undefined {
    return customer.addresses.addresses.find((address) => address.default);
};

const total = calculateTotal(shoppingCart, applyDiscount);

console.log(total);

export { calculateTotal, getMainAddress };
