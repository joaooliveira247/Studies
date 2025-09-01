import { AccommodationData, AirbnbApi } from "@/types/airbnbData";

export async function fetchData(): Promise<AirbnbApi> {
    try {
        const response = await fetch("https://web.codans.com.br/airbnb");
        const data = response.json();
        return data;
    } catch (e) {
        console.error(e);
        throw e;
    }
}
export async function fetchDataById(
    id: string
): Promise<AccommodationData | undefined> {
    try {
        const data = await fetchData();
        const accommodation = data.accommodation.find(
            (item: AccommodationData) => {
                return item.slug === id;
            }
        );
        return accommodation;
    } catch (e) {
        console.error(e);
        throw e;
    }
}
