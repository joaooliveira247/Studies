type Item = {
    id: number;
    [key: string]: string | number | null;
};

const response: Item[] = [
    { id: 1, movie: "Harry Potter" },
    { id: 2, song: "RED" },
    { id: 2, song: "Decode" },
    { id: 2, video: "TS in 100 seconds" },
];

function showItems(items: Item[]) {
    const body = document.querySelector("body");

    if (body instanceof HTMLBodyElement) {
        items.map((item) => {
            const itemElement = document.createElement("div");

            if ("song" in item) {
                itemElement.textContent = item.song.toString;
            } else if ("movie" in item) {
                itemElement.textContent = item.movie.toString;
            }
        });
    }
}
