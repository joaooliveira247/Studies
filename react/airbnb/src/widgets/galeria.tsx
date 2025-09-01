import Image from "next/image";

type Foto = {
    id: string;
    source: string;
    description: string;
};

interface GaleriaProps {
    fotos: Foto[];
}

const Galeria = ({ fotos }: GaleriaProps) => {
    return (
        <div className="grid grid-cols-6 gap-2">
            {fotos.slice(0, 9).map((foto, idx) => {
                const first = idx == 0 ? "col-span-2 row-span-2" : "";
                return (
                    <div key={idx} className={`${first}`}>
                        <Image
                            className="w-full aspect-square object-cover"
                            src={foto.source}
                            alt={foto.description}
                            width={1280}
                            height={720}
                        />
                    </div>
                );
            })}
        </div>
    );
};

export default Galeria;
