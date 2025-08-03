class FormHandler {
    createForm(): HTMLFormElement;
    createForm(inputs: string[]): HTMLFormElement;

    createForm(inputs?: string[]): HTMLFormElement {
        const form = document.createElement("form");

        if (inputs && inputs.length > 0) {
            inputs.map((value) => {
                const input = document.createElement("input");
                input.setAttribute("type", "text");
                input.setAttribute("placeholder", value);

                form.appendChild(input);
            });
        }
        document.body.appendChild(form);

        return form;
    }
}

const form = new FormHandler();
form.createForm();
