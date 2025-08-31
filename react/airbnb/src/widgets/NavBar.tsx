import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import ButtonIcon from "@/components/buttonIcon";
import { IconAdjustmentsHorizontal } from "@/assets/icons";

const NavBar = () => {
    return (
        <div className="flex flex-row items-center">
            <Swiper
                spaceBetween={10}
                slidesPerView={3}
                breakpoints={{
                    640: {slidesPerView: 3},
                    764: {slidesPerView: 4},
                    1024: {slidesPerView: 6},
                    1280: {slidesPerView: 9},
                }}
            ></Swiper>
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
