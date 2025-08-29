import Header from "@/widgets/header";
import SearchBar from "@/widgets/SearchBar";

export default function Home() {
    return (
        <div>
            <div>
                <Header />
                <SearchBar />
            </div>
            <hr className="mt-5" />
            <div className="border-green-500 border-2">Content</div>
            <div className="border-yellow-500 border-2">Footer</div>
        </div>
    );
}
