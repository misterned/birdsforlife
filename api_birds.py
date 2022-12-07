import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Première base</h1>
<p>A prototype API for french birds.</p>'''


@app.route('/requetes/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('Data/birds.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM birds_fr;').fetchall()

    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/requetes', methods=['GET'])
def api_filter():
    query_parameters = request.args

    speciescode = query_parameters.get('speciescode')
    sensitive_species = query_parameters.get('sensitive_species')
    popsize_etc = query_parameters.get('popsize_etc')

    query = "SELECT * FROM birds_fr WHERE"
    to_filter = []

    if speciescode:
        query += ' speciescode=? AND'
        to_filter.append(speciescode)
    if sensitive_species:
        query += ' sensitive_species=? AND'
        to_filter.append(sensitive_species)
    if popsize_etc:
        query += ' popsize_etc=? AND'
        to_filter.append(popsize_etc)
    if not (speciescode or sensitive_species or popsize_etc):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('Data/birds.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
