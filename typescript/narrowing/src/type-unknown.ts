let valueUnknown: unknown; // unknown type
valueUnknown = [1, 2, 3];

// let valueAny: any; // can be any type value

// valueAny.toFixed();

function processDataWithUnknown(value: unknown) {
    if (Array.isArray(value)) {
        value.map((item) => console.log(item));
    }
}

processDataWithUnknown(valueUnknown);
