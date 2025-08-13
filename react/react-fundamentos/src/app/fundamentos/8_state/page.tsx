"use client";

import { useState } from "react";

export default function Page() {
    // let num = 0;

    let [num, setNum] = useState(0);
    function increment() {
        // num += 1;
        setNum(num + 1);
        console.log(num);
    }

    return (
        <div>
            <h1>States</h1>
            <button className="bg-blue-400 p-2" onClick={increment}>
                Click here
            </button>

            <p>Number: {num}</p>
        </div>
    );
}
