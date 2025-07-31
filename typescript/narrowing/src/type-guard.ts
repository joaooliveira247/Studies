const zipCodeMask = (value: string | number): string => {
    if (typeof value === "number") {
        value = value.toString();
    }
    value = value.replace(/\D/g, "");
    value = value.replace(/(\d{5})(\d)/, `$1-$2`);
    return value;
};

const zipCode = zipCodeMask("10000000");
console.log(zipCode);
