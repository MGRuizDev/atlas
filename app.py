import json
from flask import Flask, render_template, request
from difflib import get_close_matches
app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/definition", methods=['POST'])
def definition():
    word = request.form["word"]

    content = json.load(open("data.json"))
    def search(word):
        if word in content:
            return content[word]
        elif word.lower() in content:
            return content[word]
        elif len(get_close_matches(word, content.keys())) > 0:
            x = input("Wait, did you mean one of these words: %s , Type Y if you do, or N if don't. " %get_close_matches(word, content.keys())[0])
            if x == "Y":
                return content[get_close_matches(word, content.keys())[0]]
            else:
                return "No choices"
        else:
            return "Sorry that word is not in our Database"

    definitions = search(word)

    return render_template('screen.html', definition=definitions, word=word)
    #return '<h1>These are your definitions' + '\n'.join(definitions)+ '</h1>'

if __name__ == "__main__":
    app.run(debug=True)
