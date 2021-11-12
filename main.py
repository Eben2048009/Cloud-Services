## Import Libraries
from flask import Flask, flash, redirect, render_template, request, session, url_for
#import jsonify
import google.cloud.texttospeech as tts
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = r"D:\USER\Downloads\qwiklabs-gcp-00-805ef2f108cd-70cbda1752da.json"


# Initialize the Flask application
app = Flask(__name__)



## Home Page           # This is a decorator.
#@app.route('/home')
#def home():
#    return render_template('home.html')


@app.route('/')  
@app.route("/texttospeech", methods=["GET", "POST"])
def text_to_speech():
    if request.method == "POST" and "to_speech" in request.form:
        to_speech = request.form["to_speech"]
        text_to_wav("en-AU-Wavenet-A", to_speech)
    return render_template("home.html")


def text_to_wav(voice_name: str, text: str):
    language_code = "_".join(voice_name.split("_")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)
    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    filename = f"{language_code}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')




if __name__ == '__main__':
    app.run(host= '127.0.0.1', port= 2048009, debug = True) 