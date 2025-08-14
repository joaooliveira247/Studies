import { ConteudoIndireta } from "./ConteudoIndireta";

interface AbaProps {
    atualizar(name: string): void;
}

export function AbaIndireta(props: AbaProps) {
    return (
        <div>
            <button onClick={() => props.atualizar("Conversas")}>
                Conversas
            </button>
            <button onClick={() => props.atualizar("Atualizações")}>
                Atualizações
            </button>
            <button onClick={() => props.atualizar("Conversas")}>
                Chamadas
            </button>

            <ConteudoIndireta />
        </div>
    );
}
