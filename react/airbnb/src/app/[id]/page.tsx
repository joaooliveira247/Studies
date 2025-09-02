import { fetchDataById } from "@/services/api";
import AccommodationDetails from "@/widgets/AccommodationDetails";
import AccommodationComments from "@/widgets/AccomodationComments";
import Footer from "@/widgets/Footer";
import Galeria from "@/widgets/galeria";
import Header from "@/widgets/header";
import SearchBar from "@/widgets/SearchBar";
import { notFound } from "next/navigation";

interface PageProps {
    id: string;
}

export default async function Page({
    params,
}: {
    params: Promise<PageProps>;
}) {
    const { id } = await params;
    const location = await fetchDataById(id);
    if (!location) {
        notFound();
    }
    return (
        <div>
            <header className="container mx-auto">
                <Header />
                <SearchBar />
            </header>
            <main className="container mx-auto py-6">
                <h1 className="text-3xl font-semibold pb-2">
                    {location.title}
                </h1>
                <Galeria fotos={location.photos} />
                <div className="flex flex-col md:flex-row">
                    <AccommodationDetails accommodation={location} />
                    <AccommodationComments accommodation={location} />
                </div>
            </main>
            <footer className="bg-gray-200">
                <Footer />
            </footer>
        </div>
    );
}
