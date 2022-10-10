# Restraunt_API
consists of add to menu, view menu , search menu based on string ,create order and display previous orders of the user
both add to menu and view menu are implemented using a single endpoint with POST and GET methods respectively.

the end point for Add to menu is
http://127.0.0.1:8000/menu/  with POST method

the end point for View menu is
http://127.0.0.1:8000/menu/ with GET method

the end point for seraching menu based on string is
http://127.0.0.1:8000/menu_item/<item_name_to_be_searched>/

the end point for creating order is 
http://127.0.0.1:8000/order/  with POST method

the end point for viewing past orders is
http://127.0.0.1:8000/orders/<email-id_of_user_whose_orders_are_to_be_seen>/

