interface ButtonIconProps {
    icone: React.ReactNode;
    children: React.ReactNode;
}

const ButtonIcon = (props: ButtonIconProps) => {
    return (
        <>
            <button className="rounded-xl border-2 flex items-center p-2 px-4 py-2 hover:border-gray-400 gap-2">
                <span>{props.icone}</span>
                <span>{props.children}</span>
            </button>
        </>
    );
};

export default ButtonIcon;
