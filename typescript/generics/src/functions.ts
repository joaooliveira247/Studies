function processAndReturn<TypeValue>(value: TypeValue): TypeValue {
    return value;
}

const x = processAndReturn("abc");
const y = processAndReturn(7);

console.log(x);
