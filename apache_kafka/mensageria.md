## O que são sistemas de mensageria

Um sistema de mensageria é uma infraestrutura de software que permite a comunicação entre diferentes partes de uma aplicação ou entre diferentes sistemas, enviando e recebendo mensagens de forma assíncrona. Ele é utilizado para desacoplar componentes de um sistema, permitindo que eles troquem informações de maneira eficiente e sem a necessidade de uma comunicação direta em tempo real.

### Principais Características:

- Desacoplamento: Componentes não precisam estar cientes uns dos outros ou estar ativos ao mesmo tempo para trocar mensagens.

- Assincronia: As mensagens podem ser enviadas e processadas em momentos diferentes, o que é ideal para sistemas distribuídos.

- Fiabilidade: Muitos sistemas de mensageria garantem a entrega das mensagens, mesmo em casos de falhas temporárias nos componentes envolvidos.

### Exemplos de Uso:

#### Integração de Microserviços:

Facilitando a comunicação entre diferentes serviços em uma arquitetura de microserviços.

#### Processamento de Tarefas em Background: 

Colocando tarefas em filas para serem processadas posteriormente, sem bloquear o fluxo principal da aplicação.

#### Streaming de Dados em Tempo Real: 
Enviando grandes volumes de dados de forma contínua para diferentes consumidores.


## Diferença entre Apache Kafka e RabbitMQ

Apache Kafka e RabbitMQ são duas das plataformas de mensageria mais populares, mas são projetadas para diferentes casos de uso e têm arquiteturas distintas. Abaixo, segue uma comparação entre Kafka e RabbitMQ:

### 1. Modelo de Mensageria
- **Kafka**: É um sistema de log distribuído e processador de streams, otimizado para o tratamento de grandes volumes de dados e processamento em tempo real. Kafka segue um modelo de **publicação/subscrição** (publish/subscribe), onde os produtores publicam mensagens em tópicos, e os consumidores assinam esses tópicos para receber as mensagens.
- **RabbitMQ**: É um message broker tradicional que implementa o protocolo AMQP (Advanced Message Queuing Protocol). RabbitMQ segue um modelo de **fila de mensagens**, onde os produtores enviam mensagens para filas, e os consumidores consomem essas mensagens. RabbitMQ também suporta o modelo publish/subscribe por meio de exchanges.

### 2. Arquitetura
- **Kafka**: Baseia-se em um log distribuído, onde as mensagens são armazenadas em partições dentro dos tópicos. Cada partição é uma sequência ordenada de registros e pode ser replicada para garantir a disponibilidade e tolerância a falhas. Kafka é ideal para o processamento de streams e para sistemas que necessitam de armazenamento e processamento de dados de forma contínua.
- **RabbitMQ**: Funciona como um broker de mensagens que roteia mensagens entre produtores e consumidores. Ele utiliza filas, exchanges, e bindings para definir como as mensagens devem ser roteadas. As mensagens em RabbitMQ geralmente são removidas da fila após serem consumidas, o que o torna ideal para sistemas onde as mensagens precisam ser processadas e descartadas rapidamente.

### 3. Persistência de Mensagens
- **Kafka**: As mensagens são persistidas no disco por um tempo configurável e não são excluídas após o consumo. Isso permite que múltiplos consumidores leiam as mesmas mensagens em momentos diferentes, o que é útil para reprocessamento de dados e auditorias.
- **RabbitMQ**: As mensagens são normalmente removidas da fila assim que são consumidas. Embora RabbitMQ suporte a persistência de mensagens, elas geralmente são tratadas como transientes e excluídas após o consumo, o que é mais adequado para sistemas onde a entrega única é essencial.

### 4. Escalabilidade
- **Kafka**: Altamente escalável devido à sua arquitetura de partições e réplicas. Kafka é projetado para manipular grandes volumes de dados com alta taxa de transferência, o que o torna ideal para sistemas de big data, como pipelines de ETL, coleta de logs, e streaming de eventos.
- **RabbitMQ**: Embora escalável, RabbitMQ foi projetado para casos de uso de menor escala em comparação com Kafka. Ele pode ser escalado verticalmente ou horizontalmente, mas sua arquitetura de filas não é tão eficiente quanto o particionamento de Kafka em cenários de altíssimo volume de mensagens.

### 5. Latência
- **Kafka**: Geralmente tem latências um pouco maiores devido ao seu design voltado para a persistência e tolerância a falhas. No entanto, Kafka é otimizado para throughput, o que é mais importante para muitos casos de uso em que grandes volumes de dados precisam ser processados rapidamente.
- **RabbitMQ**: É conhecido por sua baixa latência e é ideal para sistemas onde a velocidade de entrega de mensagens é crucial, como em sistemas de controle, notificação ou resposta em tempo real.

### 6. Casos de Uso
- **Kafka**: É utilizado principalmente para ingestão de dados em larga escala, processamento de streams em tempo real, e integração de grandes volumes de eventos, como logs de servidores, métricas, e eventos de sistemas distribuídos.
- **RabbitMQ**: É mais adequado para sistemas de enfileiramento de tarefas, comunicação entre microserviços, e casos onde a entrega garantida e ordenada de mensagens entre sistemas é necessária.

### 7. Complexidade de Gerenciamento
- **Kafka**: Requer mais esforço em termos de configuração e manutenção devido à sua arquitetura distribuída e à necessidade de gerenciar partições e réplicas. Porém, Kafka é altamente robusto e oferece recursos avançados de tolerância a falhas e recuperação.
- **RabbitMQ**: É mais simples de configurar e manter, especialmente para casos de uso de menor escala. RabbitMQ tem uma interface de administração amigável e um ecossistema rico de plugins e integrações.

### Resumo:
- **Kafka** é ideal para casos de uso que envolvem grandes volumes de dados, processamento em tempo real e onde a retenção de mensagens por um período prolongado é necessária.
- **RabbitMQ** é mais adequado para sistemas onde a entrega rápida e garantida de mensagens entre componentes é essencial, como em sistemas de microserviços ou em situações onde a latência muito baixa é um requisito.
