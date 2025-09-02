import { IconStarFilled } from "@/assets/icons";
import { AccommodationData } from "@/types/airbnbData";
import Image from "next/image";

interface AccommodationProps {
    accommodation: AccommodationData;
}

const AccommodationComments = (props: AccommodationProps) => {
    const comments = props.accommodation.testimonilas;
    return (
        <div className="w-full py-4">
            <h2 className="text-xl font-semibold">Depoimentos</h2>
            <div className="flex gap-2 items-center">
                <IconStarFilled className="size-4" />
                <span>4.9 (400+ avaliações)</span>
            </div>

            {comments.map((comment, idx) => (
                <div key={idx} className="flex items-center gap-4 py-4">
                    <Image
                        className="aspect-square object-cover rounded-full"
                        src={comment.image}
                        alt={`${comment.name} photo`}
                        width={48}
                        height={48}
                    />
                    <div>
                        <span className="font-semibold">{comment.name}</span>
                        <p>{comment.comment}</p>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default AccommodationComments;
