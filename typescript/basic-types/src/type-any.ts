export function handleFileUpload(file: any) {
    console.log(`name: ${file.name}`);
}

const file = { name: "John" };

handleFileUpload(file);
