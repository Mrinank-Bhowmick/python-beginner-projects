from flask import Blueprint, render_template, request, flash
import duckdb

views = Blueprint("views", __name__)
# Read data using DuckDB
db = duckdb.connect()
db.execute(
    "CREATE TEMPORARY TABLE attributes AS SELECT * FROM read_csv_auto('user_attributes.csv')"
)
db.execute(
    "CREATE TEMPORARY TABLE events AS SELECT * FROM read_csv_auto('user_events.csv')"
)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/query_output", methods=["GET", "POST"])
def index():
    # Create a SQL query as a string to execute in DuckDB
    if request.method == "POST":
        print(request.form)
        attr = request.form
        age_from = attr.get("age_from")
        age_to = attr.get("age_to")
        gender_male = attr.get("male")
        gender_female = attr.get("female")
        input_location = attr.get("input_location")
        input_date = attr.get("input_date")
        input_sub_plan = attr.get("input_sub_plan")
        input_device = attr.get("input_device")

    column_name = [
        "User ID",
        "User Name",
        "Age",
        "Gender",
        "Country",
        "Sign-UP Date",
        "Subscription Plan",
        "Device",
        "Login",
        "Added To Cart",
        "Purchased Item",
        "Time of Event",
    ]
    selected_queries = []
    query_select = [
        "SELECT a.*,e.* EXCLUDE user_ID FROM attributes a INNER JOIN events e ON a.user_ID = e.user_ID WHERE"
    ]
    parameters = []
    query_orderer = []
    # Check for the attributes which are selected and add them to the SQL query
    if attr.get("age") == "on":
        selected_queries.append(age_from)
        selected_queries.append(age_to)
        if age_from is not "" and age_to is not "":
            query_for_age = "(a.age BETWEEN ? AND ?) AND"
            query_select.append(query_for_age)
            parameters.append(age_from)
            parameters.append(age_to)
        else:
            query_for_age = "(a.age BETWEEN 18 AND 60) AND"
            query_select.append(query_for_age)

    if attr.get("gender") == "on":
        if gender_female == "female" and gender_male == "male":
            selected_queries.append(gender_female)
            query_for_gender_all = "a.gender == 'Female' OR a.gender == 'Male' AND"
            query_select.append(query_for_gender_all)
        elif gender_female == "female":
            selected_queries.append(gender_female)
            query_for_female = "a.gender == 'Female' AND"
            query_select.append(query_for_female)
        elif gender_male == "male":
            selected_queries.append(gender_male)
            query_for_male = "a.gender == 'Male' AND"
            query_select.append(query_for_male)

    if attr.get("location") == "on":
        selected_queries.append(input_location)
        query_for_location = "UPPER(a.location) == UPPER(?) AND"
        query_select.append(query_for_location)
        parameters.append(input_location)

    if attr.get("signup_date") == "on":
        selected_queries.append(input_date)
        query_for_date = "(a.signup_date == ?) AND"
        parameters.append(input_date)
        query_select.append(query_for_date)

    if attr.get("sub_plan") == "on":
        selected_queries.append(input_sub_plan)
        query_for_plan = "(UPPER(a.sub_plan) == UPPER(?)) AND"
        parameters.append(input_sub_plan)
        query_select.append(query_for_plan)

    if attr.get("device") == "on":
        selected_queries.append(input_device)
        query_for_device = "(UPPER(a.device_type) == UPPER(?))"
        parameters.append(input_device)
        query_select.append(query_for_device)

    query_selection = " ".join(query_select).rstrip("AND")

    if attr.get("event_1") == "on":
        selected_queries.append(login)
        query_for_login = " ORDER BY e.login,a.user_ID;"
        query_orderer.append(query_for_login)
    elif attr.get("event_2") == "on":
        selected_queries.append(added_to_cart)
        query_for_cart = " ORDER BY e.added_to_cart,a.user_ID;"
        query_orderer.append(query_for_cart)
    elif attr.get("event_3") == "on":
        selected_queries.append(purchased_item)
        query_for_purchased_item = " ORDER BY e.purchased_item,a.user_ID;"
        query_orderer.append(query_for_purchased_item)
    elif attr.get("time_stamp") == "on":
        selected_queries.append(time_stamp)
        query_for_time = " ORDER BY e.time_stamp,a.user_ID;"
        query_orderer.append(query_for_time)
    else:
        query_order = " ORDER BY a.user_ID;"
        query_orderer.append(query_order)

    query_selection = query_selection + " ".join(query_orderer)
    print(
        query_selection, parameters
    )  # Logs out the SQL query before running (For Debugging purposes)

    data = db.execute(query_selection, parameters).fetchall()
    return render_template("table.html", data=data, header=column_name)
