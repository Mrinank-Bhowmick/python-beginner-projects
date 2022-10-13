from flask import Flask, render_template,session,redirect,url_for,request
from text_to_speech import *
import time
from spe import *
app = Flask(__name__)
@app.route('/')
def indexabc():
    speechis("Which language do you speak, आप कौन सी भाषा बोलते हैं, আপনি কোন ভাষা পছন্দ করেন?, நீங்கள் எந்த மொழியை விரும்புகிறீர்கள்","en")
    time.sleep(10)
    global a
    a="Hindi"
    return render_template("basics.html",a=a)
@app.route('/index')
def index():
    Name=""
    status="logout"
    global a
    if a=="English":
        speechis2("Recent policies are as follows 1. Pradhan Mantri Kisan Pension Yojana . 2. Pradhan Mantri Kisan Samman Nidhi Scheme . 3. Pradhan Mantri Fasal Bima Yojana","en")
        return render_template("index.html",Name=Name,status=status)
    elif a=="Hindi":
        speechis2("Recent policies are as follows 1. Pradhan Mantri Kisan Pension Yojana . 2. Pradhan Mantri Kisan Samman Nidhi Scheme . 3. Pradhan Mantri Fasal Bima Yojana","hi")
        return render_template("index1.html",Name=Name,status=status)
    elif a=="Tamil":
        return render_template("index2.html",Name=Name,status=status)
    elif a=="Banbala":
        return render_template("index3.html",Name=Name,status=status)
    else:
        speechis("Which language do you speak, आप कौन सी भाषा बोलते हैं, আপনি কোন ভাষা পছন্দ করেন?, நீங்கள் எந்த மொழியை விரும்புகிறீர்கள்","en")
        time.sleep(10)
        a=speccecc()
        return render_template("basics.html",a=a)
@app.route('/logout')
def logout():
    Name=""
    status="logout"
    return render_template("index.html",Name=Name,status=status)
@app.route('/login')
def login():
    return render_template("loginform.html",password="True",statement=" ")
@app.route('/textto')
def textto():
    speechis1("Main purpose: To address the problems of farm sector distress, the Modi 2.0 Cabinet has approved a proposal to provide small and marginal farmers with a minimum Rs 3,000 per month fixed pension, costing Rs 10,774.5 crore per annum to the exchequer.","en")
    Name=""
    status="logout"
    return render_template("index.html",Name=Name,status=status)
if __name__ == '__main__':
    app.run(debug=True)
