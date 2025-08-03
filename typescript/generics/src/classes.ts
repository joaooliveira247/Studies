class Stack2<T> {
    constructor(private stack: T[]) {}
    last(): T | undefined {
        if (this.stack.length > 0) return this.stack[this.stack.length - 1];
    }
}

const numbers2 = [1, 2, 3, 4, 5];
const stack1 = new Stack2(numbers2);
