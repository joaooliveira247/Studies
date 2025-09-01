import Accommodation from "@/widgets/accommodation";
import Header from "@/widgets/header";
import NavBar from "@/widgets/NavBar";
import SearchBar from "@/widgets/SearchBar";

export default function Home() {
    return (
        <div>
            <header className="container mx-auto">
                <Header />
                <SearchBar />
            </header>
            <hr className="my-3" />
            <main className="container mx-auto">
                <NavBar />
                <Accommodation />
            </main>
            <div className="border-green-500 border-2">Content</div>
            <footer className="border-purple-500 border-2">footer</footer>
        </div>
    );
}
