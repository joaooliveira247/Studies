# 🗂️ Dimensional modeling

Dimensional modeling is a data modeling technique used in data warehousing that allows businesses to structure data to optimize analysis and reporting. This method involves organizing data into dimensions and facts, where dimensions are used to describe the data, and facts are used to quantify the data.

For instance, suppose a business wants to analyze sales data. In that case, the dimensions could include customers, products, regions, and time, while the facts could be the number of products sold, the total revenue generated, and the profit earned.

![dim_model](https://c8d86cee.rocketcdn.me/wp-content/uploads/2023/06/dimensional-data-modeling-facts-and-dimensions-data-sleek.png)

Data warehouses typically use a denormalized or star schema design rather than a normalized design. Normalization is a database design technique used to minimize redundancy and dependency by organizing data into tables and defining relationships between them.

In contrast, data warehouses often denormalize data for performance reasons. Denormalization involves combining tables and duplicating data to reduce the number of joins required to retrieve information, which can significantly improve query performance for analytical purposes

## ⭐ Star Model

The star schema is the simplest and most common dimensional modeling technique. In a star schema, the fact table is at the center and connected via foreign key(s) to the dimension tables. The fact table contains the numerical values or metrics being analyzed, while the dimension tables have the attributes that describe the data.

![star_model](https://iterationinsights.com/wp-content/uploads/2020/07/Star-Schema-Model.png)

The star schema is a straightforward and efficient method of dimensional modeling that is easy to understand and use. It is suitable for data warehouses that require fast and efficient queries.

## ❄️ Snowflake Model

The snowflake schema is a more complex dimensional modeling technique used when there are multiple levels of granularity within a dimension. In a snowflake schema, the dimension tables are normalized, meaning they are split into multiple tables to reduce data redundancy. This normalization results in a more complex schema that resembles a snowflake, hence the name.

![snowflake](https://assets-global.website-files.com/5e6f9b297ef3941db2593ba1/614df5d249f1d56f764083ef_Screenshot%202021-09-24%20at%2017.47.02.png)

For instance, the customer dimension table could be normalized in the sales data example to include separate tables for customer and address information.

The snowflake schema suits large, complex data warehouses requiring extensive data analysis and reporting. However, it can be more challenging to use and maintain than the star schema.

## Elements of Dimensional Data Model:

### Facts

Facts are the measurable data elements that represent the business metrics of interest. For example, in a sales data warehouse, the facts might include sales revenue, units sold, and profit margins. Each fact is associated with one or more dimensions, creating a relationship between the fact and the descriptive data.

### Dimension

Dimensions are the descriptive data elements that are used to categorize or classify the data. For example, in a sales data warehouse, the dimensions might include product, customer, time, and location. Each dimension is made up of a set of attributes that describe the dimension. For example, the product dimension might include attributes such as product name, product category, and product price.


### Attributes

Characteristics of dimension in data modeling are known as characteristics. These are used to filter, search facts, etc. For a dimension of location, attributes can be State, Country, Zipcode, etc.

### Fact Table

In a dimensional data model, the fact table is the central table that contains the measures or metrics of interest, surrounded by the dimension tables that describe the attributes of the measures. The dimension tables are related to the fact table through **foreign key relationships**

### Dimension Table

Dimensions of a fact are mentioned by the dimension table and they are basically joined by a **foreign key**. Dimension tables are simply de-normalized tables. The dimensions can be having one or more relationships.

## Content: 

### [Type of fact tables](/fact_tables.md)

### [Type of dimensional tables](./dim_tables.md)


## References:

https://data-sleek.com/blog/dimensional-data-modeling/