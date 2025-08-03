interface VehicleInterface {
    type: string;
    description(): string;
}

abstract class VehicleAbstract {
    protected readonly type: string;
    constructor(type: string) {
        this.type = type;
    }
    abstract description(): string;
}

// interfaces são implementadas, n interfaces
class BycycleWithInterface implements VehicleInterface {
    public readonly type: string;
    constructor(type: string) {
        this.type = type;
    }
    description(): string {
        return `${this.type}`;
    }
}

// classes abstratas são extendidas 1 só
class BycycleWithClass extends VehicleAbstract {
    constructor(protected readonly type: string) {
        super(type);
    }
    description(): string {
        return `${this.type}`;
    }
}
