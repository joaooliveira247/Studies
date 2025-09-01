import { fetchData } from "@/services/api";
import Accommodations from "@/widgets/accommodation";
import Footer from "@/widgets/Footer";
import Header from "@/widgets/header";
import NavBar from "@/widgets/NavBar";
import SearchBar from "@/widgets/SearchBar";

export default async function Home() {
    const data = await fetchData();

    return (
        <div>
            <header className="container mx-auto">
                <Header />
                <SearchBar />
            </header>
            <hr className="my-6" />
            <main className="container mx-auto">
                <NavBar icons={data.icons} />
                <Accommodations accomodations={data.accommodation} />
            </main>
            <footer className="bg-gray-200">
                <Footer />
            </footer>
        </div>
    );
}
