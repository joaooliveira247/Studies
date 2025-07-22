class Product {

}

const prod = new Product

const Hotel = function() {
    this.name = "SomeHotel";
    this.rooms = 12;
    this.busy = 4;
    this.pools = 1;

    this.booking = function(){
        this.busy++
    }
}

console.log(typeof prod)