import { IconHeartFilled, IconStarFilled } from "@/assets/icons";

interface AccommodationProps {
    children: React.ReactNode;
    local: string;
    anfitriao: string;
    date: string;
    price: number;
    avaliacao: number;
    preferidoHospede: boolean;
}

const Accommodation = ({
    children,
    local,
    anfitriao,
    date,
    price,
    avaliacao,
    preferidoHospede,
}: AccommodationProps) => {
    return (
        <figure className="relative">
            <div className="p-2 absolute w-full flex flex-row justify-between items-center">
                <div>
                    {preferidoHospede && (
                        <span className="bg-white rounded-full px-4 py-1 font-semibold">
                            Preferido dos hóspedes
                        </span>
                    )}
                </div>
                <IconHeartFilled
                    className="stroke-white opacity-80"
                    aria-label="fav icon"
                    size={30}
                />
            </div>

            {children}
            <figcaption className="pt-2">
                <div className="flex flex-row justify-between">
                    <span className="font-semibold">{local}</span>
                    <div className="flex flex-row gap-1">
                        <IconStarFilled
                            className=""
                            aria-label="stars icon"
                            size={20}
                        />
                        <span className="font-semibold">{avaliacao}</span>
                    </div>
                </div>
                <div>Anfitrião: {anfitriao}</div>
                <div>{date}</div>
                <div className="font-semibold">R$: {price}</div>
            </figcaption>
        </figure>
    );
};

export default Accommodation;
