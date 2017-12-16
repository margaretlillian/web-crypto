from flask import Flask, request, render_template
import jinja2, os
from crypto import caesar_rotate_string, vigenere_rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def index():
    return render_template("caesar.html")
@app.route("/", methods=['POST'])    
def encrypt():
    #request.form(name-of-thing-being-requested)
    try:
        rot = request.form["encrypt"]
        text = request.form["text"]
        new_text = caesar_rotate_string(text, int(rot))
    except ValueError:
        error = "Only integers can be used. No letters, punctuation (including commas in large numbers), or decimals allowed."
        return render_template("caesar.html", error=error)
    else:
        return render_template("caesar.html", encrypted_message=new_text)
@app.route("/vigenere")

def vigenere():
    return render_template("vigenere.html")
@app.route("/vigenere", methods=['POST'])    
def encrypt_v():
    #request.form(name-of-thing-being-requested
    rot = request.form["encrypt"]
    text = request.form["text"]
    if rot.isalpha():
        new_text = vigenere_rotate_string(text, rot)
        return render_template("vigenere.html", encrypted_message=new_text)
    else:
        error = "Only a word or letters can be used. Spaces, punctuation or numbers are not allowed."
        return render_template("vigenere.html", error=error)
app.run()