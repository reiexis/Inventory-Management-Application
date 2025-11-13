
# Track multiple books
books = {}
threshold = 5


# Input details for 3 books
for i in range(1, 4):
    print(f"\n--- Enter details for Book {i} ---")
    book_title = input("Enter book title: ")
    quantity_purchased = int(input("Enter quantity of book purchased: "))
    price_per_unit = float(input("Enter price per unit: "))
    stock_updates = int(input("Enter number of new shipment: "))
    current_stock = int(input("Enter current stock: "))


    # Run calculations
    total_sales_amount = quantity_purchased * price_per_unit
    inventory_count = current_stock + stock_updates - quantity_purchased


    # Save book details
    books[book_title] = {
        "inventory": inventory_count,
        "total_sales": total_sales_amount
    }


    # Check threshold
    if inventory_count < threshold:
        print(f" Stock is {inventory_count}, time to restock!")
    else:
        print(f" Stock level is okay: {inventory_count}")


    print(f"Total sales cost is ${total_sales_amount:.2f}")
    print(f"Copies of {book_title} left in stock: {inventory_count}")


# Show summary of all books
print("\n--- Inventory Summary ---")
for title, info in books.items():
    print(f"{title}: {info['inventory']} copies left, Sales ${info['total_sales']:.2f}")
