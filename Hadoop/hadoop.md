# <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/apache_hadoop_logo_icon_169586.png" width=25px> Hadoop

Hadoop é uma plataforma de software em Java de computação distribuída voltada para clusters e processamento de grandes volumes de dados, com atenção a tolerância a falhas

- plataforma escrita em Java

- Vem perdendo espaço para clouds.

- Usa o conceito de MapReduce

- Processamento em Batch(Pode demorar muito tempo)

### `MapReduce`

- Dividir tarefas de processamento de dados em vários nós(node)

    - Dados são divididos em blocos

    - Conceito de dividir para conquistar (um grande problema vira varios pequeno)

    - Foi criado em 2004 pela [Google](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)

    - Escalável

    - Tolerante a falhas

    - Disponibilidade

    - Confiável

    - Usa conceito key/value

    - Não cria gargalos na rede. pois dados não trafegam, são processados em nós

    - Mapeamento é executado em paralelo nos nós

    - Apenas quando o Map é Encerrado, reduce inicia em paralelo

    - Entre Map -> Reduce tem uma fase intermediaria chamada Shuffle phase in Hadoop transfers the map output from Mapper to a Reducer in MapReduce.

    - Existem tarefas que requerem apenas a etapa de Mapeamento.

### `HDFS`

Hadoop Distributed File System

- Arquivos separados em blocos

- Cópias replicadas(por padrão é replicada em 3 nós)

- Distribuidos em nós de redes

Hadoop aceita outros tipos de dados como:

|Data Type|Description|
|:---:|:---:|
|Text|Padrão em ferramentas como Hive|
|Sequence File|key/value binary|
|AVRO|Formato binário de serialização|
|*ORC|Colunas otimizado para consultar em linha|
|RC|Orientado a coluna, key/value|
|Parquet|Orientado a colunas Binário|

\* muito usado do Hadoop

## Vantagens e Desvantages

|Vantagens|Desvantagens|
|:---:|:---:|
|Grande volume de dados|Processamento real-time|
|Processamento em batch|Pequeno volume de dados|
||Problemas complexos(como uso de grafos)|
||Acesso interatico(ad-hoc) [Data visualisation] e Operações simples|
||Operações que demandam grande tráfego na rede|
||Problemas Transacionais|
||Requer o uso de java(Apesar de ter o Apache pig script)|

## Alternativas ao Hadoop

|Logo|Plataforma|
|:---:|:---:|
|<img src="https://www.vectorlogo.zone/logos/google_bigquery/google_bigquery-ar21.svg" width=100px>|Google BigQuery|
|<img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" width=100px>|Snowflake|
|<img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" width= 100px>|Apache Spark|


