# Welcome to my AI CHATBOT APP developed using Django


To use the app:  &nbsp;   
1. Activate your virtualenv    &nbsp; 
2. cd Shailaputri_AIchatbot/AIchatbot  &nbsp;   
3. Run pip install -r requirements.txt  &nbsp;   
4. Generate openAI API Key. Check https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt for steps.  
5. Enter the key in Shailaputri_AIchatbot/AIchatbot/AIchatbotapp/views.py file.   &nbsp; 
![Alt text](Attachments/OpenAIAPI.png?raw=true)&nbsp; 
&nbsp;  
6. Go to http://127.0.0.1:8000/register.   &nbsp; 

**Features:** Here are some features I used:-
=======
**Login Page (Landing):**.   
Here existing user can login. New user can create account. &nbsp;     
![Alt text](Attachments/loginPage1.png?raw=true)&nbsp; 
&nbsp; 

![Alt text](Attachments/loginPage.png?raw=true)&nbsp; 


Throws error if login details are filled incorrectly. 
![Alt text](Attachments/loginError.png?raw=true)&nbsp; 

&nbsp;  
**Register Page:**.    
Here new user can create an account by filling different fields.  
![Alt text](Attachments/registerPage.png?raw=true)&nbsp;   

If password1 != password2 it throws error.  
![Alt text](Attachments/registerError.png?raw=true)&nbsp;   
  

**AIChatbot Page:**.    
Here user is greeted by a welcome message. Addressing his username credentials.
![Alt text](Attachments/PreWelcomeMsg.png?raw=true)&nbsp;   

User can type his/her query.
![Alt text](Attachments/User2.png?raw=true)&nbsp;   

History of conversation is saved even after user logsout. This conversation is saved in Database
and differs for different user. 
![Alt text](Attachments/HistoryOfConv.png?raw=true)&nbsp; 

admin page(backend)
![Alt text](Attachments/adminpage.png?raw=true)&nbsp; 


**Logout:**. 
Redirects to the Login page.



**Other information:**.  
This app integrates with openAI API using model = gpt-3.5-turbo, which is the lastest available currently (free version). 

