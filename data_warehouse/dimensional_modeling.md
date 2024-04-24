# 🗂️ Dimensional modeling

Dimensional modeling is a data modeling technique used in data warehousing that allows businesses to structure data to optimize analysis and reporting. This method involves organizing data into dimensions and facts, where dimensions are used to describe the data, and facts are used to quantify the data.

For instance, suppose a business wants to analyze sales data. In that case, the dimensions could include customers, products, regions, and time, while the facts could be the number of products sold, the total revenue generated, and the profit earned.

![dim_model](https://c8d86cee.rocketcdn.me/wp-content/uploads/2023/06/dimensional-data-modeling-facts-and-dimensions-data-sleek.png)

Data warehouses typically use a denormalized or star schema design rather than a normalized design. Normalization is a database design technique used to minimize redundancy and dependency by organizing data into tables and defining relationships between them.

In contrast, data warehouses often denormalize data for performance reasons. Denormalization involves combining tables and duplicating data to reduce the number of joins required to retrieve information, which can significantly improve query performance for analytical purposes

## ⭐ Star Model

## ❄️ Snowflake Model

## References:

https://data-sleek.com/blog/dimensional-data-modeling/