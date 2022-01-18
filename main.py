from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    # Initial retrieval of home page.
    if(request.method == "GET"):
        return render_template("home.html")
    else:
        # Retrieving string to be enciphered.
        text = request.form["simpleText"]
        encText = ""
        # Enciphering string character by character
        for char in text:
            if char >= 'a' and char <= 'z':
                # implementation of algorithm.
                encText = encText + chr(25 - ord(char) + 2 * ord('a'))
            else:
                # if char is not lower-case alphabetical character.
                encText = encText + char
        # returning page with enciphered string.
        return render_template("home.html", eText=encText, plainText = text)

@app.route("/home", methods = ["GET", "POST"])
def decFun():
    if(request.method == "GET"):
        return render_template("home.html")
    else:
        # Retrieving string to be deciphered.
        text = request.form["encipheredText"]
        decText = ""
        # Deciphering string character by character
        for char in text:
            if char >= 'a' and char <= 'z':
                # implementation of algorithm.
                decText = decText + chr(25 - ord(char) + 2 * ord('a'))
            else:
                # if char is not lower-case alphabetical character.
                decText = decText + char
        # returning page with deciphered string.
        return render_template("home.html", plainText = text, eText = text)

if __name__ == '__main__':
    app.run(debug = True)

