type File = {
    readonly name: string;
    size: number;
};

const file: File = { name: "enterprises.txt", size: 1000 };

export function handleFileUpload(file: any) {
    console.log(`name: ${file.name}`);
}

handleFileUpload(file);
