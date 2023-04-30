## Overview

The system should allow store managers to add, update and remove products from the inventory, as well as track their stock levels. The system should also allow customers to view the inventory and place orders. The system should be flexible to handle multiple types of products and provide different ways to calculate the stock levels. To achieve this goal, we will use the following design patterns:

* Strategy pattern: to implement different strategies for calculating the stock levels of products.
* Observer pattern: to notify the store manager and customers when the inventory is updated.
* Command pattern: to encapsulate requests from customers to place orders.

## Decomposition of the task

1. Define the Product class with attributes such as id, name, price, and stock level. Implement a factory pattern to create different types of products.
2. Implement a strategy pattern to provide different algorithms for calculating the stock level of products. Implement two strategies: based on the number of units in stock and based on the total value of the stock.
3. Define the Inventory class with methods to add, update, and remove products from the inventory. The Inventory class should be implemented using the singleton pattern to ensure that there is only one instance of the inventory in the system.
4. Implement the observer pattern to notify the store manager and customers when the inventory is updated.
5. Define the Order class with attributes such as id, product, quantity, and customer information. Implement the command pattern to encapsulate requests from customers to place orders.
6. Implement a Customer class with attributes such as id, name, and address. The Customer class should be able to place orders and view the inventory.
7. Implement a StoreManager class with attributes such as id, name, and email. The StoreManager class should be able to add, update, and remove products from the inventory and receive notifications when the inventory is updated.
