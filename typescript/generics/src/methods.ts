class Stack {
    static last<T>(arr: T[]): T | undefined {
        if (arr.length > 0) return arr[arr.length - 1];
    }
}

const numbers = [1, 2, 3, 4, 5];
const lastNumber = Stack.last(numbers);

console.log(lastNumber);
