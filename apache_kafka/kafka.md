# <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/apachekafka/apachekafka-original.svg" width="25px"/> Apache Kafka

O Apache Kafka é uma plataforma distribuída de streaming de eventos que é usada para construir pipelines de dados em tempo real e aplicativos de streaming. Originalmente desenvolvido pela LinkedIn e depois doado à Apache Software Foundation, o Kafka é uma ferramenta essencial em arquiteturas de microsserviços, big data e processamento de dados em tempo real.

### Caracteristicas Gerais

- Os dados são publicados
um única vez

- Quem tem Interesse nos
dados “assina” e consome
só o que interessa

- Produtores e
Consumidores
desacoplados

- Podem trabalhar em
ritmos diferentes

- Consumidores podem ler
dados mais de uma vez

- Indisponibilidade do
Produtor não afeta o
processo

- Além disso, Kafka traz alto
disponibilidade e
capacidade com recursos
de cluster e
particionamento

#

> Definições
>
>[Clusters](./clusters.md)
>
>

## Principais Conceitos e Componentes do Kafka:

1. Tópicos (Topics):

    - Um tópico é uma categoria ou nome para onde as mensagens são enviadas. É similar a uma tabela em um banco de dados, mas no contexto de mensagens. Os dados são armazenados no Kafka como streams de eventos em tempo real e são organizados em tópicos.

2. Mensagens (Messages):

    - As mensagens são unidades de dados que contêm o payload (o conteúdo da mensagem) e metadados. As mensagens são escritas em tópicos por produtores e lidas por consumidores.

3. Produtores (Producers):

    - Os produtores são aplicativos que enviam (escrevem) dados para os tópicos no Kafka. Eles determinam em qual partição do tópico a mensagem será escrita, geralmente com base em uma chave associada à mensagem.

4. Consumidores (Consumers):

    - Os consumidores são aplicativos que leem dados dos tópicos do Kafka. Eles se inscrevem em um ou mais tópicos e processam os dados em tempo real.

5. Partições (Partitions):

    - Um tópico no Kafka pode ser dividido em várias partições. Cada partição é uma sequência ordenada e imutável de registros, e novas mensagens são adicionadas ao final da partição. Isso permite que as mensagens sejam processadas em paralelo, aumentando a escalabilidade.

6. Offset:

    - O offset é um identificador único para cada mensagem dentro de uma partição. Ele indica a posição da mensagem na partição, permitindo que os consumidores acompanhem quais mensagens foram processadas.

7. Brokers:

    - O Kafka é executado em uma ou mais instâncias conhecidas como brokers. Um cluster Kafka é composto por vários brokers que trabalham juntos para armazenar e distribuir dados.

8. Clusters:

    - Um cluster Kafka é um conjunto de brokers que trabalham juntos para fornecer alta disponibilidade e escalabilidade. As partições dos tópicos são replicadas entre diferentes brokers para garantir que os dados estejam seguros em caso de falha de um broker.

9. Zookeeper:

    - O Zookeeper é usado para gerenciar o estado do cluster Kafka, como a coordenação dos brokers, a atribuição de partições aos consumidores, e a liderança das partições. Embora o Kafka possa operar sem o Zookeeper em algumas configurações mais recentes, ele ainda é amplamente usado em arquiteturas tradicionais.

## Casos de Uso Comuns:

- Processamento de Dados em Tempo Real: Kafka é usado para capturar e processar fluxos de dados em tempo real, como logs de servidor, transações de banco de dados, e dados de sensores IoT.

- Pipelines de Dados: Kafka é frequentemente usado para construir pipelines de dados que movem e transformam dados entre diferentes sistemas de forma eficiente e escalável.

- Integração de Sistemas: Kafka permite que diferentes sistemas e serviços troquem dados de forma assíncrona e em tempo real, desacoplando as dependências entre eles.

- Arquitetura de Microsserviços: No contexto de microsserviços, Kafka pode atuar como um "backbone" para comunicação entre serviços, permitindo que eles sejam mais resilientes e escaláveis.

## Vantagens do Apache Kafka:

- Escalabilidade: Kafka pode lidar com grandes volumes de dados, escalando horizontalmente através da adição de mais brokers ao cluster.

- Desempenho: Kafka é altamente otimizado para throughput elevado, capaz de processar milhões de mensagens por segundo com baixa latência.

- Persistência: As mensagens no Kafka são persistidas em disco e podem ser armazenadas por um período configurável, permitindo reprocessamento e auditoria.

- Alta Disponibilidade: Kafka oferece replicação de dados entre brokers para garantir alta disponibilidade e tolerância a falhas.