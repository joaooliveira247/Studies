# Composite

O Composite é um padrão de projeto estrutural que permite que você componha objetos em estruturas de árvores e então trabalhe com essas estruturas como se elas fossem objetos individuais.

![composite_ilustration](./composite.png)

### Aplicabilidade

- Utilize o padrão Composite quando você tem que implementar uma estrutura de objetos tipo árvore.

    - O padrão Composite fornece a você com dois tipos básicos de elementos que compartilham uma interface comum: folhas simples e contêineres complexos. Um contêiner pode ser composto tanto de folhas como por outros contêineres. Isso permite a você construir uma estrutura de objetos recursiva aninhada que se assemelha a uma árvore.

- Utilize o padrão quando você quer que o código cliente trate tanto os objetos simples como os compostos de forma uniforme.

    - Todos os elementos definidos pelo padrão Composite compartilham uma interface comum. Usando essa interface o cliente não precisa se preocupar com a classe concreta dos objetos com os quais está trabalhando.

|Vantagens|Desvantages|
|:---:|:---:|
|Você pode trabalhar com estruturas de árvore complexas mais convenientemente: utilize o polimorfismo e a recursão a seu favor.|Pode ser difícil providenciar uma interface comum para classes cuja funcionalidade difere muito. Em certos cenários, você precisaria generalizar muito a interface componente, fazendo dela uma interface de difícil compreensão.|
|Princípio aberto/fechado. Você pode introduzir novos tipos de elemento na aplicação sem quebrar o código existente, o que agora funciona com a árvore de objetos.||

### Diagrama

![composite_diagram](./Composite_diagram.png)

![BST](./BST.png)