import Logo from "@/components/logo/logo";
import Link from "next/link";

const header = () => {
    return (
        <div className="container mx-auto flex justify-between items-center py-6">
            <Logo />
            <div className="flex gap-6">
                <Link className="font-semibold" href={"/"}>
                    Acomodações
                </Link>
                <Link className="font-semibold" href={"/"}>
                    Experiências
                </Link>
            </div>
            <button className="rounded-md border-2">Entrar</button>
        </div>
    );
};

export default header;
