from tabulate import tabulate

# The following program will read from inventory.txt file and is designed to assist with stock take.

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
       
        return (self.cost)
      

    def get_quantity(self):
       
        return (self.quantity)
       

    def __str__(self):

        return (
            f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
            )
      


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt and read the data from this file,
    then create a shoes object with this data and append this object into the shoes list.  
    '''
    # Here we use the try-except in this function for error handling. 
    try:

        with open ("inventory.txt", "r") as file:
            file = file.readlines()
        for line in file:
            # Here we will skip the first line as it is the title
            if file.index(line) == 0:
                pass
            elif file.index(line) > 0:
                country, code, product, cost, quantity = line.strip().split(",")

                shoe = Shoe(country, code, product, cost, quantity)
                # The line above represents data to create one object of shoes.
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File does not exist! Please try again")
        

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    country = input("Please enter what country the product is from: ")
    code = input("Please enter the product code: ")
    product = input("Please enter the product name: ")
    cost = int(input("Please enter the cost of the product: "))
    quantity = int(input("Please enter the quantity of the product: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    table_list = [["Country", "Code", "Product", "Cost", "Quantity"]]
    for shoe in shoe_list:
        lst1 = shoe.__str__().strip().split(",")
        table_list.append(lst1)
    # Here we use the tabulate module to display the data
    print(tabulate(table_list, headers="firstrow", tablefmt="fancy_grid"))

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked.
    '''
    f = open("inventory.txt", "r")
    lines = f.readlines()
    shoe_dict = {}
    for shoe in shoe_list:
        lst1 = shoe.__str__().strip().split(",")
        shoe_dict[lst1[2]] = shoe.get_quantity()
    lowest = min(shoe_dict.values())

# We will ask the user if they want to add this quantity of shoes and then update it.
    for key, value in shoe_dict.items():
        if value == lowest:
            restock_num = int(input(f"{key}'s are low in stock, how much stock would you like to add? "))

# This quantity should be updated on the file for this shoe.
    writer = open("inventory.txt", "w")
    for line in lines:
        split_line = line.strip().split(",")
        if split_line[-1].strip() == str(lowest).strip():

            split_line[-1] = f"{str(restock_num)}\n"
            edited_line = ",".join(split_line)
            lines[lines.index(line)] = edited_line
            writer.writelines(lines)
            print("WRITTEN")
            writer.close()


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
  

    search_query = input("Please enter the shoe code: ").upper()

    for shoe in shoe_list:
        lst1 = shoe.__str__().strip().split(",")

        if search_query.strip() == lst1[1].strip():
            print(shoe.__str__())
            break
        
    else:
        print("You have entered an incorrect code, please try again!")


def value_per_item():
    '''
    This function will calculate the total value for each item.
    This information will be printed on the console for all the shoes.
    '''
    shoe_dict = {}
    for shoe in shoe_list:
        lst1 = shoe.__str__().strip().split(",")
        value = shoe.get_cost() * shoe.get_quantity()
        shoe_dict[lst1[2]] = value

    for key, value in shoe_dict.items():
        print(f"""{BOLD}{WHITE}
        ----------------------------------------------------------------
                {key}      :     ${value}
        ----------------------------------------------------------------{END}
        """)


def highest_qty():
    '''
    The code below is to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    shoe_dict = {}
    for shoe in shoe_list:
        lst1 = shoe.__str__().strip().split(",")
        shoe_dict[lst1[2]] = shoe.get_quantity()

    highest = max(shoe_dict.values())
    for key, value in shoe_dict.items():
        if value == highest:
            print(f"""{BOLD}{WHITE}
            ----------------------------------------------------------------
            Massive $ale on the {key}'s $ale! $ale!, come and grab a bargain
            ----------------------------------------------------------------{END}
            
            """)

#==========Main Menu=============
'''
The choice menu below will execute each function above.
'''
WHITE = "\u001b[47m"
END = "\033[0m"
BOLD =  "\u001b[1m"
BLACK = "\u001b[30;1m"
# here we create a variables to be able to change the font and the background in parts of the program like the menu section.

Choice = """
Welcome to the Nike Warehouse system! What would you like to do?

s - search a product
r - re-stock.
a - add product.
v - view all.
p - put on sale.
c - calculate total value per product.
e - exit this program.
"""

read_shoes_data()

while True:
    user_choice = input(F"{WHITE}{BOLD}{BLACK}{Choice.strip().lower()}{END}")

    if user_choice == "s":
        search_shoe()

    elif user_choice == "r":
        re_stock()

    elif user_choice == "a":
        capture_shoes()    

    elif user_choice == "v":
        view_all()

    elif user_choice == "p":
        highest_qty()

    elif user_choice == "c":
        value_per_item()

    elif user_choice == "e":
        print("Goodbye")
        break
    else:
        print("Oops - incorrect input")