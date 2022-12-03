import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True
@app.route('/', methods=['GET'])

birds = [
{'speciescode': 'A067',
'speciesname': 'Bucephala clangula',
'popsize_etc': 2250,
'population_trend_long_magnitude_min': 3000,
},
    
{'speciescode': 'A075',
'speciesname': 'Haliaeetus albicilla',
'popsize_etc': 25,
'population_trend_long_magnitude_min': 100,
},
    
{'speciescode': 'A084',
'speciesname': 'Circus pygargus',
'popsize_etc': 33,
'population_trend_long_magnitude_min': 700,
}
]

def home():
    return "<h1>Le monde des oiseaux est magique</h1>"
app.run()
