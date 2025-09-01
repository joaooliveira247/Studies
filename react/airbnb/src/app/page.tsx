import Accommodations from "@/widgets/accommodation";
import Footer from "@/widgets/Footer";
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
            <hr className="my-6" />
            <main className="container mx-auto">
                <NavBar />
                <Accommodations />
            </main>
            <footer className="bg-gray-200">
                <Footer />
            </footer>
        </div>
    );
}
