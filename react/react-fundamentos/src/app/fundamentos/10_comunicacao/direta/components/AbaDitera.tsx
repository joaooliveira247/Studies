import { useState } from "react";
import { ConteudoDireta } from "./ConteudoDireta";

export function AbaDireta() {
    const [aba, setAba] = useState("");

    return (
        <div>
            <button onClick={() => setAba("Conversas")}>Conversas</button>
            <button onClick={() => setAba("Atualizações")}>
                Atualizações
            </button>
            <button onClick={() => setAba("Chamadas")}>Chamadas</button>

            <ConteudoDireta name={aba} />
        </div>
    );
}
