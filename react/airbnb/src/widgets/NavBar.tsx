"use client";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import ButtonIcon from "@/components/buttonIcon";
import { IconAdjustmentsHorizontal } from "@/assets/icons";
import Link from "next/link";
import Image from "next/image";

const icons = [
    {
        id: "0001",
        description: "Piscina",
        source: "https://web.codans.com.br/airbnb/img/icon/0001.jpg",
        url: "/piscina",
    },
    {
        id: "0002",
        description: "Icônicos",
        source: "https://web.codans.com.br/airbnb/img/icon/0002.jpg",
        url: "/iconicos",
    },
    {
        id: "0003",
        description: "Chalés",
        source: "https://web.codans.com.br/airbnb/img/icon/0003.jpg",
        url: "/chales",
    },
    {
        id: "0004",
        description: "Vistas incríveis",
        source: "https://web.codans.com.br/airbnb/img/icon/0004.jpg",
        url: "/vistas-incriveis",
    },
    {
        id: "0005",
        description: "Casas na árvore",
        source: "https://web.codans.com.br/airbnb/img/icon/0005.jpg",
        url: "/casas-arvore",
    },
    {
        id: "0006",
        description: "Casas triangulares",
        source: "https://web.codans.com.br/airbnb/img/icon/0006.jpg",
        url: "/casas-triangulares",
    },
    {
        id: "0007",
        description: "Em frente à praia",
        source: "https://web.codans.com.br/airbnb/img/icon/0007.jpg",
        url: "/frente-praia",
    },
    {
        id: "0008",
        description: "Containêres",
        source: "https://web.codans.com.br/airbnb/img/icon/0008.jpg",
        url: "/containeres",
    },
    {
        id: "0009",
        description: "No interior",
        source: "https://web.codans.com.br/airbnb/img/icon/0009.jpg",
        url: "/interior",
    },
    {
        id: "0010",
        description: "Pousadas",
        source: "https://web.codans.com.br/airbnb/img/icon/0010.jpg",
        url: "/pousadas",
    },
    {
        id: "0011",
        description: "Na beira do lago",
        source: "https://web.codans.com.br/airbnb/img/icon/0011.jpg",
        url: "/beira-lago",
    },
    {
        id: "0012",
        description: "Parques nacionais",
        source: "https://web.codans.com.br/airbnb/img/icon/0012.jpg",
        url: "/parques-nacionais",
    },
    {
        id: "0013",
        description: "Microcasas",
        source: "https://web.codans.com.br/airbnb/img/icon/0013.jpg",
        url: "/microcasas",
    },
    {
        id: "0014",
        description: "Fazendas",
        source: "https://web.codans.com.br/airbnb/img/icon/0014.jpg",
        url: "/fazendas",
    },
    {
        id: "0015",
        description: "Mansões",
        source: "https://web.codans.com.br/airbnb/img/icon/0015.jpg",
        url: "/mansoes",
    },
    {
        id: "0016",
        description: "Ilhas",
        source: "https://web.codans.com.br/airbnb/img/icon/0016.jpg",
        url: "/ilhas",
    },
    {
        id: "0017",
        description: "Casas-barco",
        source: "https://web.codans.com.br/airbnb/img/icon/0017.jpg",
        url: "/casas-barco",
    },
    {
        id: "0018",
        description: "Luxe",
        source: "https://web.codans.com.br/airbnb/img/icon/0018.jpg",
        url: "/luxe",
    },
    {
        id: "0019",
        description: "Uau!",
        source: "https://web.codans.com.br/airbnb/img/icon/0019.jpg",
        url: "/uau",
    },
    {
        id: "0020",
        description: "Castelos",
        source: "https://web.codans.com.br/airbnb/img/icon/0020.jpg",
        url: "/castelos",
    },
    {
        id: "0021",
        description: "Ártico",
        source: "https://web.codans.com.br/airbnb/img/icon/0021.jpg",
        url: "/artico",
    },
    {
        id: "0022",
        description: "Tropical",
        source: "https://web.codans.com.br/airbnb/img/icon/0022.jpg",
        url: "/tropical",
    },
    {
        id: "0023",
        description: "Diversão",
        source: "https://web.codans.com.br/airbnb/img/icon/0023.jpg",
        url: "/diversao",
    },
    {
        id: "0024",
        description: "Em alta",
        source: "https://web.codans.com.br/airbnb/img/icon/0024.jpg",
        url: "/em-alta",
    },
    {
        id: "0025",
        description: "Casas de terra",
        source: "https://web.codans.com.br/airbnb/img/icon/0025.jpg",
        url: "/casas-de-terra",
    },
    {
        id: "0026",
        description: "Design",
        source: "https://web.codans.com.br/airbnb/img/icon/0026.jpg",
        url: "/design",
    },
    {
        id: "0027",
        description: "Cidades famosas",
        source: "https://web.codans.com.br/airbnb/img/icon/0027.jpg",
        url: "/cidades-famosas",
    },
    {
        id: "0028",
        description: "Quartos",
        source: "https://web.codans.com.br/airbnb/img/icon/0028.jpg",
        url: "/quartos",
    },
    {
        id: "0029",
        description: "Nas alturas",
        source: "https://web.codans.com.br/airbnb/img/icon/0029.jpg",
        url: "/nas-alturas",
    },
    {
        id: "0030",
        description: "Casas arredondadas",
        source: "https://web.codans.com.br/airbnb/img/icon/0030.jpg",
        url: "/casas-arredondadas",
    },
    {
        id: "0031",
        description: "Barcos",
        source: "https://web.codans.com.br/airbnb/img/icon/0031.jpg",
        url: "/barcos",
    },
    {
        id: "0032",
        description: "Cozinhas gourmet",
        source: "https://web.codans.com.br/airbnb/img/icon/0032.jpg",
        url: "/cozinhas-gourmet",
    },
    {
        id: "0033",
        description: "Energia alternativa",
        source: "https://web.codans.com.br/airbnb/img/icon/0033.jpg",
        url: "/energia-alternativa",
    },
    {
        id: "0034",
        description: "Acampamentos",
        source: "https://web.codans.com.br/airbnb/img/icon/0034.jpg",
        url: "/acampamentos",
    },
    {
        id: "0035",
        description: "Prédios históricos",
        source: "https://web.codans.com.br/airbnb/img/icon/0035.jpg",
        url: "/predios-historicos",
    },
    {
        id: "0036",
        description: "Espaços criativos",
        source: "https://web.codans.com.br/airbnb/img/icon/0036.jpg",
        url: "/espacos-criativos",
    },
    {
        id: "0037",
        description: "Vinhedos",
        source: "https://web.codans.com.br/airbnb/img/icon/0037.jpg",
        url: "/vinhedos",
    },
    {
        id: "0038",
        description: "Novidades",
        source: "https://web.codans.com.br/airbnb/img/icon/0038.jpg",
        url: "/novidades",
    },
    {
        id: "0039",
        description: "Deserto",
        source: "https://web.codans.com.br/airbnb/img/icon/0039.jpg",
        url: "/deserto",
    },
    {
        id: "0040",
        description: "Riads",
        source: "https://web.codans.com.br/airbnb/img/icon/0040.jpg",
        url: "/riads",
    },
    {
        id: "0041",
        description: "Grutas",
        source: "https://web.codans.com.br/airbnb/img/icon/0041.jpg",
        url: "/grutas",
    },
    {
        id: "0042",
        description: "Moinhos",
        source: "https://web.codans.com.br/airbnb/img/icon/0042.jpg",
        url: "/moinhos",
    },
    {
        id: "0043",
        description: "Celeiros",
        source: "https://web.codans.com.br/airbnb/img/icon/0043.jpg",
        url: "/celeiros",
    },
    {
        id: "0044",
        description: "Surfe",
        source: "https://web.codans.com.br/airbnb/img/icon/0044.jpg",
        url: "/surfe",
    },
    {
        id: "0045",
        description: "Dammusi",
        source: "https://web.codans.com.br/airbnb/img/icon/0045.jpg",
        url: "/dammusi",
    },
    {
        id: "0046",
        description: "Torres",
        source: "https://web.codans.com.br/airbnb/img/icon/0046.jpg",
        url: "/torres",
    },
    {
        id: "0047",
        description: "Hanoks",
        source: "https://web.codans.com.br/airbnb/img/icon/0047.jpg",
        url: "/hanoks",
    },
    {
        id: "0048",
        description: "Ryokans",
        source: "https://web.codans.com.br/airbnb/img/icon/0048.jpg",
        url: "/ryokans",
    },
    {
        id: "0049",
        description: "Espaços adaptados",
        source: "https://web.codans.com.br/airbnb/img/icon/0049.jpg",
        url: "/espacos-adaptados",
    },
    {
        id: "0050",
        description: "Casas cicládicas",
        source: "https://web.codans.com.br/airbnb/img/icon/0050.jpg",
        url: "/casas-cicladicas",
    },
    {
        id: "0051",
        description: "Trailers/motorhomes",
        source: "https://web.codans.com.br/airbnb/img/icon/0051.jpg",
        url: "/trailers-motorhomes",
    },
    {
        id: "0052",
        description: "Golfe",
        source: "https://web.codans.com.br/airbnb/img/icon/0052.jpg",
        url: "/golfe",
    },
    {
        id: "0053",
        description: "Esqui",
        source: "https://web.codans.com.br/airbnb/img/icon/0053.jpg",
        url: "/esqui",
    },
    {
        id: "0054",
        description: "Minsus",
        source: "https://web.codans.com.br/airbnb/img/icon/0054.jpg",
        url: "/minsus",
    },
    {
        id: "0055",
        description: "Casas cubanas",
        source: "https://web.codans.com.br/airbnb/img/icon/0055.jpg",
        url: "/casas-cubanas",
    },
    {
        id: "0056",
        description: "Cabanas de pastor",
        source: "https://web.codans.com.br/airbnb/img/icon/0056.jpg",
        url: "/cabanas-de-pastor",
    },
    {
        id: "0057",
        description: "Lurtas",
        source: "https://web.codans.com.br/airbnb/img/icon/0057.jpg",
        url: "/lurtas",
    },
    {
        id: "0058",
        description: "Na pista de esqui",
        source: "https://web.codans.com.br/airbnb/img/icon/0058.jpg",
        url: "/na-pista-de-esqui",
    },
    {
        id: "0059",
        description: "Pianos de cauda",
        source: "https://web.codans.com.br/airbnb/img/icon/0059.jpg",
        url: "/pianos-de-cauda",
    },
    {
        id: "0060",
        description: "Trulli",
        source: "https://web.codans.com.br/airbnb/img/icon/0060.jpg",
        url: "/trulli",
    },
    {
        id: "0061",
        description: "Praia",
        source: "https://web.codans.com.br/airbnb/img/icon/0061.jpg",
        url: "/praia",
    },
    {
        id: "0062",
        description: "Lago",
        source: "https://web.codans.com.br/airbnb/img/icon/0062.jpg",
        url: "/lago",
    },
];

const NavBar = () => {
    return (
        <div className="flex flex-row items-center">
            <Swiper
                spaceBetween={10}
                slidesPerView={3}
                breakpoints={{
                    640: { slidesPerView: 3 },
                    764: { slidesPerView: 4 },
                    1024: { slidesPerView: 6 },
                    1280: { slidesPerView: 9 },
                }}
            >
                {icons.map((icon, idx) => (
                    <SwiperSlide key={idx}>
                        <Link
                            href={icon.url}
                            className="flex flex-col items-center hover:text-red-500"
                        >
                            <Image
                                src={icon.source}
                                alt={icon.description}
                                width={24}
                                height={24}
                            />
                            <span>{icon.description}</span>
                        </Link>
                    </SwiperSlide>
                ))}
            </Swiper>
            <ButtonIcon
                icone={
                    <IconAdjustmentsHorizontal
                        aria-label="adjustaments icon"
                        size={20}
                    />
                }
            >
                {" "}
                Filtros
            </ButtonIcon>
        </div>
    );
};

export default NavBar;
