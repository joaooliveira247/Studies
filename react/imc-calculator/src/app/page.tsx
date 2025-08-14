"use client";

import { useState } from "react";

export default function Home() {
    const [peso, setPeso] = useState("");

    const [altura, setAltura] = useState("");

    const [resultado, setResultado] = useState("");

    function calcIMC() {
        const p = parseFloat(peso);
        const a = parseFloat(altura);

        const imc = p / (a * a);

        if (imc <= 18) {
            setResultado(`${imc}: Abaixo do peso.`);
        } else if (imc > 18 && imc < 25) {
            setResultado(`${imc}: Peso Normal.`);
        } else {
            setResultado(`${imc}: Obesidade.`);
        }
    }

    return (
        <div>
            <h1>IMC Calculator</h1>
            <hr />

            <p>Digite seu peso</p>
            <input
                value={peso}
                onChange={(e) => setPeso(e.target.value)}
                type="number"
                placeholder="ex: 90"
                className="bg-gray-200 p-1 rounded-md"
            />
            <span>KG</span>
            <br />
            <p>Digite sua altura</p>
            <input
                value={altura}
                onChange={(e) => setAltura(e.target.value)}
                type="number"
                placeholder="ex: 1.80"
                className="bg-gray-200 p-1 rounded-md"
            />
            <span>Metros</span>
            <br />
            <button
                className="bg-blue-500 p-1 rounded-md text-white hover:bg-blue-400"
                onClick={calcIMC}
            >
                Calcular
            </button>
            <br />
            <span>Resulatado: {resultado}</span>
        </div>
    );
}
