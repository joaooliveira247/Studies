export interface AirbnbApi {
    accommodation: AccommodationData[];
    icons: Icon[];
}

export interface AccommodationData {
    id: string;
    title: string;
    date: string;
    testimonilas: Testimonials[];
    hasBadge: boolean;
    host: string;
    slug: string;
    location: Location;
    price: number;
    rating: number;
    photos: Photo[];
}

export interface Testimonials {
    id: string;
    name: string;
    image: string;
    comment: string;
    rating: number;
    customerTime: number;
    createdAt: number;
    stayedAt: number;
}

export interface Location {
    description: string;
    city: string;
    state: string;
    country: string;
}

export interface Photo {
    id: string;
    source: string;
    description: string;
}

export interface Icon {
    id: string;
    description: string;
    source: string;
    url: string;
}
