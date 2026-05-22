# CURD-API

This repo is an example for creating an API using Flask and Python. It can search the database on any type of segmentation of data. 
It includes a sample csv file consisting of 1000 lines of dummy data. Select the options that you want to include in the filter and add parameters for filtration of data.
For example, if you want to get data of male customers whose age is between 18 and 25, put a tick on the Age and the Gender checkboxes and add the required age group and gender specification.

Please note that this a sample project to understand the concepts of SQL and web development using Flask. It does not contain any personal data. You can take inspiration from this algorithm to create your own projects.

## Example

1. Run `python3 main.py` and open `http://127.0.0.1:5000/` in a browser.
2. The home page shows a filter form. Tick the "Age" checkbox and enter `18` and `25` in the age-range fields; tick the "Gender" checkbox and select "Male".
3. Click the submit button. The app builds a SQL query against the loaded CSV data using DuckDB and redirects to `/query_output`.
4. A table is rendered showing columns: User ID, User Name, Age, Gender, Country, Sign-UP Date, Subscription Plan, Device, Login, Added To Cart, Purchased Item, and Time of Event — filtered to male customers aged 18–25.

## Usage
1. To install the required packages, run `pip3 install -r ./requirements.txt` in Terminal while working in the CURD-API directory. 

2. Run: `python3 main.py`
  
If everything works successfully, the website will be available on the localhost server -> http://127.0.0.1:5000/
