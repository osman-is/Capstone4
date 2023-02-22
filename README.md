Capstone 4 project -- OOP

This is a description of the fourth HyperionDev Capstone Project which involves creating an inventory management program for Nike warehouses.

Menu
---------------------------------------------------------------------------------------------------------------------------------------------------

a - Add a new shoe to the inventory list

v - View data about every shoe in the inventory list

r - Restock the lowest quantity shoe in the inventory list

s - Search for a shoe by product code

c - Show the value per shoe (cost*quantity) for each shoe in the inventory list

p - Print an 'on sale' notice for the product with the highest quantity

e - exits the program


Functions
-----------------------------------------------------------------------------------------------------------------------------------------------------
Read Shoe data

If the user wants to read the data from the inventory.txt file they will have to type view data from the menu then this will iterate through the file to make a list of shoe objects.

Capture Shoes

When the user selects 'a', they are prompted to provide information about a new shoe. This information includes:

Country of origin

Product code (which must be entered as SKUXXXX where X is a digit from 0-9), Product name, Cost and the Quantity

View All

If the user selects 'v', the shoes list is iterated through and printed as a tabulate table for ease of reading.

Restock

If the user selects 'r', allows the user to increase the amount of stock of the lowest quantity shoe by a certain amount.

Search

If the user selects 's', allows the user to search for a shoe by its product code.

Value Per Shoe

If the user selects 'c', allows the user to see the value per shoe, calculated by the following:

Exit

if the user selects 'e' they exit the program
