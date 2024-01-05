
# Student Management System

For every school important task for administration department is to manage student information in a procedure oriented manner with latest updates for every year which need to be available for easy access. This can be provided by a simple Students Management system to help administration so to efficiently manage student’s details. To store data MySQL is used by connecting MySQL with Python using MySQL Connector. There is also a Login Panel where now admin can register themselves and can Login.

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

  
