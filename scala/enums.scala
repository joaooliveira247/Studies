enum CrustSize:
    case Small, Medium, Large

enum CrustType:
    case Thin, Thick, Regular

enum Topping:
    case Cheese, Pepperoni, BlackOlives, GreenOlives, Onions

import CrustSize.*

@main def enums(): Unit =
    val currentCrustSize = Small

    currentCrustSize match
        case Small => println("Small crust size")
        case Medium => println("Medium crust size")
        case Large => println("Large crust size")
    
    if currentCrustSize == Small then println("Small crust size")


    
