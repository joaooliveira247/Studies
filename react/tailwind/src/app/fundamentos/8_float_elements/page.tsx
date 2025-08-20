import Image from "next/image";

export default function Float() {
    return (
        <div className="border p-3">
            <Image
                className="float-right"
                src="img/cidade"
                alt="desc"
                width={120}
                height={120}
            />

            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Cupiditate nobis ipsa doloremque aliquid sit! Eveniet magni
                fuga nobis vitae voluptatibus optio neque nostrum obcaecati
                alias temporibus modi, porro atque molestias.
            </p>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                Cupiditate nobis ipsa doloremque aliquid sit! Eveniet magni
                fuga nobis vitae voluptatibus optio neque nostrum obcaecati
                alias temporibus modi, porro atque molestias.
            </p>
        </div>
    );
}
