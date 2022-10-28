from flask import Flask
from flask.json import jsonify
import random

app = Flask(__name__)


@app.route("/")
def life():
    fin = open("Make-API//quote.txt", "r")
    Random_line = random.randint(0, 2)
    quote = fin.readlines()[Random_line]
    return jsonify(quote[0:-1])

#add a sentence to the poem with a post request! 

@app.route("/quote", methods=[POST])
def add_data(quote):
    entry = open("quote.txt", "w") #the second argument in the open is the files permissions. W = write, allowing us to write to the file itself. 
    entry.write("All warfare is based on deception.")
    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=True)
