import { Acomodacao, Button, Header } from "@/components/interface";

export default function Home() {
    const firstName = "john";
    return (
        <div>
            {Header()}
            <hr />
            {Acomodacao()}
            <hr />
            {firstName}
            <hr />
            {Button()}
        </div>
    );
}