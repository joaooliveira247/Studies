let programmer = {
  name: "John",
  age: 18,
};

export function showProgrammer(programmer: {
  name: string;
  age: number;
  skills?: Array<string>;
}): void {
  console.log(programmer);
}

showProgrammer(programmer);
