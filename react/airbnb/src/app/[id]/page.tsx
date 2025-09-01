interface PageProps {
    id: string;
}

export default async function Page({
    params,
}: {
    params: Promise<PageProps>;
}) {
    const data = await params;
    return <div>url: {data.id}</div>;
}
