// Notação literal
const hotel = {
    rooms: 10,
    busy: 2,
    pools: 1,
    roomsAvailable: function(){return this.rooms - this.busy;}
}

hotel.rooms = 20;
hotel["rooms"] = 10;
delete hotel.pools; // return a bool

// Notação de Construtor

const hotel2 = new Object();
hotel2.rooms = 20;
console.log(hotel2)

// classes

class Hotel {
    constructor(rooms, busy, pools) {
        this.rooms = rooms;
        this.busy = busy;
        this.pools = pools;
    }

    roomsAvailable() {
        return this.rooms - this.busy;
    }
}

const hotel3 = new Hotel(9, 4, 1)
console.log(hotel3, hotel3.roomsAvailable())