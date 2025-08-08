const userLogin = {
    userName: "John",
    permissions: ["User"],
};

function checkPermissions(requiredPermissions: string[]): MethodDecorator {
    return (target, propertyKey, descriptor) => {
        const hasPermission = requiredPermissions.some((permission) => {
            userLogin.permissions.includes(permission);
        });

        if (!hasPermission) {
            throw new Error("Invalid Permissions");
        }
        return descriptor;
    };
}

class ShoppingCart {
    @checkPermissions(["User", "Admin", "Super User"])
    getItems() {
        console.log("Items");
    }
}
