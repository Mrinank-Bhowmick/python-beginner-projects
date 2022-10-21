## WEBSITE BLOCKER
The objective of Python website blocker is to block some certain websites which can distract the user during the specified amount of time.
In this, we will block the access to the list of some particular websites during the working hours so that the user can only access those websites during the free time only.
The working time in this python application is considered from 9 AM to 5 PM. The time period except that time will be considered as free time.

### The hosts file

>To block the access to a specific website on the computer, we need to configure the  **hosts**  file.

The hosts file is a local file which was used to map hostnames to IP addresses in the old days. Although the DNS service is used nowadays to map the hostnames to the IP addresses, the host file is still very complex and can be used to configure the mapping of the IP addresses locally.
### Location of hosts file
The location of the hosts file varies from operating system to operating system.
1. **Windows:**  C:\Windows\System32\drivers\etc
2. **mac and Linux:**  /etc/hosts
We can manually change this file or write a python script to block the websites.
![enter image description here](https://images.pcworld.com/images/article/2012/01/block2-10964843.png)

### Requirements

We need to know the following python modules to build the python website blocker.

1.  **file handling:**  file handling is used to do the modifications to the hosts file.
2.  **time:**  The time module is used to control the frequency of the modifications to the hosts file.
3.  **datetime:**  The datetime module is used to keep track of the free time and working time.