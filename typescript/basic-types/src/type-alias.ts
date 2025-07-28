type Salary = number | string;

type Programmer = {
  name: string;
  age: number;
  skills?: Array<string>;
  contact: { email: string; phone?: string };
  salary?: Salary;
};

export function showProgrammer(programmer: Programmer): void {
  console.log(programmer);
}

showProgrammer({ name: "John", age: 27, contact: { email: "email@email" } });
