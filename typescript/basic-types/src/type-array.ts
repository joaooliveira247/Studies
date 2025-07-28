let movies: string[] = ["Dune: part two", "Harry Potter and the chamber of secrets"];
let movies2: Array<string> = ["Dune: part two", "Harry Potter and the chamber of secrets"];


export function toUpperCaseStrings(arr: Array<string>): Array<string>{
    return arr.map(value => value.toUpperCase());
}

console.log(toUpperCaseStrings(movies2));