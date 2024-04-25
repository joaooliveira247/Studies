# Dimensional Tables

## Slowly Changing Dimension

These are the dimension tables that change slowly over time! Well if that does not make sense to you, then let me give you an example. The address of an individual is a great example of a slowly changing dimension, it does not change every day but it may change over time.

When you encounter any slowly changing dimensions next question to ask is if the business needs to store the history or not? If a business says yes, they need to store history then you need to ask the next question which is how much of history has to be stored. Based on the answer to these questions you will have to design your Slowly Changing Dimension (SCD) tables.

There are majorly 3 types of Slowly Changing Dimension tables.

### SCD Type 1

In this, no history is stored. If we take Address Dimension as an example then in that we do not store any address history of an individual. The dimension table consists of only the latest address of the individual.

This approach is easy to design and saves storage!

### SCD Type 2

This is the most commonly used type out of all these. In this approach complete history is maintained along with dates to identify from when to when the record is valid. They are usually called start_date and end_date. If the end date is empty then that means that is the active record!

In Address example, if John moves John moves from New York to Boston then Address Dimension would store from when to when John lived in New York and from when he started living in Boston.

This approach takes lots of storage.

### SCD Type 3

In this, only a limited history is stored. Let's say a business wants to keep only the current address and previous address of the individuals and they do not care to store all of the previous addresses.

This is usually achieved by adding additional columns to store the previous address. This approach falls in-between Type 1 and Type 2!

Compared to Type 2, this approach is easier to design and takes less storage space.

Now that we have dealt with the Elephant, let's look into the other Dimensions!!

## Conformed Dimension

A dimension that can be used by multiple facts and has the same meaning across the model is called a Confirmed Dimension.

For example, if we have a dimension for a list of places. This can be used across multiple fact tables.

## Degenerate Dimension

When a “fact” table stores dimensional values (not foreign keys to Dimensional tables) then we call it a degenerate dimension. Usually, if there are independent dimensional attributes then they are stored with the facts in fact tables. A typical example of this is Invoice number, though it is not a measure we often see it being stored in the Sales Fact table.

## Junk Dimension

If the model has too many small dimensions then all of them can be put into one dimension though each of those small dimensions is unrelated. This is called a Junk Dimension.

## Role Playing Dimension

A role-playing dimension consists of values that can be associated with multiple facts. For example, Sale location, Product Location, Person Location can all be related to a single Place Dimension but in changes in meaning based on the context. Another classic example of this is Date Dimension, it can be used in various fact tables with different contexts like Sale Date, Payment Date, etc. all linking to the same Date Dimension.

## Static Dimension

A static dimension usually never changes. Most often this would also mean that it is not driven by any of the source tables. Status Dimension, Gender Dimension is a good example of this.

## Shrunken Dimension

If a dimension can be further divided into a smaller dimension (Snowflake) then that is called a shrunken dimension.

## References:

https://en.wikipedia.org/wiki/Dimension_(data_warehouse)

https://abhimarichi.medium.com/types-of-dimension-tables-in-a-data-warehouse-bf6b48daf166