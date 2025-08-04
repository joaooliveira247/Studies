interface TableProps {
    data: Game[];
    colums: Array<{
        header: string;
        accessor: (item: Game) => string | number;
    }>;
}

function createTable({ data, colums }: TableProps): HTMLTableElement {
    const table = document.createElement("table");
    table.setAttribute("border", "1");

    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    colums.forEach((column) => {
        const th = document.createElement("th");
        th.textContent = column.header;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");

    data.forEach((row) => {
        const bodyRow = document.createElement("tr");

        colums.forEach((column) => {
            const td = document.createElement("td");
            td.textContent = column.accessor(row).toString();
            bodyRow.appendChild(td);
        });
        tbody.appendChild(bodyRow);
    });
    table.appendChild(tbody);

    return table;
}

interface Game {
    id: number;
    title: string;
    price: number;
}

const games: Game[] = [
    { id: 1, title: "League Of Legends", price: 0 },
    { id: 2, title: "GTA V", price: 50 },
    { id: 3, title: "Minecraft", price: 120 },
];

const table = createTable({
    data: games,
    colums: [
        { header: "ID", accessor: (game: Game) => game.id },
        { header: "Title", accessor: (game: Game) => game.title },
        { header: "Price", accessor: (game: Game) => game.price },
    ],
});
document.body.appendChild(table);
