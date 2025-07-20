function main() {
    // While
    let num = 0;

    while (num < 4) {
        console.log(`Slice ${num + 1} eaten.`);
        num ++
    }
    // do...while
    let num2 = 0;

    do {
        console.log(`Exec ${num2}`);
        num ++
    } while (num2 >= 1)

    // for
    for (let i = 0; i < 4; i++) {
        console.log(`Slice ${i + 1} eaten.`);
    }

    const fruits = ["Apple", "Banana", "Avocado", "Grape", "Orange"];

    for ( i in fruits) {
        console.log(fruits[i]);    
    }
}

main();