# Networks

Redes Docker são um componente crucial das capacidades de rede do Docker, permitindo que os containers se comuniquem entre si, com o sistema host e com redes externas.

`OBS`: Para usar o host de ponte use `host.docker.internal`

## Tipos de Redes Docker

### Rede Bridge

Rede padrão criada pelo Docker.
Adequada para containers independentes ou quando você deseja isolar um grupo de containers.

Containers na mesma rede bridge podem se comunicar entre si usando endereços IP ou nomes de containers.

Exemplo: `docker network create my-bridge-network`

### Rede Host

O container compartilha a pilha de rede e o endereço IP do host.
Não há isolamento entre a rede do host e a do container.

Útil para cenários onde o container precisa realizar operações de rede diretamente no host.

Exemplo: `docker run --network host my-container`

### Rede Overlay

Usada para redes Docker multi-host, tipicamente com Docker Swarm.

Permite que containers executados em diferentes hosts Docker se comuniquem de forma segura.

Útil para aplicações distribuídas e microsserviços.

Exemplo: `docker network create -d overlay my-overlay-network`

### Rede Macvlan


Atribui um endereço MAC a cada container, fazendo-o parecer como um dispositivo físico na rede.

Containers são conectados diretamente à rede física.

Útil para aplicações legadas que requerem acesso direto à rede.

Exemplo: `docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 my-macvlan-network`

### Rede None

Containers são completamente isolados de qualquer rede.

Útil quando você precisa de um ambiente altamente isolado.

Exemplo: `docker run --network none my-container`

## Gerenciamento de Redes Docker

### Criar uma Rede:

```sh
docker network create my-network
```

### Listar Redes:

```sh
docker network ls
```

### Inspecionar uma Rede:

```sh
docker network inspect my-network
```

### Conectar um Container a uma Rede:

```sh
docker network connect my-network my-container
```

### Desconectar um Container de uma Rede:

```sh
docker network disconnect my-network my-container
```

### Remover uma Rede:

```sh
docker network rm my-network
```

## Casos de Uso

### Rede Bridge:

- Isolamento de ambientes de desenvolvimento.

- Comunicação simples entre containers no mesmo host.

### Rede Host:

- Aplicações de alto desempenho que precisam de acesso direto à rede.

- Executar serviços de rede como DNS, DHCP, etc.

### Rede Overlay:


- Aplicações distribuídas em múltiplos hosts Docker.

- Arquitetura de microsserviços no Docker Swarm ou Kubernetes.

### Rede Macvlan:

- Otimização de desempenho de rede.
Executar serviços que requerem endereços MAC únicos.

### Rede None:

- Testes ou isolamento de segurança.
Executar aplicações que não requerem acesso à rede.






