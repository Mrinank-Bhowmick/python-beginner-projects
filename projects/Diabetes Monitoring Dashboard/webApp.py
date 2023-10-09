from chat import chat
import pandas as pd
import requests
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from streamlit_lottie import st_lottie  # importing package for animation

st.set_page_config(page_title="PredictO", layout="wide", page_icon=":pill:")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# -------------ASSETS-------------
lottie_files1 = load_lottieurl(
    "https://lottie.host/c44be9f7-2309-4573-bc2f-1735c2d0581d/JkZN9a1nq8.json"
)
lottie_files2 = load_lottieurl(
    "https://lottie.host/805c4752-59c1-4bb8-bbed-ee08a2fa18fe/y2uZUuipJB.json"
)
lottie_files3 = load_lottieurl(
    "https://lottie.host/198f917d-41bf-47b4-a8ed-6c7838f693d0/G6AU3k0wqA.json"
)

# -------------Header Section-----------------
st.subheader("WELCOME TO PREDICTO :wave:")
st.title("Your Real-Time Healthcare App")
with st.container():
    l_column, r_column = st.columns((7, 3))
    with l_column:
        st.write(
            "Revolutionize your healthcare experience with our smart app! "
            "Accessible, intuitive, and personalized, it empowers you to take control of your well-being. "
            "From tracking vital signs to scheduling appointments, our app seamlessly connects you with healthcare"
            " professionals and provides tailored recommendations for a healthier life. "
            "Experience the future of healthcare at your fingertips!"
        )

# -------------What do I DO Section-----------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How to get yourself Checked?")
        st.write("##")  # adds space between title and body
        st.write(
            """
            - Fill in all the values in their respective blocks.

            - Click on the 'Predict' button.

            - Get to know your results in Real-time.

            """
        )

    with right_column:
        st_lottie(lottie_files1, height=300, key="health")

# -------------Loading dataset-----------------
df = pd.read_csv("diabetesv2.0.csv")

# Assuming your dataset is stored in the 'df' variable
X = df[["BMI", "Glucose", "Pregnancies", "Age"]]
y = df["Outcome"]

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Creating and training the Support Vector Machine model
svm = SVC()
svm.fit(X_train, y_train)

# Calculate accuracy for training data
train_predictions = svm.predict(X_train)
train_accuracy = accuracy_score(y_train, train_predictions) * 100

# -------------Taking Inputs Section-----------------

with st.container():
    st.write("---")
    st.header("Let's get you Checked!")
    st.write("##")
    (
        col1,
        col2,
        col3,
    ) = st.columns((3, 1, 3))
    with col1:
        # Input fields
        gender = st.radio("Select your gender", ("Male", "Female"))
        height = st.number_input(
            "Height(in centimeters)", min_value=0.0, max_value=300.0, value=0.0
        )
        weight = st.number_input(
            "Weight(in kilograms)", min_value=0.0, max_value=600.0, value=0.0
        )

    with col3:
        st.write(
            """
            - #### Use your Beato Sensor and fill in the Glucose value.
            """
        )
        glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
        pregnancies = st.number_input(
            "Number of Pregnancies", min_value=0, max_value=20, value=0
        )
        age = st.number_input("Age", min_value=0, max_value=120, value=0)

        def user_report():
            user_report_data = {
                "BMI": weight / (height**2),
                "Glucose": glucose,
                "Pregnancies": pregnancies,
                "Age": age,
            }
            report_data = pd.DataFrame(user_report_data, index=[0])
            return report_data

        # Initialize user_result outside the if block
        user_result = None

        # Button to predict
        if st.button("Predict"):
            # Get user input and make prediction
            user_data = user_report()
            user_result = svm.predict(user_data)

# Display the prediction result
with st.container():
    st.write("---")
    l_column, r_column, end_column = st.columns((3, 3, 3))
    with r_column:
        if user_result is not None:
            if user_result[0] == 0:
                st_lottie(lottie_files2, height=300, key="healthy")
                st.write(" ##### Prediction: You are not Diabetic")
                st.write(f"Training Data Accuracy: {train_accuracy:.2f}%")
            else:
                st_lottie(lottie_files3, height=300, key="unhealthy")
                st.write(" ##### Prediction: You are Diabetic")
                st.write(f"Training Data Accuracy: {train_accuracy:.2f}%")
if user_result is not None:
    with st.container():
        st.write("---")
        left_column, mid_column, right_column = st.columns((2, 6, 2))
        with mid_column:
            st.header("Additional Diagnostic")
            st.write("##")
            if user_result is None:
                st.write("  ")
            else:
                # Calculating Basal Metabolic Rate
                if gender == "male":
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5

                    st.write("Your Basal Metabolic Rate(BMR) is ", bmr, "calories/day")

                else:
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161

                    st.write("Your Basal Metabolic Rate(BMR) is ", bmr, "calories/day")

            st.write("##")
            st.write("##")

            try:
                bmi = weight / (height**2)
            except ZeroDivisionError:
                bmi = ""

            query = ""

            if user_result is not None:
                if user_result[0] == 0:
                    query = f"""I am a {gender}, {age} years old having a BMI of {bmi} kg/square meters and
                            BMR of {bmr} calories/day, I have had {pregnancies} pregnancies and my current glucose
                            levels are {glucose} mg/dL and I am non diabetic, please suggest me health prescriptions
                            to keep myself healthy and also to keep a check on my fitness condition based on the 
                            parameters I have mentioned. Give suggestions in points, avoid using any other comprehension 
                            other than what is asked for and keep it user friendly. """
                else:
                    query = f"""I am a {gender}, {age} years old having a BMI of {bmi} kg/square meters and
                                            BMR of {bmr} calories/day, I have had {pregnancies} pregnancies and my 
                                            current glucose levels are {glucose} mg/dL and I am diabetic, please 
                                            suggest me health prescriptions to keep myself healthy and also to keep a 
                                            check on my fitness condition based on the parameters I have mentioned. 
                                            Give suggestions in points, avoid using any other comprehension other 
                                            than what is asked for and keep it user friendly."""
            if user_result is not None:
                data = chat(query)

                # Printing the data in a box using markdown
                st.markdown(f"```markdown\n{data}\n```")
