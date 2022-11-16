# Template method

O Template Method é um padrão de projeto comportamental que define o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura.

Também é possível definir hooks para que as subclasses utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."

(IoC - Inversão de controle)

![template_ilustration](./template-method.png)

### Aplicabilidade

- Utilize o padrão Template Method quando você quer deixar os clientes estender apenas etapas particulares de um algoritmo, mas não todo o algoritmo e sua estrutura.

    - O Template Method permite que você transforme um algoritmo monolítico em uma série de etapas individuais que podem facilmente ser estendidas por subclasses enquanto ainda mantém intacta a estrutura definida em uma superclasse.

- Utilize o padrão quando você tem várias classes que contém algoritmos quase idênticos com algumas diferenças menores. Como resultado, você pode querer modificar todas as classes quando o algoritmo muda.

    - Quando você transforma tal algoritmo em um Template Method, você também pode erguer as etapas com implementações similares para dentro de uma superclasse, eliminando duplicação de código. Códigos que variam entre subclasses podem permanecer dentro das subclasses.

|Vantagens|Desvantagens|
|:---:|:---:|
|Você pode deixar clientes sobrescrever apenas certas partes de um algoritmo grande, tornando-os menos afetados por mudanças que acontece por outras partes do algoritmo.|Alguns clientes podem ser limitados ao fornecer o esqueleto de um algoritmo.|
|Você pode elevar o código duplicado para uma superclasse.|Você pode violar o princípio de substituição de Liskov ao suprimir uma etapa padrão de implementação através da subclasse.|
||Implementações do padrão Template Method tendem a ser mais difíceis de se manter quanto mais etapas eles tiverem.|

### Diagramas

![template_diagram](./Template%20Method.png)