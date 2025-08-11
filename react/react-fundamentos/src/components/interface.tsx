export function Acomodacao() {
    return (
        <div>
            <span>Image</span>
            <h1>Hello</h1>
            <p>desc</p>
        </div>
    );
}

export function Button() {
    return (
        <button>Common Button</button>
    );
}

function Menu() {
    return (
        <div className="bg-yellow-500">
            Acomodações | Experiências
        </div>
    );
}

export function Header() {
    return (
        <div className="bg-blue-700">
            <h1>
                Logo
            </h1>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quos eum ipsa, commodi quidem animi nemo velit quis magnam magni alias! Exercitationem mollitia iure praesentium amet, rem officia perspiciatis ab! Odit!</p>
            {Menu()}
        </div>
    );
}
