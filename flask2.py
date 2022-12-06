from flask import Flask, render_template
app = Flask(__name__)

list_latin = ['Vanellus vanelli', 'Ardea cinerea', 'Carduelis carduelis']
tuple_francais = ('Vanneau huppé', 'Héron Cendré', 'Chardonneret élégant')

@app.route("/")
def home():
    return render_template("home.html", message = "le dernier oiseau "
                           +"que j'ai photographié est un "
                           + tuple_francais[-1], nb = len(tuple_francais),
                           franc = tuple_francais)

@app.route("/next")
def suite():
    return render_template("page_suivante.html",nb = len(tuple_francais))

app.run()
