# Restraunt_API
The Restaurant API consists of: adding items to the menu, viewing the menu, searching for menu items based on a string, creating orders, and displaying previous orders for a user.

Add to Menu:
- Endpoint: POST http://127.0.0.1:8000/menu/
  
View Menu:
- Endpoint: GET http://127.0.0.1:8000/menu/

Both the "Add to Menu" and "View Menu" functions are implemented using a single endpoint with POST and GET methods, respectively.

Search Menu Based on String:
- Endpoint: GET http://127.0.0.1:8000/menu_item/<item_name_to_be_searched>/
This endpoint allows you to search for menu items based on a provided string.

Create Order:
- Endpoint: POST http://127.0.0.1:8000/order/
This endpoint is used to create orders.

View Past Orders:
- Endpoint: GET http://127.0.0.1:8000/orders/<email-id_of_user_whose_orders_are_to_be_seen>/
You can use this endpoint to view the previous orders of a user by providing their email address.
