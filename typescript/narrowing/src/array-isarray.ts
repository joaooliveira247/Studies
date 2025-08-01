let arr: number[] | undefined = [1, 2, 3, 4];

console.log(typeof arr);
console.log(arr instanceof Array);
console.log(Array.isArray(arr));

if (Array.isArray(arr)) {
    arr.map((item) => {
        console.log(item);
    });
}

// arr?.map((item) => {
//     console.log(item);
// });
