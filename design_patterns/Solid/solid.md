# SOLID com Python

Sempre que falamos de qualidade de um software, é impossível não falar sobre utilização de boas práticas e padrões durante a sua construção e manutenção.

A partir dos vários princípios criados por Robert C. Martin para a programação orientada a objetos, Michael Feathers propôs o acrônimo S.O.L.I.D. para 5 princípios básicos que devem reger o processo de desenvolvimento de um software de qualidade.

A idéia é que estes princípios deveriam ser seguidos na programação durante todo o tempo de vida de um software. Com isso, evitamos possíveis problemas e também melhoramos a produtividade nas entregas, além de tornar o nosso código muito mais legível para outras pessoas.

<details>
    <summary>
        <a style="color:#04eaa6;">[S] INGLE RESPONSABILITY PRINCIPLE (SRP)</a>
    </summary>
<p>
Princípio da responsabilidade única: "Uma classe não pode ter mais de um motivo para ser alterada."

Sendo ainda mais específico, uma classe deve ter somente um motivo para ser alterada.

Muitas vezes precisamos de algum método ou de alguma propriedade e inserimos em uma determinada classe porque simplesmente não existe nenhum outro lugar melhor para colocá-lo. Com isso, estamos alterando o comportamento de uma classe que já havia sido definida para o que deveria fazer. Além de alterar o comportamento da classe, ainda estamos tornando ela ainda mais frágil (aumentando acoplamento e diminuindo a coesão).
</p>

`Por exemplo:`

```python3
class Quadrado:
    
    def __init__(self, comprimento_lado=0):
        self.comprimento_lado = comprimento_lado
    def calcula_area(self):
        return self.comprimento_lado ** 2
    def desenhar(self):
        # Desenha um quadrado
        pass
```

<p>
Dessa forma, podemos claramente ver que estamos atribuindo duas responsabilidades para a classe Quadrado, a de calcular a área e também desenhar o quadrado. Isso não está errado, porém se pensarmos no princípio de responsabilidade única, podemos ter duas classes, uma para calcular e outra para desenhar:
</p>

`Por exemplo:`

```python3
class CalculaQuadrado:
    def __init__(self, comprimento_lado=0):
        self.comprimento_lado = comprimento_lado
    def calcula_area(self):
        return self.comprimento_lado * 2
class DesenhaQuadrado:
    
    def desenha(self):
        # Desenha um quadrado
        pass

```

<p>
Assim, cada classe tem um único propósito: temos uma classe que podemos utilizar para cálculos geométricos e outra classe responsável por desenhos geométricos.
</p>

</details>

<details>
    <summary>
        <a style="color:#04eaa6;">[O] PEN/CLOSED PRINCIPLE (OCP)</a>
    </summary>
<p>
Princípio do aberto/fechado: "O comportamento de uma classe deve estar aberta para extensão porém fechada para alterações."

A principal idéia é que uma classe mãe deve ser genérica e abstrata para ser estendida e reaproveitada por classes filhas. Esse princípio rege que a classe mãe não deve ser alterada.

No Python podemos fazer uma operação conhecida como Monkey-Patching. Resumidamente, uma classe em Python é mutável e um método é apenas um atributo de uma classe. 
</p>

`Por exemplo:`

```python3
from abc import ABC
from datetime import datetime


class Cliente(ABC):
    nome: str
    sobrenome: str
    endereco: str
    create_at: datetime

class ClienteFisico(Cliente):
    cpf: str

class ClienteJuridico(Cliente):
    cnpj: str
```


</details>

<details>
    <summary>
        <a style="color:#04eaa6;">[L] ISKOV SUBSTITUTION PRINCIPLE (LSP)</a>
    </summary>

<p>
Princípio da substituição de Liskov: "Uma classe filha deve poder ser substituída pela suas classe pai."

Esse princípio define que uma subclasse deve poder ser substituída pela respectiva superclasse. E estas podem ser substituídas por qualquer uma das suas subclasses. Uma subclasse deve sobrescrever os métodos da superclasse de forma que a interface continue sempre a mesma.Princípio da substituição de Liskov: "Uma classe filha deve poder ser substituída pela suas classe pai."

Esse princípio define que uma subclasse deve poder ser substituída pela respectiva superclasse. E estas podem ser substituídas por qualquer uma das suas subclasses. Uma subclasse deve sobrescrever os métodos da superclasse de forma que a interface continue sempre a mesma.
</p>

`Por exemplo:`

```python3
class Animal:
    def make_noise(self) -> None:
        raise NotImplementedError("You have to implement make_noise")
    
    def move(self) -> None:
        raise NotImplementedError("You have to implement make_noise")

class Dog(Animal):
    def make_noise(self) -> None:
        print("au au")

class Cat(Animal):
    def make_noise(self) -> None:
        print("miau miau")
```

</details>

<details>
    <summary>
        <a style="color:#04eaa6;">[I] NTERFACE SEGREGATION PRINCIPLE (ISP)</a>
    </summary>

<p>
Princípio da segregação de interfaces: "Várias interfaces específicas são melhores do que uma interface genérica."

Este princípio define que uma classe não deve conhecer nem depender de métodos que não necessitam.

Já sabemos que para que uma classe seja coesa e reutilizável, ela não deve possuir mais de uma responsabilidade. Mas ainda assim, essa única responsabilidade pode ser quebrada em responsabilidades ainda menores, tornando a interface muito mais amigável.

No Python podemos fazer herança múltipla, então resolvi abstrair uma classe para calcular o volume de um polígono baseado em seu número de lados, uma para calcular a área também baseado em seu número de lados. Assim, eu conseguiria reutilizá-las para outros polígonos com quantidades de lados diferentes:
</p>

`Por exemplo, uma maneira não recomendada de fazer isso seria:
`

```python3
from abc import ABC, abstractclassmethod


class Cliente(ABC):
    @abstractclassmethod
    def get_cpf(self) -> None:
        pass
    
    @abstractclassmethod
    def get_cnpj(self) -> None:
        pass

class ClienteJuridico(Cliente):
    def get_cpf(self) -> None:
        pass

    def get_cnpj(self) -> None:
        pass

class Clientefisico(Cliente):
    def get_cpf(self) -> None:
        pass

    def get_cnpj(self) -> None:
        pass

```

<p>
Nesse caso as classes filhas são obrigadas a implementar os métodos da classe pai devido ao "contato" assinado com a classe pai por causa da AbstractClass, portanto o ideal seria quea as classes filhas n dependenssem da implementação de métodos indesejávei; Para isso a possibilidade de multipla herança do python é uma boa solução.
</p>

</details>

<details>
    <summary>
        <a style="color:#04eaa6;">[D] EPENDENCY INVERSION PRINCIPLE (DIP)</a>
    </summary>

<p>
Princípio da inversão de dependências: "Devemos depender de classes abstratas e não de classes concretas."

Esse princípio define que módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Ao mesmo tempo, estas abstrações não devem depender detalhes. Os detalhes é que devem depender de abstrações.

Legal, mas o que isso quer dizer?

Uma classe não deve conhecer outra classe para realizar alguma operação. Muito pelo contrário, deve existir uma interface genérica para intermediar esse acesso da forma mais abstrata possível.

Mas vamos concordar que em Python, geralmente nós não utilizamos interfaces para resolvermos problemas. No entanto, podem aparecer situações em que precisaremos definir uma interface, por exemplo em um contrato de uma API, na qual gostaríamos de estender alguma biblioteca ou framework. Para este caso, podemos contar com o módulo de Abstract Base Classes(ABC). E como o Python permite herança múltipla, as ABC's se comportam essencialmente como uma interface
</p>
</details>
