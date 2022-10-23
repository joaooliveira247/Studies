# Factory Method

O Factory Method é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

- Aplicabilidade

    - **Use o Factory Method quando não souber de antemão os tipos e dependências exatas dos objetos com os quais seu código deve funcionar.**

        - O Factory Method separa o código de construção do produto do código que realmente usa o produto. Portanto, é mais fácil estender o código de construção do produto independentemente do restante do código.

        - Por exemplo, para adicionar um novo tipo de produto à aplicação, só será necessário criar uma nova subclasse criadora e substituir o método fábrica nela.

    - **Use o Factory Method quando desejar fornecer aos usuários da sua biblioteca ou framework uma maneira de estender seus componentes internos.**

        - Herança é provavelmente a maneira mais fácil de estender o comportamento padrão de uma biblioteca ou framework. Mas como o framework reconheceria que sua subclasse deve ser usada em vez de um componente padrão?

        - A solução é reduzir o código que constrói componentes no framework em um único método fábrica e permitir que qualquer pessoa sobrescreva esse método, além de estender o próprio componente.

        - Vamos ver como isso funcionaria. Imagine que você escreva uma aplicação usando um framework de UI de código aberto. Sua aplicação deve ter botões redondos, mas o framework fornece apenas botões quadrados. Você estende a classe padrão Botão com uma gloriosa subclasse BotãoRedondo. Mas agora você precisa informar à classe principal UIFramework para usar a nova subclasse no lugar do botão padrão.

        - Para conseguir isso, você cria uma subclasse UIComBotõesRedondos a partir de uma classe base do framework e sobrescreve seu método criarBotão. Enquanto este método retorna objetos Botão na classe base, você faz sua subclasse retornar objetos BotãoRedondo. Agora use a classe UIComBotõesRedondos no lugar de UIFramework. E é isso!

    - **Use o Factory Method quando deseja economizar recursos do sistema reutilizando objetos existentes em vez de recriá-los sempre.**

        - Você irá enfrentar essa necessidade ao lidar com objetos grandes e pesados, como conexões com bancos de dados, sistemas de arquivos e recursos de rede.

        - Vamos pensar no que deve ser feito para reutilizar um objeto existente:

            1. Primeiro, você precisa criar algum armazenamento para manter o controle de todos os objetos criados.

            2. Quando alguém solicita um objeto, o programa deve procurar um objeto livre dentro desse conjunto.

            3. ...e retorná-lo ao código cliente.

            4. Se não houver objetos livres, o programa deve criar um novo (e adicioná-lo ao conjunto de objetos).

        - Isso é muito código! E tudo deve ser colocado em um único local para que você não polua o programa com código duplicado.

        - Provavelmente, o lugar mais óbvio e conveniente onde esse código deve ficar é no construtor da classe cujos objetos estamos tentando reutilizar.
        
        - No entanto, um construtor deve sempre retornar novos objetos por definição. Não pode retornar instâncias existentes.

        - Portanto, você precisa ter um método regular capaz de criar novos objetos e reutilizar os existentes. Isso parece muito com um método fábrica.

- Vantagens: 

    - Você evita acoplamentos firmes entre o criador e os produtos concretos.

    - Princípio de responsabilidade única. Você pode mover o código de criação do produto para um único local do programa, facilitando a manutenção do código.

    - Princípio aberto/fechado. Você pode introduzir novos tipos de produtos no programa sem quebrar o código cliente existente.

- Desvantagens:

    - O código pode se tornar mais complicado, pois você precisa introduzir muitas subclasses novas para implementar o padrão. O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes criadoras.

![img_factory_method](./Factory%20Method.png)

`exemplo:`

[Factory Method](./factory_method.py)




