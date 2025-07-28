let shoppingCart: Array<number | string> = [
  200.75,
  150.12,
  "33.90",
  "44",
  "null",
];

export function totalize(values: (string | number)[]): number {
  return values
    .map((value) => (typeof value === "number" ? value : parseFloat(value)))
    .filter((value) => !isNaN(value))
    .reduce((acc, currentValue) => acc + currentValue, 0);
}

console.log(totalize(shoppingCart));
