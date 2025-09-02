import {
    IconPhoto,
    IconToolsKitchen2,
    IconDesk,
    IconPool,
    IconBrandCarbon,
    IconSailboat,
    IconWifi,
    IconParking,
    IconAlarmSmoke,
    IconDog,
} from "@/assets/icons";
import { AccommodationData } from "@/types/airbnbData";

interface AccommodationDetailProps {
    accommodation: AccommodationData;
}

const AccommodationDetails = (props: AccommodationDetailProps) => {
    const accommodation = props.accommodation;

    return (
        <div className="w-full py-4">
            <h2 className="text-xl font-semibold">
                {accommodation.location.description}
            </h2>
            <ul className="flex flex-row gap-2">
                <li>10 Hóspedes</li>
                <li>&middot;</li>
                <li>5 Quartos</li>
                <li>&middot;</li>
                <li>5 Camas</li>
                <li>&middot;</li>
                <li>5 Banheiros</li>
            </ul>

            <h2 className=" pt-4 text-xl font-semibold">
                O que este lugar oferece ?
            </h2>

            <ul className="py-6 grid grid-cols-2 items-center gap-y-6">
                <li className="flex gap-1.5">
                    <IconPhoto />
                    <span>Vista para as montanhas</span>
                </li>
                <li className="flex gap-1.5">
                    <IconToolsKitchen2 />
                    <span>Cozinha</span>
                </li>
                <li className="flex gap-1.5">
                    <IconDesk />
                    <span>Espaço de trabalho exclusivo</span>
                </li>
                <li className="flex gap-1.5">
                    <IconPool />
                    <span>Piscina privatica</span>
                </li>
                <li className="flex gap-1.5">
                    <IconAlarmSmoke />
                    <span>Alarme de segurança p/ gás</span>
                </li>
                <li className="flex gap-1.5">
                    <IconSailboat />
                    <span>Vista para as águas</span>
                </li>
                <li className="flex gap-1.5">
                    <IconWifi />
                    <span>Wi-Fi rápido (83 Mbps)</span>
                </li>
                <li className="flex gap-1.5">
                    <IconParking />
                    <span>Estacionamento incluído</span>
                </li>
                <li className="flex gap-1.5">
                    <IconDog />
                    <span>Permitido animais</span>
                </li>{" "}
                <li className="flex gap-1.5">
                    <IconBrandCarbon />
                    <span>Detector de fumaças</span>
                </li>
            </ul>
        </div>
    );
};

export default AccommodationDetails;
