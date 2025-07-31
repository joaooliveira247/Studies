type Person = {
    name: string;
    age: number;
};

type Employee = {
    departament: string;
};

type Customer = {
    wishlist: string[];
};

type EmployeeDetails = Person & Employee;

const employee: EmployeeDetails = {
    name: "John",
    age: 26,
    departament: "TI",
};

type CustomerDetails = Person & Customer;

const customer: CustomerDetails = {
    name: "Peter",
    age: 32,
    wishlist: ["a", "b"],
};
