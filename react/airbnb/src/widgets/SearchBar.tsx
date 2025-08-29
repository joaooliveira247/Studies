import { IconSearch } from "@/assets/icons";

const SearchBar = () => {
    return (
        <div className="flex items-center rounded-full px-3 py-2 w-full max-w-2xl mx-auto border-2  border-gray-200 shadow-lg shadow-gray-200 overflow-clip">
            <input
                className="w-full focus:outline-none px-2"
                type="text"
                placeholder="Digite Sua Pesquisa"
            />
            <button className="bg-red-500 rounded-full p-2">
                <IconSearch aria-label="search" size={32} color="white" />
            </button>
        </div>
    );
};

export default SearchBar;
