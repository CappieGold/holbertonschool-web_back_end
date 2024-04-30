# NoSQL

## Learning Objectives

### 1. What NoSQL Means
NoSQL stands for "Not Only SQL" and refers to a category of database management systems that do not primarily use SQL for interacting with the database. NoSQL databases are designed to handle a wide variety of data models, including key-value, document, columnar, and graph formats. They are often chosen for their ability to scale out easily and are particularly effective for working with large sets of distributed data.

### 2. Difference Between SQL and NoSQL
- `Data Model`: SQL databases are primarily relational, storing data in tables and rows, and they require a predefined schema. NoSQL databases can store data in many ways (e.g., documents, key-value pairs, graphs) and typically do not require a fixed schema.
- `Scalability`: SQL databases are vertically scalable, meaning they are scaled by increasing the hardware specifications. NoSQL databases are horizontally scalable, meaning they scale by adding more servers into the pool.
- `Transactions`: SQL databases are often ACID-compliant, making them a better choice for applications that need reliable transactions. NoSQL databases may sacrifice ACID compliance for performance and scalability.

### 3. What is ACID
ACID stands for Atomicity, Consistency, Isolation, Durability. These are a set of properties that guarantee that database transactions are processed reliably:
- `Atomicity`: Ensures that each transaction is treated as a single unit, which either succeeds completely or fails completely.
- `Consistency`: Ensures that a transaction can only bring the database from one valid state to another, maintaining database invariants.
- `Isolation`: Ensures that concurrent execution of transactions leaves the database in the same state that would have been obtained if the transactions were executed sequentially.
- `Durability`: Ensures that once a transaction has been committed, it will remain so, even in the event of a system failure.

### 4. What is Document Storage
Document storage is a type of NoSQL database that stores data in the form of documents. These documents are usually in JSON or XML format, making them highly flexible as they can contain nested data and varying data types. MongoDB is a popular example of a document storage system.

### 5. Types of NoSQL Databases
- `Document Stores`: Data is stored in documents (MongoDB, CouchDB).
- `Key-Value Stores`: Data is stored in an array of key-value pairs (Redis, DynamoDB).
- `Column-Family Stores`: Data is stored in columns instead of rows and is efficient for reading and writing large volumes of data (Cassandra, HBase).
- `Graph Databases`: Data is stored in graph structures with nodes, edges, and properties to represent and store data (Neo4j, ArangoDB).

### 6. Benefits of a NoSQL Database
- `Flexibility`: No strict schema constraints.
- `Scalability`: Designed to scale out by using distributed and horizontal scaling.
- `High Performance`: Optimized for specific data models and access patterns.
- `Variety`: Handles varied data types like structured, semi-structured, and unstructured data.

### 7. How to Query Information from a NoSQL Database
Queries in NoSQL databases depend on the type:
- `Document Stores`: Use JSON-like queries (MongoDB uses find(), findOne()).
- `Key-Value Stores`: Query by the key.
- `Column-Family Stores`: Query by row and column identifiers.
- `Graph Databases`: Use graph-specific languages (e.g., Cypher in Neo4j).

### 8. How to Insert/Update/Delete Information from a NoSQL Database
In MongoDB:
- `Insert`: `db.collection.insertOne({item})` or `db.collection.insertMany([{item1}, {item2}])`.
- `Update`: `db.collection.updateOne({query}, {update})` or `db.collection.updateMany({query}, {update})`.
- `Delete`: `db.collection.deleteOne({query})` or `db.collection.deleteMany({query})`.

### 9. How to Use MongoDB
- `Setup`: Install MongoDB and set up the MongoDB server.
- `Connect`: Connect to the database using a MongoDB client.
- `Operations`: Perform CRUD operations using the MongoDB query language.

Each of these aspects of MongoDB and NoSQL databases opens up vast possibilities for managing and manipulating large-scale, diverse datasets in modern applications. If you need more detailed guidance on any specific operation or concept, feel free to ask!
