import { useState } from "react";
import { AbaIndireta } from "./AbaIndireta";

export function ConteudoIndireta() {
    const [aba, setAba] = useState("");

    function alterarNome(name: string) {
        setAba(name);
    }

    return (
        <div>
            <span>aba</span>
            <hr />
            <AbaIndireta atualizar={ alterarNome } />
        </div>
    );
}
