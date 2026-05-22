
# Student Management System

For every school important task for administration department is to manage student information in a procedure oriented manner with latest updates for every year which need to be available for easy access. This can be provided by a simple Students Management system to help administration so to efficiently manage student’s details. To store data MySQL is used by connecting MySQL with Python using MySQL Connector. There is also a Login Panel where now admin can register themselves and can Login.

## Example

```text
-------------------------------------
 Welcome to Student Management System
-------------------------------------
1: Login
2: Register
Enter your choice: 2
-------------------------
--------Register---------
-------------------------
Enter your Id: admin1
Enter your Password: secret
Registered successfully!
--- login ---
Enter the id: admin1
Enter the password: secret
-------------------------------------
--Welcome admin1 what you want to do!--
-------------------------------------
1: Add New Student
2: View Students
3: Search Student
4: Update Student
5: Delete Student
6: Exit
Enter your choice: 1
-------------------------
Add Student Information
-------------------------
Enter the sch no. of the student: 101
Enter the name of the student: Alice
Enter the age of the student: 17
Enter the email of the student: alice@school.edu
Enter the phone no. of the student: 9876543210
Data saved successfully!
```

## Installation

##### 1. Install Mysql Python connector 

- [Mysql](https://dev.mysql.com/downloads/mysql/)
- [Mysql Python connector](https://dev.mysql.com/downloads/connector/python/)
 
##### 2. install Mysql in Python using below command
  ```bash
    pip install mysql
  ```
    
## Features
- Login and Register
- Adding New Student
- Viewing Students
- Searching Student
- Updating Student
- Deleting Student
  
## MySQL Table Structure


### Admin Table

| Field    | Type         | Null | Key | Default | Extra |
|----------|--------------|------|-----|---------|-------|
| id       | varchar(50)  | YES  |     | NULL    |       |
| password | varchar(100) | YES  |     | NULL    |       |
 


### Student Information Table

| Field      | Type         | Null | Key | Default | Extra |
|------------|--------------|------|-----|---------|-------|
| sch_no     | int          | NO   | PRI | NULL    |       |
| name       | varchar(100) | YES  |     | NULL    |       |
| class      | varchar(50)  | YES  |     | NULL    |       |
| fee_status | varchar(100) | YES  |     | NULL    |       |
| age        | int          | YES  |     | NULL    |       |
| email      | varchar(150) | YES  |     | NULL    |       |
| phone      | varchar(150) | YES  |     | NULL    |       |


## Deployment

To deploy this project just run .py files.



  
## Author

- [@siddharth9300](https://github.com/siddharth9300)
