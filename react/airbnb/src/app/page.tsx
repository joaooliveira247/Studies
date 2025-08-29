import Header from "@/widgets/header";

export default function Home() {
    return (
        <div>
            <div>
                <Header />
            </div>
            <hr />
            <div className="border-green-500 border-2">Content</div>
            <div className="border-yellow-500 border-2">Footer</div>
        </div>
    );
}
