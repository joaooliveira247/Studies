type Movie = {
    title: string;
    year: number;
    isFavorite: boolean;
    genre: string;
    director: string;
    [key: string | number]: string | number | boolean;
};

type Movies = {
    [key: string]: Movie;
};

let movies = {
    movie1: {
        title: "A Origem",
        year: 2010,
        isFavorite: true,
        genre: "Ficção Científica",
        director: "Christopher Nolan",
    },
    movie2: {
        title: "Um Sonho de Liberdade",
        year: 1994,
        isFavorite: true,
        genre: "Drama",
        director: "Frank Darabont",
        runtime: 142,
    },
    movie3: {
        title: "O Senhor dos Anéis: A Sociedade do Anel",
        year: 2001,
        isFavorite: false,
        genre: "Fantasia",
        director: "Peter Jackson",
        oscars: 4,
    },
};

export default function showMovies(movies: Movies): void {
    console.log(movies);
}

showMovies(movies);
