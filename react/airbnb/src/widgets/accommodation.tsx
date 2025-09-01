import Image from "next/image";
import Accommodation from "@/components/accommodation";
import Link from "next/link";
import { AccommodationData } from "@/types/airbnbData";

interface AccommodationsProps {
    accomodations: AccommodationData[];
}

const Accommodations = (props: AccommodationsProps) => {
    const locations = props.accomodations;
    return (
        <section className="py-6 grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {locations.map((location, idx) => (
                <div key={idx}>
                    <Link href={location.slug}>
                        <Accommodation
                            local={location.location.description}
                            anfitriao={location.host}
                            date={location.date}
                            price={location.price}
                            avaliacao={location.rating}
                            preferidoHospede={location.hasBadge}
                        >
                            <Image
                                className="w-full aspect-square object-cover rounded-xl"
                                src={location.photos[0].source}
                                alt={location.photos[0].description}
                                width={300}
                                height={300}
                            />
                        </Accommodation>
                    </Link>
                </div>
            ))}
        </section>
    );
};

export default Accommodations;
