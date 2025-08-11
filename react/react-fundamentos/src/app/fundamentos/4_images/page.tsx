

export default function Page() {

    const user = {
        name: "Anna",
        urlProfile: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    }

    return (
        <div>
            <h1>Image</h1>
            <img src={user.urlProfile} alt={`Name: ${user.name}`} style={{width:90, height:90}}/>
        </div>
    );
}