cartItems = []
# print(cartItems)
cartPrices = []
# print(cartPrices)


def add_to_cart(items, cartItems, cartPrices):
    userItem = input("Please enter an item to add to your cart")
    try:  # try except block to handle incorrect user input
        # print(items[userItem])
        cartItems.append(userItem)  # adds user input along with the price
        # print(cartItems)
        cartPrices.append(items[userItem])
        # print(cartPrices)
    except KeyError:
        # error validation for if the user gives an input that does not match the item list
        print("Not found")
