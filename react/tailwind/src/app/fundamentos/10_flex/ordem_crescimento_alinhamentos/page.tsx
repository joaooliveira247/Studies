export default function Application() {
    return (
        <div className="flex border p-3 flex-row flex-wrap">
            <div className="box order-1">Box 1</div>
            <div className="box grow">Box 2</div>
            <div className="box order-3">Box 3</div>
            <div className="box">Box 4</div>
        </div>
    );
}
