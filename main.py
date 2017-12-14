from flask import Flask, request, render_template
import jinja2, os
from crypto import caesar_rotate_string, vigenere_rotate_string

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


error = """
<h2>Error!</h2>
    <p>Please enter a valid number. Letters, punctuation (including commas in larger numbers), and decimals are not allowed.</p>
    <p><a href="/">Return back</a></p>
    """
css = "/static/css.css"
checked = 'checked="checked"'
@app.route("/")

def index():
    explanation = '''With the Caesar Cipher, each letter is "shifted" x amount of times. For example, 
    the word "thing" with a rotation of 2 becomes "vjkpi". Enter a message you want to encrypt 
    and how many times to rotate the characters.'''
    template = jinja_env.get_template('crypto.html')
    return template.render(css=css, c_checked=checked, explanation=explanation, instructions="Rotation amount")
@app.route("/", methods=['POST'])    
def encrypt():
    explanation = '''With the Caesar Cipher, each letter is "shifted" x amount of times. For example, 
    the word "thing" with a rotation of 2 becomes "vjkpi". Enter a message you want to encrypt 
    and how many times to rotate the characters.'''
    template = jinja_env.get_template('crypto.html')
    #request.form(name-of-thing-being-requested)
    try:
        rot = request.form["encrypt"]
        text = request.form["text"]
        new_text = caesar_rotate_string(text, int(rot))
    except ValueError:
        error_template = template = jinja_env.get_template('error.html')
        return template.render(css=css, error="Only integers are allowed. No letters, punctuation (including commas in large numbers), or decimals allowed.", home="/")
    else:
        return template.render(css=css, c_checked=checked, explanation=explanation, instructions="Rotation amount", encrypted_message=new_text)
@app.route("/vigenere")

def vigenere():
    text='''The Vigenere Cipher uses an 'encryption key' to rotate the letters in a message so many characters, starting with "a"
    at 0 rotations, and ending with "z" at 25 rotations.  
    For example, the phrase "Florida swamp" with an encryption key of "gator" would give you "Llhfzja lkrsp". Here's how:
    <table><tr><td>Phrase:</td><td>F</td> <td>l</td> <td>o</td> <td>r</td> <td>i</td> <td>d</td> <td>a</td> <td> </td>
    <td>s</td> <td>w</td> <td>a</td> <td>m</td> <td>p</td></tr>
    <tr><td>Key:</td><td>g</td> <td>a</td> <td>t</td> <td>o</td> <td>r</td> <td>g</td> <td>a</td> <td>('skip') </td>
    <td>t</td> <td>o</td> <td>r</td> <td>g</td> <td>a</td></tr>
    <tr><td>Rotation amount:</td><td>6</td> <td>0</td> <td>19</td> <td>14</td> <td>17</td> <td>6</td> <td>0</td> <td>('skip') </td>
    <td>19</td> <td>14</td> <td>17</td> <td>6</td> <td>0</td></tr>
    <tr><td>Result:</td><td>L</td> <td>l</td> <td>h</td> <td>f</td> <td>z</td> <td>j</td> <td>a</td> <td> </td>
    <td>l</td> <td>k</td> <td>r</td> <td>s</td> <td>p</td></tr></table>
    '''
    template = jinja_env.get_template('crypto.html')
    return template.render(css=css, v_checked=checked, explanation=text, instructions="Encryption key")
@app.route("/vigenere", methods=['POST'])    
def encrypt_v():
    explanation = '''The Vigenere Cipher uses an 'encryption key' to rotate the letters in a message so many characters, starting with "a"
    at 0 rotations, and ending with "z" at 25 rotations.  
    For example, the phrase "Florida swamp" with an encryption key of "gator" would give you "Llhfzja lkrsp". Here's how:
    <table><tr><td>Phrase:</td><td>F</td> <td>l</td> <td>o</td> <td>r</td> <td>i</td> <td>d</td> <td>a</td> <td> </td>
    <td>s</td> <td>w</td> <td>a</td> <td>m</td> <td>p</td></tr>
    <tr><td>Key:</td><td>g</td> <td>a</td> <td>t</td> <td>o</td> <td>r</td> <td>g</td> <td>a</td> <td>('skip') </td>
    <td>t</td> <td>o</td> <td>r</td> <td>g</td> <td>a</td></tr>
    <tr><td>Rotation amount:</td><td>6</td> <td>0</td> <td>19</td> <td>14</td> <td>17</td> <td>6</td> <td>0</td> <td>('skip') </td>
    <td>19</td> <td>14</td> <td>17</td> <td>6</td> <td>0</td></tr>
    <tr><td>Result:</td><td>L</td> <td>l</td> <td>h</td> <td>f</td> <td>z</td> <td>j</td> <td>a</td> <td> </td>
    <td>l</td> <td>k</td> <td>r</td> <td>s</td> <td>p</td></tr></table>
    '''
    template = jinja_env.get_template('crypto.html')
    #request.form(name-of-thing-being-requested
    rot = request.form["encrypt"]
    text = request.form["text"]
    if rot.isalpha():
        new_text = vigenere_rotate_string(text, rot)
        return template.render(css=css, v_checked=checked, explanation=explanation, instructions="Encryption key", encrypted_message=new_text)
    else:
        error_template = template = jinja_env.get_template('error.html')
        return template.render(css=css, error="Only letters are allowed for an encryption key. No spaces, numbers or special characters.", home="/vigenere")
app.run()