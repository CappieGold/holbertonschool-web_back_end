# Pagination

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### 1. Paginating a Dataset with Simple page and page_size Parameters
This is the most straightforward method of pagination and is often used in many web applications. Here’s a basic outline of how it can be implemented:

#### Parameters:
- `page`: The current page number that the user is viewing.
- `page_size`: The number of items to display on a single page.
#### Backend Implementation:
- Calculate the starting point for the data retrieval (offset) as `(page - 1) * page_size`.
- Fetch the `page_size` number of items from the dataset starting from the offset.
#### Example in Python (using a hypothetical database query):
```bash
def get_paginated_items(page, page_size):
    offset = (page - 1) * page_size
    return database_query("SELECT * FROM items LIMIT %s OFFSET %s", (page_size, offset))
```

### 2. Paginating a Dataset with Hypermedia Metadata
When paginating with hypermedia controls, also known as HATEOAS (Hypermedia as the Engine of Application State), you include links in your API responses that lead to other pages of data. This approach can make your API more intuitive and easier to interact with. Here’s how to implement it:

#### Response Structure:
- Each response not only carries the data but also metadata with links to the first, previous, next, and last pages.
#### Example Response:
```bash
{
  "data": [...],  // the actual data being paginated
  "links": {
    "first": "https://api.example.com/items?page=1&page_size=10",
    "prev": "https://api.example.com/items?page=1&page_size=10",
    "next": "https://api.example.com/items?page=3&page_size=10",
    "last": "https://api.example.com/items?page=10&page_size=10"
  }
}
```

### 3. Pagination in a Deletion-Resilient Manner
Paginating through a dataset that might change (e.g., items being deleted) can be challenging because it can lead to skipping items or showing duplicates. To handle this, you might consider:

#### Using a Stable Identifier:
- Paginate based on a unique, stable identifier (like a timestamp or an auto-incrementing ID) that doesn't change even if items are deleted.
- Fetch items where the identifier is greater than the last identifier the user has seen.
#### Example:
- If you are paginating based on an id and the user last saw id=100, your query might be:
```bash
SELECT * FROM items WHERE id > 100 ORDER BY id ASC LIMIT 10
```

Implementing these pagination methods correctly ensures that your application scales effectively with large data volumes and provides a better user experience by loading data efficiently and reliably.
