import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

def home():
    return "<h1>Le monde des oiseaux est magique</h1><br>list_latin = ['Vanellus vanelli', 'Ardea cinerea', 'Carduelis carduelis']\
    <br>tuple_francais = ('Vanneau huppé', 'Héron Cendré', 'Chardonneret élégant')\
    <br>print(list_latin)\
    <br>print(tuple_francais)\
    <br>print(list_latin[0])\
    <br>list_latin[0] = 'Vanellus vanellus' # Modification du premier élément de la liste\
    <br>print(list_latin)\
    <br>print(tuple_francais[1])\
    <br># Modification du premier élément du tuple\
    <br>#tuple_français[1] = 'Vanneau pas huppé'\
    print(tuple_francais)\
    <br>print('Poids en octets du tuple : ',tuple_francais.__sizeof__()) #taille de la variable, occupation en mémoire\
    <br>print('Poids en octets de la liste : ',list_latin.__sizeof__())"


app.run()
