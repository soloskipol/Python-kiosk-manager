kiosk=input("Please enter the kiosk name: ").strip().title()

name = input("Please enter your name: ").strip().title()

print(f"Hello, {name}! Welcome to the {kiosk} kiosk")


#THE STOCK OF THE KIOSK PROJECT A DICTIONARY CONTAINING THE PRODUCTS AND THEIR PRICES

stock={1:{"name":"sugar","price":7.5,"quantity":10},
       2:{"name":"milk","price":1.5,"quantity":20},
       3:{"name":"eggs","price":3.0,"quantity":15},
       4:{"name":"cheese","price":4.0,"quantity":8},
       5:{"name":"butter","price":2.0,"quantity":12},
       6:{"name":"bread","price":4.5,"quantity":5},
       7:{"name":"coffee","price":5.0,"quantity":15}}

#COUNTING THE NUMBER OF PRODUCTS IN THE STOCK
def  display_stock():
    print(f"\nThere are {len(stock)} products in the stock\n")

    for order,items in stock.items():

        print(f"Product {order}: {items['name']:<10} - ${items['price']:>5.2f} and the available quantity is {items['quantity']}")

def adding_products_and_restoking():
    6
    print("\n--- Available Products ---\n")
    for id,items in stock.items():
        print(items['name'].title())

    target_id=None

    product=input("Please enter the name of the product you want to add for: ").strip().lower()

    for id,items in stock.items():
        if items['name']==product:
            target_id=id
            break


    if target_id is not None:

        print(f"{product} is already in stock")

        while True:

            user_quantity=input(f"please enter the quantity of {product} you want to add: ").strip()

            if  user_quantity.isdigit():

                quantity=int(user_quantity)

                stock[target_id]['quantity']+=quantity
                
                print(f"{quantity} {product} has been added to the stock. The new quantity is {stock[target_id]['quantity']}")

                print("\nthe updated stock is as follows:".title())

                for id,items in stock.items():

                    print(f"{id}-{items['name']}: {items['quantity']}")
                break
            else:
                print("Invalid quantity entered. Please enter a valid number.")
    # ADDING A NEW PRODUCT TO THE STOCK
    else:
        print(f"\n'{product.title()}' is not in stock. Let's add it as a new product!")
        product_name=product
        price=None
        while True:

            product_price = input(f"Please enter the price of {product_name} (or 'quit' to abort): ").strip()

            if product_price.lower() == 'quit':
                print("Aborting the addition of the product.")
                return

            # using the replace method to remove the decimal point and check if the remaining string is a digit, 
            # allowing for decimal prices (additionally, the is digit method alone would fail if used for decimal prices)

            if product_price.replace('.','',1).isdigit():

                price=float(product_price)

                break

            else:
                print("Invalid price entered. Please enter a valid number.")

        if price is not None:

            print(f"The price of {product_name} is set to ${price:.2f}.")
            quantity=None
            while True:

                product_quantity=input(f"Please enter the quantity of {product_name}: ").strip()

                if  product_quantity.isdigit():

                    quantity=int(product_quantity)
                    break

                else:
                    print("Invalid quantity entered. Please enter a valid number.")

            # Assign a new ID based on the maximum existing ID or start from 1 if stock is empty

            new_id=max(stock.keys())+1 if stock else 1  

            stock[new_id]={
                    "name":product_name,
                    "price":price,
                    "quantity":quantity}

            print(f"{product_name} has been added to the stock with a price of ${price:.2f} and a quantity of {quantity}.")

            print("\nthe updated stock is as follows:".title())

            for id,items in stock.items():
                    print(f"Product {id}: {items['name']:<10} - ${items['price']:>5.2f} and the available quantity is {items['quantity']}")

#THE SALES FUNCTION
sales_log = []
unique_products = set()
def sales():

    while True:

        print("\n--- AVAILABLE PRODUCTS ---\n")

        for order, items in stock.items():
            print(f"Product {order}: {items['name']:<10} - "
                  f"${items['price']:>5.2f} and the available quantity is {items['quantity']}")

        # FINDING THE PRODUCT
        while True:

            product_id = None

            purchase = input("\nWhat do you want to buy? ").strip().lower()

            for id, items in stock.items():

                if purchase == items["name"].lower():

                    product_id = id
                    break

            if product_id is None:

                print("Enter a valid product.")

            else:

                print(f"Product found: {stock[product_id]['name']}")
                break

        # GETTING THE QUANTITY
        while True:

            user_quantity = input("Enter the quantity you want to buy: ").strip()

            if user_quantity.isdigit():

                quantity = int(user_quantity)

                if quantity <= 0:

                    print("Quantity must be greater than 0.")

                elif quantity > stock[product_id]["quantity"]:

                    print(f"The only available "
                          f"{stock[product_id]['name']} are "
                          f"{stock[product_id]['quantity']}")

                else:

                    # REDUCE STOCK
                    stock[product_id]["quantity"] -= quantity

                    # CALCULATE SALE
                    item_total = quantity * stock[product_id]["price"]

                    # STORE THE SALE AS A TUPLE IN THE SALES LOG
                    sale = (
                        stock[product_id]["name"],
                        quantity,
                        item_total
                    )

                    sales_log.append(sale)

                    # ADD PRODUCT TO THE SET
                    unique_products.add(stock[product_id]["name"])

                    print(f"\nSale recorded!")
                    print(f"Product: {stock[product_id]['name']}")
                    print(f"Quantity: {quantity}")
                    print(f"Total: ${item_total:.2f}")
                    print(f"Remaining stock: {stock[product_id]['quantity']}")

                    break

            else:

                print("Enter a valid number.")

        # ASK IF CUSTOMER WANTS ANOTHER PRODUCT
        again = input(
            "\nDo you want to buy another product? (yes/no): "
        ).strip().lower()

        if again != "yes" and again != "y":

            print("\nSale completed.")
            return


def view_sales_report():

    print("\n========== SALES REPORT ==========\n")

    # CHECK IF THERE ARE ANY SALES
    if len(sales_log) == 0:

        print("No sales have been recorded yet.11111")
        input("\nPress Enter to return to the menu...")

        return

    total_revenue = 0

    product_totals = {}

    # DISPLAY EACH SALE
    for sale in sales_log:

        product, quantity, total = sale

        print(
            f"Product: {product:<10} "
            f"Quantity: {quantity:<5} "
            f"Total: ${total:.2f}"
        )

        # ACCUMULATE TOTAL REVENUE
        total_revenue += total

        # ACCUMULATE QUANTITY SOLD PER PRODUCT
        if product in product_totals:

            product_totals[product] += quantity

        else:

            product_totals[product] = quantity

    # FIND BEST-SELLING PRODUCT
    best_product = None
    highest_quantity = 0

    for product, quantity in product_totals.items():

        if quantity > highest_quantity:

            highest_quantity = quantity
            best_product = product

    print("\n---------- SUMMARY ----------")

    print(f"Total sales: {len(sales_log)}")
    print(f"Total revenue: ${total_revenue:.2f}")
    print(f"Unique products sold: {len(unique_products)}")

    print(
        f"Best-selling product: {best_product} "
        f"({highest_quantity} sold)"
    )


def search_product():

    print("\n========== SEARCH PRODUCTS ==========\n")

    search = input(
        "Enter the product name you want to search for: "
    ).strip().lower()

    found = False

    for id, items in stock.items():

        product_name = items["name"].lower()

        if search in product_name:

            print(
                f"Product {id}: {items['name']:<10} "
                f"- ${items['price']:.2f} "
                f"- Quantity: {items['quantity']}"
            )

            found = True

    if found == False:

        print("No matches found.")  
    


#CREATING THE MENU FOR THE KIOSK PROJECT
menu={1:"view stock",
      2:"add/restock",
      3:"sell a product",
      4:"view sales report",
      5:"search product",
      6:"exit"}

while True:

    print("\nAvailable options for the kiosk are: ")

    for key, values in menu.items():

        print(f"\nOption {key}  is  {values}")

    menu_option=input("\nplease select an option from the menu above: ").strip()

    if menu_option.isdigit():
        choice=int(menu_option)

        if choice==1:
            display_stock()
        elif choice==2:
            adding_products_and_restoking()
        elif choice==3:
            sales()
            
        elif choice == 4:
            view_sales_report()
            print("\nThe sales report has been generated successfully.")

        elif choice == 5:
            search_product()
            
        elif choice==6:
            print("\nGoodbye! Thank you for using the kiosk program.\n")

            for id,items in stock.items():
                print(f"Product {id}: {items['name']:<10} - ${items['price']:>5.2f} and the available quantity is {items['quantity']}")

            break           
        else:
            print("Invalid number selected. Please try again.")
    else:
        print("Invalid option selected. Please try again.")
 