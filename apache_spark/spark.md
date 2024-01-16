# <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" width=50px> Spark

Apache Spark é um framework de código fonte aberto para computação distribuída. Foi desenvolvido no AMPLab da Universidade da Califórnia e posteriormente repassado para a Apache Software Foundation que o mantém desde então. Spark provê uma interface para programação de clusters com paralelismo e tolerância a falhas.

## Componentes do Spark

![spark_componentes](https://intellipaat.com/mediaFiles/2017/02/Components-of-Spark.jpg)

#### Spark SQL

- Permite ler dados tabulares de várias fontes (CSV, JSON, Parquet, OORC, ...)

- Sintaxe similar a SQL

#### Spark Streaming

- Dados estruturados

- Processamento de dados em "Real time"

#### MLib

- Componente para machine learning

#### GraphX

- Grafos acíclicos dirigidos

- Spark constroi grapos acíclicos dirigidos

- Estrutura de dados grafo com peso

### Elementos do Spark

- SparkSession: Seção (conexão ao Spark)

- Application: Programa


## Transformações e Ações

- Um data frame é imutável: trz tolerância a falhas

- Uma transformação gera um novo data frame

- O processamento de trasformação de fato só ocorre quando há uma Ação: Lazy Evaluation

## [Lazy Evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation#:~:text=In%20programming%20language%20theory%2C%20lazy,by%20the%20use%20of%20sharing\).)

Lazy Evaluation ou Call-by-need é um conjunto de regras que atrasa a atribuição de uma expressãop até que seu valor seja necessário e que também evita atribuições repetidas.

- Beneficios

    - definir fluxo de controle como abstração ao inves de primitivos.

    - definir estruturas de dados infinitas, isso permite a implementação mais direta de alguns algoritmos

    - definir estruturas de dados parcialmente definidas onde alguns elementos são erros. Isso permite uma prototipagem rápida.

No Spark o processo  só é definido quando uma "ação" é feita.

`Filter(Transformação) -> Union(Transformação) -> Sample(Transformação) -> Show(Ação)`

|Transformações|Ações|
|:---:|:---:|
|map|reduce|
|filter|collect|
|flatMap|count|
|mapPartitions|first|
|mapPartitionsWithIndex|take|
|sample|takeSample|
|union|takeOrdered|
|intersection|saveAsTextFile|
|distinct|saveAsSequenceFile|
|groupByKey|saveAsObjectFile|
|reduceByKey|countByKey|
|agregateByKey|foreach|
|sortByKey||
|join||
|cogroup||
|cartesian||
|pipe||
|coalesce||
|repartiotion||
|repartiotionAndSortWithinPartitions||

## API's

[Spark Scala API (Scaladoc)](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html)

[Spark Java API (Javadoc)](https://spark.apache.org/docs/latest/api/java/index.html)

[Spark Python API (Sphinx)](https://spark.apache.org/docs/latest/api/python/index.html)

[Spark R API (Roxygen2)](https://spark.apache.org/docs/latest/api/R/index.html)

[Spark SQL, Built-in Functions (MkDocs)](https://spark.apache.org/docs/latest/api/sql/index.html)

## Cloud

- AWS(EMR)

- Azure(HDInsight)

- Databricks

Também é possilvel instalar em servidores cloud e usar a Api.

O google fornece o google colab onde é possivel usar o Spark


## <img src="https://cdn.icon-icons.com/icons2/2699/PNG/512/databricks_logo_icon_170295.png" width=25px> Databricks

A Databricks é uma empresa americana de software fundada pelos criadores do Apache Spark. A Databricks desenvolve uma plataforma baseada na web para trabalhar com o Spark, que fornece gerenciamento automatizado de cluster e notebooks no estilo IPython.

Além disso, a plataforma também possui recursos para construção de pipelines, permitindo que os usuários processem dados em etapas e visualizem os resultados em tempo real. Em resumo, o Databricks é uma plataforma de processamento de dados flexível e eficiente que oferece uma variedade de ferramentas para ajudar as empresas a processar e analisar dados

### Suporte

- Python

- R

- SQL

### O workspace do Databricks fornece uma interface e ferramentas unificadas para a maioria das tarefas de dados, incluindo:

- Programação e gerenciamento de fluxos de trabalho de processamento de dados

- Gerando dashboards e visualizações

- Gerenciando segurança, governança, alta disponibilidade e recuperação de desastres

- Descoberta, anotação e exploração de dados

- Modelagem de aprendizado de máquina (ML), acompanhamento e modelo de atividade

- Soluções de IA generativa



