// Procedural Paradigm
function roomsAvailable(rooms, busy) {
    return rooms - busy;
}

let rooms = 20;
let busy = 5;

console.log(roomsAvailable(rooms, busy))
// OO Paradigm
const hotel = {
    rooms: 10,
    busy: 2,
    roomsAvailable: function(){return this.rooms - this.busy;}
}

console.log(hotel.roomsAvailable())

