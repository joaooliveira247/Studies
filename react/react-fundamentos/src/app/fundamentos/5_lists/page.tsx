export default function Page(){

    const names: {id: number, firstName: string, email: string}[] = [
        {id: 1, firstName: "John", email:"j@email.com"},
        {id: 2, firstName: "Mariah", email: "m@gmail.com"}
    ];

    const list = names.map(
        user =>  <li key={user.id}>{user.firstName}  ( {user.email} )</li>
    );

    return (
        <ul>
            {list}
        </ul>
    );
}