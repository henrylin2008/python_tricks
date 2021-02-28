## MenuItem Class

### Attributes:

* <b>name (str)</b>:  The name of the drink. 
  * e.g. “latte”
  
* <b>cost (float)</b>: The price of the drink. 
  * e.g 1.5

* <b>ingredients (dictionary)</b>: The ingredients and amounts required to make the drink. 
  * e.g. {“water”: 100, “coffee”: 16}



## Menu Class

### Methods:

* <b>get_items()</b>: Returns all the names of the available menu items as a concatenated string.
    * e.g. “latte/espresso/cappuccino”

* <b>find_drink(order_name)</b>: Parameter order_name: (str) The name of the drinks order. 
  Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.



## CoffeeMaker Class

### Methods:

* <b>report()</b>: Prints a report of all resources.
    * e.g.
        * Water: 300ml
        * Milk: 200ml
        * Coffee: 100g


* <b>is_resource_sufficient(drink)</b>: Parameter drink: (MenuItem) The MenuItem object to make.
Returns True when the drink order can be made, False if ingredients are insufficient.
    * e.g.
        * True


* <b>make_coffee(order)</b>: Parameter order: (MenuItem) The MenuItem object to make. 
  Deducts the required ingredients from the resources.
  

## MoneyMachine Class

### Methods:

* <b>report()</b>: Prints the current profit 
  * e.g.
    * Money: \$0


* <b>make_payment(cost)</b>: Parameter cost: (float) The cost of the drink. 
  Returns True when payment is accepted, or False if insufficient.
  * e.g. False 