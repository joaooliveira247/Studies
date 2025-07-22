class Product {

}

const prod = new Product

const Hotel = function() {
    this.name = "SomeHotel";
    this.rooms = 12;
    let busy = 4; // it will be "private" now
    this.pools = 1;

    this.booking = function(){

        if (busy < this.rooms) {
            busy++
            return;
        }
        console.log("This hotel has no empty rooms.")
    }
}

console.log(typeof prod)