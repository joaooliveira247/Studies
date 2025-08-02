interface Dog {
    type: "dog";
    bark: () => void;
}

interface Cat {
    type: "cat";
    meow: () => void;
}

type Pet = Dog | Cat;

function isDog(pet: Pet): pet is Dog {
    return pet.type === "dog";
}

function handlePet(pet: Pet) {
    if (isDog(pet)) {
        pet.bark();
    } else {
        pet.meow();
    }
}

const myPet: Pet = {
    type: "dog",
    bark: () => console.log("Woof!"),
};

handlePet(myPet);
