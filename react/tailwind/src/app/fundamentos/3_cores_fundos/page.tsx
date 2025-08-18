export default function Colors() {
    return (
        <div>
            <h1 className="text-orange-300/50">Colors</h1>
            <h1 className="text-[#50d71e]">Color-hex</h1>

            <button className="bg-orange-600 hover:bg-amber-300"></button>
            <button className="bg-[#50d71e] hover:bg-amber-300"></button>
            {/* bg-[url(/img/cidade.jpg)] bg-bottom */}
            <h1 className="h-96 bg-[url(/img/nuvem.png)] bg-repeat-x">
                background image
            </h1>
        </div>
    );
}
