interface Person {
    name: string;
    age: number;
}
// put all interfaces in archives with name file.d.ts
interface Employee extends Person {
    employeeId: number;
    department: string;
}

const dev: Employee = {
    name: "Ana",
    age: 30,
    employeeId: 1234,
    department: "Engineering",
};

console.log(dev);
