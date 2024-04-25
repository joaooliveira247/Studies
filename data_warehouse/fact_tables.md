# Fact tables

## Transaction
A transaction fact table or transaction fact entity records one row per transaction.

A Transaction table is the most basic and fundamental view of business operations. These fact tables represent an event that occurred at an instantaneous point in time. A row exists in the fact table for a given customer or product only if a transaction has occurred.

so, let’s take an example:

if you have a shop or supermarket, you will use the transaction fact table to record each transaction happened over the day, if you have 100 customers purchased over the day, you will have 100 records at transaction fact table.


![transactio](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*bpbjXZs895P9V9gJ3X6blQ.png)

## Periodic
A periodic fact table or periodic fact entity stores one row for a group of transactions that happen over a period of time.

so, let’s take an example:

if you have a shop or supermarket, ang you have only three categories, let’s say bike, car and bicycle, you will use the periodic fact table if you want to know like what the total sales of each category over month or week or quarter is.

![periodic](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*HJnpQXePqDhJc18bz4XwIA.png)

## Accumulating
An accumulating fact table or accumulating fact entity stores one row for the entire lifetime of an event. An example of an accumulating fact table or entity records is the timeline of the hiring process at any company , we all know that the hiring process have many stages and every stage have it’s time , let’s say we have three stages A , B and C , A takes 3 days , B takes 6 days and A takes 2 days , so you will use the accumulating fact table if you want to know the whole time of an process.

![acc_1](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*Y2U9-li-toWJGE6vGgHQ_g.png)

![acc_2](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*EkXvlUrJBieU3o9xbPc3Qg.png)

## Aggregate

Aggregate fact tables are simple numeric rollups of atomic fact table data built solely to accelerate query performance. These aggregate fact tables should be available to the BI layer at the same time as the atomic fact tables so that BI tools smoothly choose the appropriate aggregate level at query time. This process, known as aggregate navigation, must be open so that every report writer, query tool, and BI application harvests the same performance beneﬁts. A properly designed set of aggregates should behave like database indexes, which accelerate query performance but are not encountered directly by the BI applications or business users. Aggregate fact tables contain foreign keys to shrunken conformed dimensions, as well as aggregated facts created by summing measures from more atomic fact tables. Finally, aggregate OLAP cubes with summarized measures are frequently built in the same way as relational aggregates, but the OLAP cubes are meant to be accessed directly by the business users.
## References:

https://medium.com/@mohamad.ashour203/fact-table-definition-and-its-types-in-data-warehousing-with-examples-4fa89cc53dee

https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/aggregate-fact-table-cube/

https://en.wikipedia.org/wiki/Fact_table

https://www.geeksforgeeks.org/factless-fact-table/?ref=header_search