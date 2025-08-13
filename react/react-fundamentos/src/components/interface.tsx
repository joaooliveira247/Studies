import Link from "next/link";

export function Acomodacao() {
    return (
        <div>
            <span>Image</span>
            <h1>Hello</h1>
            <p>desc</p>
        </div>
    );
}

export function Button() {
    return <button>Common Button</button>;
}

export function Menu() {
    return (
        <div className="bg-yellow-500">
            <MenuItem text="Home" url="/home" />
        </div>
    );
}

export function MenuItem(props: any) {
    return <Link href={props.url}>{props.text}</Link>;
}

interface HeaderProps {
    title: string;
    className?: string;
}

export function Header(props: HeaderProps) {
    return (
        <div className={props.className}>
            <h1>Logo</h1>
            <p>{props.title}</p>
            <p>
                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quos
                eum ipsa, commodi quidem animi nemo velit quis magnam magni
                alias! Exercitationem mollitia iure praesentium amet, rem
                officia perspiciatis ab! Odit!
            </p>
            {Menu()}
        </div>
    );
}

export function Content(props: any) {
    return (
        <div className="bg-amber-200">
            <h1>Content</h1>
            {props.children}
        </div>
    );
}
