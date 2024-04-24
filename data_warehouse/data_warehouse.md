# <img src="https://cdn-icons-png.freepik.com/512/7787/7787808.png" width=20px> Data Warehouse

A data warehouse is a central repository for data which will be used for reporting and analytics. Data comes into the data warehouse from transactional systems, relational databases, or other sources usually on a regular cadence.

Business analysts, data engineers, data scientists, and decision makers then access the data through business intelligence tools, SQL clients, and other analytics applications. Because the primary use cases for a data warehouse revolve around analytics, they typically use an OLAP technology for performance.

![dw_ilustration](https://www.mistralbs.com/wp-content/uploads/2020/01/dwh-2.png)

|Advantages|Disvantages|
|:---:|:---:|
|Consolidate data from multiple data sources into one "source of truth"|A significant investment of time and resources to properly build|
|Optimized for read access which makes generating reports faster than using a source transaction system for reporting|Not designed for ingesting data in real-time (although they can typically handle near real-time)|
|Store and analyze large amounts of historical data
||

### When to use Data Warehouse

Data warehouses are made for complex queries on large datasets. You should consider a data warehouse if you're looking to keep your historical data separate from current transactions for performance reasons.

## Data Warehouse x Data Mart x Data Lake

![data_warehouse_lake](https://cdn-ajfbi.nitrocdn.com/GuYcnotRkcKfJXshTEEKnCZTOtUwxDnm/assets/images/optimized/rev-f88f631/datawarehouseinfo.com/wp-content/uploads/2018/09/DW-architecture.jpg)

|Concept|Description|
|:---:|:---:|
|Data Warehouse|A data warehouse stores data in a structured format. It is a central repository of preprocessed data for analytics and business intelligence.|
|Data Mart|A data mart is a data warehouse that serves the needs of a specific business unit, like a company’s finance, marketing, or sales department.|
|Data Lake|a data lake is a central repository for raw data and unstructured data. You can store data first and process it later on.|

### Similarities between data warehouses, data marts, and data lakes

Organizations today have access to ever-increasing volumes of data. However, they must sort, process, filter, and analyze the raw data to derive practical benefits. At the same time, they also have to follow rigid data protection and security practices for regulatory compliance. For example, here are practices organizations must follow:

- Collect data from different sources like applications, vendors, Internet of Things (IoT) sensors, and other third parties.


- Process data into a consistent, trustworthy, and useful format. For example, organizations could process data to make sure all dates in the system are in a common format or summarize daily reports.

- Prepare the data by formatting XML files for machine learning software or generating reports for humans.

Organizations use various tools and solutions to achieve their data analytics outcomes. Data warehouses, marts, and lakes are all solutions that help with storing data.

## Cloud Data warehouse

- Amazon Redshift
- Azure Synapse Analytcs
- Google BigQuery
- Microsoft SQL Server
- Snowflake
- AmazonS3 (DataLake)

## OLTP x OLAP

![oltpxolap](https://static.wixstatic.com/media/20d4f8_842daf80cd994c3e822ff370e3df0e96~mv2.gif)

Online analytical processing (OLAP) and online transaction processing (OLTP) are data processing systems that help you store and analyze business data. You can collect and store data from multiple sources such as websites, applications, smart meters, and internal systems. OLAP combines and groups the data so you can analyze it from different points of view. Conversely, OLTP stores and updates transactional data reliably and efficiently in high volumes. OLTP databases can be one among several data sources for an OLAP system.

|Criteria|OLAP|OLTP|
|:---:|:---:|:---:|
|Purpose|OLAP helps you analyze large volumes of data to support decision-making.|OLTP helps you manage and process real-time transactions.|
|Data source|OLAP uses historical and aggregated data from multiple sources.|OLTP uses real-time and transactional data from a single source.|
|Data structure|OLAP uses multidimensional (cubes) or relational databases.|OLTP uses relational databases.|
|Data model|OLAP uses star schema, snowflake schema, or other analytical models.|OLTP uses normalized or denormalized models.|
|Volume of data|OLAP has large storage requirements. Think terabytes (TB) and petabytes (PB).|OLTP has comparatively smaller storage requirements. Think gigabytes (GB).|
|Response time|OLAP has longer response times, typically in seconds or minutes.|OLTP has shorter response times, typically in milliseconds|
|Example applications|OLAP is good for analyzing trends, predicting customer behavior, and identifying profitability.|OLTP is good for processing payments, customer data management, and order processing.|

## Content:

[🗂️ Dimensional modeling](./dimensional_modeling.md)


## References:

https://aws.amazon.com/compare/the-difference-between-a-data-warehouse-data-lake-and-data-mart/

https://aws.amazon.com/compare/the-difference-between-olap-and-oltp/

https://dataengineering.wiki/Concepts/Data+Warehouse