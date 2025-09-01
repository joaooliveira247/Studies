import Footer from "@/widgets/Footer";
import Header from "@/widgets/header";
import SearchBar from "@/widgets/SearchBar";

interface PageProps {
    id: string;
}

export default async function Page({
    params,
}: {
    params: Promise<PageProps>;
}) {
    const data = await params;
    return (
        <div>
            <header className="container mx-auto">
                <Header />
                <SearchBar />
            </header>
            <main className="container mx-auto py-6">
                <h1 className="text-3xl">Rancho da lua</h1>
            </main>
            <footer className="bg-gray-200">
                <Footer />
            </footer>
        </div>
    );
}
