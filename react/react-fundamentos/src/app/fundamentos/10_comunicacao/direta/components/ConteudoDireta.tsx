interface ConteudoProps {
    name: string;
}

export function ConteudoDireta(props: ConteudoProps) {
    return (
        <div>
            <span>{props.name}</span>
        </div>
    );
}
