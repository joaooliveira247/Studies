"use client";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import ButtonIcon from "@/components/buttonIcon";
import { IconAdjustmentsHorizontal } from "@/assets/icons";
import Link from "next/link";
import Image from "next/image";
import { Icon } from "@/types/airbnbData";

interface NavBarProps {
    icons: Icon[];
}

const NavBar = (props: NavBarProps) => {
    const icons = props.icons;
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
                            <span className="text-sm">{icon.description}</span>
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
