# Abstract Factory

Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.
Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações.

- Aplicabilidade:

    - Use o Abstract Factory quando seu código precisa trabalhar com diversas famílias de produtos relacionados, mas que você não quer depender de classes concretas daqueles produtos-eles podem ser desconhecidos de antemão ou você simplesmente quer permitir uma futura escalabilidade.

    - O Abstract Factory fornece a você uma interface para a criação de objetos de cada classe das famílias de produtos. Desde que seu código crie objetos a partir dessa interface, você não precisará se preocupar em criar uma variante errada de um produto que não coincida com produtos já criados por sua aplicação.

        - Considere implementar o Abstract Factory quando você tem uma classe com um conjunto de métodos fábrica que desfoquem sua responsabilidade principal.

        - Em um programa bem desenvolvido cada classe é responsável por apenas uma coisa. Quando uma classe lida com múltiplos tipos de produto, pode valer a pena extrair seus métodos fábrica em uma classe fábrica solitária ou uma implementação plena do Abstract Factory.


| Vantagens|Desvantagens|
|:---:|:---:|
| - Você pode ter certeza que os produtos que você obtém de uma fábrica são compatíveis entre si.| - O código pode tornar-se mais complicado do que deveria ser, uma vez que muitas novas interfaces e classes são introduzidas junto com o padrão. |
|- Você evita um vínculo forte entre produtos concretos e o código cliente.||
|- Princípio de responsabilidade única. Você pode extrair o código de criação do produto para um lugar, fazendo o código ser de fácil manutenção.||
|- Princípio aberto/fechado. Você pode introduzir novas variantes de produtos sem quebrar o código cliente existente.||

![img_abstract_factory](./Abstract%20Factory.png)

`exemplo:`

[Abstract Factory](./abstract_factory.py)