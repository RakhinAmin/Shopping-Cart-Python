import addToCart
import viewCart
# importing functions from other modules that are necessary to run the cart program
import calculateCart

# creates a dictionary - a list of cart items that each have a price assigned
items = {'apple': 0.5, 'banana': 0.25, 'chocolate': 1.0}
print("Welcome to our store! the items for sale are", items)
cartItems = []  # creates an empty list for the user to add their desired items and prices
# print(cartItems)
cartPrices = []
# print(cartPrices)


while True:  # loop will run until the user decides to end the program
    userChoice = input(
        "Please enter one of the following choices: add, view, calculate or end")  # gives user 4 choices for the program
    print(userChoice)
    if userChoice == "add":
        # runs the add to cart function
        addToCart.add_to_cart(items, cartItems, cartPrices)
    elif userChoice == "view":
        # runs the view cart function
        viewCart.view_cart(cartItems, cartPrices)
    elif userChoice == "calculate":
        # runs the calculate cart total function
        calculateCart.calculate_total(cartPrices)
    elif userChoice == "end":
        break  # ends program
    else:
        # in case user input is wrong, error is shown
        print("Invalid input, please try again")

print("Thank you for shopping at our store")
