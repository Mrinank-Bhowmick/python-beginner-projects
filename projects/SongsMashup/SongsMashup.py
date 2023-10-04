from flask import Flask, request, redirect, render_template, send_file
import zipfile
import numpy as np
import smtplib
import concurrent.futures  # for multithreading compilation

# import sys
# import re
from pytube import YouTube  # downloading the mp4 file
from pydub import AudioSegment  # creating small snippets
from pydub.utils import make_chunks  # making small chunks out of it
import os
from email.mime.multipart import MIMEMultipart  # Emailing the output to the user
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders  # Encoding the attachment
from zipfile import ZipFile
from youtube_search import (
    YoutubeSearch,
)  # Bypassing the Youtube API with the another API
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        Number_vid = int(request.form["Number_vid"])
        duration = int(request.form["duration"])
        Email = request.form["email"]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(process_audio, singer, Number_vid, duration, Email)
        # process_audio(singer,Number_vid,duration)
        # email=request.form['email']
        return redirect("/success")
    return render_template("index.html")


def process_audio(singer, Number_vid, duration, Email):
    singer1 = singer + "songs"
    results1 = YoutubeSearch(singer1, max_results=Number_vid).to_dict()
    data = pd.DataFrame(results1)
    for i in range(1, (data["url_suffix"].count())):
        data["url_suffix"][i] = "https://www.youtube.com" + data["url_suffix"][i]
    links = data["url_suffix"]
    for i in links:
        # yt = YouTube(str(i))
        yt = YouTube(i, use_oauth=True, allow_oauth_cache=True)
        # print(yt.title)
        # if(yt.length<100):
        # extract only audio
        video = yt.streams.filter(file_extension="mp4", only_audio=True).first()
        # download the file
        out_file = video.download()
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp4"
        os.rename(out_file, new_file)
    audio_files = []
    for file in os.listdir():
        if file.endswith(".mp4"):
            audio = AudioSegment.from_file(file, "mp4")
            audio_file = file.replace(".mp4", ".wav")
            audio.export(audio_file, format="wav")
            audio_files.append(audio_file)
    chunks = []
    # print(audio_files)
    for audio_file in audio_files:
        chunk = make_chunks(
            AudioSegment.from_file(audio_file, format="wav"),
            chunk_length=duration * 1000,
        )
        id = np.random.randint(0, len(chunk))
        chunk = chunk[id]
        # print(chunk)
        chunks.append(chunk)
    merged = AudioSegment.empty()
    for chunk in chunks:
        merged += chunk
    merged.export("output.mp3", format="mp3")
    dir = os.getcwd()
    test = os.listdir(dir)
    for item in test:
        if item.endswith(".mp4"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".wav"):
            os.remove(os.path.join(dir, item))
    with zipfile.ZipFile("output.zip", "w") as zipf:
        zipf.write("output.mp3")
    msg = MIMEMultipart()
    msg["From"] = "noobbobby241@gmail.com"
    msg["To"] = COMMASPACE.join([Email])
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = "Downloaded and Converted Audio"

    with open("output.zip", "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename="output.zip")
        msg.attach(part)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login("noobbobby241@gmail.com", "cliwqftyqujpisht")
    smtp.sendmail("noobbobby241@gmail.com", [Email], msg.as_string())
    print("Email Sent")


@app.route("/success")
def success():
    return render_template("success.html")


# @app.route('/download')
# def download():
#     #@after_this_request
#     #def cleanup(response):
#         #cleanup_directory()
#         #return response
#     return send_file('output.zip', as_attachment=True)
# def cleanup_directory():
# test = os.listdir()
# for item in test:
# if item.endswith(".mp3"):
# os.remove(os.path.join(os.getcwd(), item))
# if item.endswith(".zip"):
# os.remove(os.path.join(os.getcwd(), item))
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
