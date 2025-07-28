let moviesArray: Array<number | string | boolean> = [
  1,
  "The Godfather",
  false,
];

// ? can be optional
let moviestTuple: [number, string, boolean?] = [1, "The Godfather", false];

const [id, title, available] = moviestTuple;
