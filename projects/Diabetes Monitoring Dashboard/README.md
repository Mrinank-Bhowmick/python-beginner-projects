# Diabetes Monitoring Dashboard

This is a healthcare web-application that uses Machine Learning algorithms to predict whether a person is diabetic or not, while also providing valuable life style improvement suggestions through chatGPT api.

## How is it unique and different from other diabetes prediction models ?

- It uses only the information from the user which he/she can fill in real-time.
- This application is integrated with an IOT device responsible for measuring real-time blood glucose levels.
- App evaluates the data and returns not only the prediction but also a good suggestion on how to keep up a good fitness for every individual.

Chat-GPT is already integrated in the dashboard to help user with further insights regarding results.😊

# Model Description

We used SVM(Support Vector Machine) machine-learning algorithm on the dataset that was uploaded to the repository (diabetesv2.0).
This dataset contains a minimum number of parameters that are required to do predictions for diabetes.

### The used machine learning model in this project is SVM at **77.27%** accuracy.

Here are some performance metrics for our model:

- SVM Accuracy: 0.7727272727272727

- SVM Precision: 0.7272727272727273

- SVM Recall: 0.5818181818181818

- SVM F1 Score: 0.6464646464646464

# Requirements

Install the till-needed packages using the command :

```bash
pip install -r requirements.txt
```

Also, don't forget to add your own OenAI API-key in chat.py

# How to run the application

After installing all the dependencies, open a terminal window in project directory and run following command :

```bash
streamlit run webApp.py
```

The application will deploy a webapp on localhost which then can be accesed through web browsers (Chrome recommended!) by any client on that network.
