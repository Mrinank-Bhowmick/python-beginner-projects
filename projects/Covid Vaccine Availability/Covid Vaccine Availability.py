import requests
import datetime
import json
import random

#### Getting otp
print("\n--------Vaccine Booking Portal--------")
mobile_no = input("Enter the Mobile number: ")
mobile_dic = {"mobile": mobile_no}
mobile_dic = json.dumps(mobile_dic)
otp_url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
mobile_otp = requests.post(otp_url, data=mobile_dic)
otp_data = mobile_otp.text
otp = input("Enter the OTP: ")

#### Asking for location and date
district_pincode = input("\nEnter Pincode of District: ")
date = input("Enter the date for Booking(dd-mm-yyyy): ")

#### Genarating current date
today = datetime.datetime.now()
appointment_date = datetime.datetime.strptime(date, "%d-%m-%Y")

#### Dates in format
today = today.__format__("%Y-%m-%d")
appointment_date = appointment_date.__format__("%Y-%m-%d")

#### Checking for valid date
if today <= appointment_date:

    #### Fetching appointment Availability
    appointment_url = ("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="
            + district_pincode
            + "&date=" + date)
    
    appointment_list = requests.get(appointment_url)
    appointment_data = appointment_list.json()

    #### Checking whether working or not
    if 200 == appointment_list.status_code and len(appointment_data["sessions"]) != 0:
        user_name = input("Enter Beneficiary Name: ")

        #### Vaccine selection
        vaccine_type = {"1": "COVISHIELD", "2": "COVAXIN"}
        print("\n--------Vaccine--------")
        print("1. COVIDSHIELD\n2. COVAXIN")
        vaccine = input("Vaccine: ")

        #### Getting Appointment list
        print("\n--------Appointment Availability--------\n")
        for i in appointment_data["sessions"]:
            if i["vaccine"] == vaccine_type[vaccine]:
                print("->", i["name"])
                print("Vaccine:", i["vaccine"])
                print("Dose 1:",i["available_capacity_dose1"],
                    "\nDose 2:",i["available_capacity_dose2"],
                    "\n")

        ##### Booking Venue
        vaccination_centre = input("Enter Vaccination Centre: ")

        ##### Dose selection
        print("\n--------Appointment for Dose--------")
        print("1.Dose 1\n2.Dose 2")
        dose = input("Dose:")

        ##### Slot Booking
        print("\n--------Appointment Timing--------")
        slots = {
            "1": "09:00AM-11:00AM",
            "2": "11:00AM-01:00PM",
            "3": "01:00PM-03:00PM",
            "4": "03:00PM-06:00PM",
        }
        print("1.09:00AM-11:00AM\n2.11:00AM-01:00PM\n3.01:00PM-03:00PM\n4.03:00PM-06:00PM")
        slot_time = input("\nSelect Slot Timing: ")

        ##### Generating random number
        random = random.randint(10000000000000, 99999999999999)

        ###### Message of appointment
        date = str(date)
        print("\nDear " + user_name + ",\nYour Vaccination is Scheduled for "
            + date + " " + slots[slot_time] + " at " 
            + vaccination_centre, end="")

        print(".\nYour Beneficiary reference id " + str(random)
            + " and your 4 digits secret code for vaccination is "
            + str(random % 10000) + " -CoWIN\n\n\n")

    else:
        print("Booking yet not started!")
else:
    print("Invalid Date!")
    