import Logo from "@/components/logo";
import Link from "next/link";
import ButtonIcon from "@/components/buttonIcon";
import { IconUserCircle } from "@/assets/icons";

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
            <ButtonIcon
                icone={<IconUserCircle aria-label="icone usuario" size={20} />}
            >
                Entrar
            </ButtonIcon>
        </div>
    );
};

export default header;
