export function Acomodacao() {
    return (
        <div>
            <span>Image</span>
            <h1>Hello</h1>
            <p>desc</p>
        </div>
    );
}


export default function Home() {
    const firstName = "john";
    return (
        <div>
            {Acomodacao()}
            <hr />
            {Acomodacao()}
            <hr />
            {firstName}
        </div>
    );
}