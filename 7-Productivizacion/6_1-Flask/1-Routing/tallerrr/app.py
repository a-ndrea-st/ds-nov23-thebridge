import flask
from flask import request, jsonify


app=flask.Flask(__name__)
app.config["DEBUG"]=True    # Establece la configuración de depuración de la aplicación. Si ocurre algún error en la aplicación, se mostrará una página de error detallada en el navegador web.


books = [ 
    {'id': 0, 
     'title': 'A Fire Upon the Deep', 
     'author': 'Vernor Vinge', 
     'first_sentence': 'The coldsleep itself was dreamless.', 
     'published': '1992'}, 
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 
     'author': 'Ursula K. Le Guin', 
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 
     'published': '1973'}, 
    {'id': 2, 
     'title': 'Dhalgren', 
     'author': 'Samuel R. Delany', 
     'first_sentence': 'to wound the autumnal city.', 
     'published': '1975'} 
] 

@app.route('/api/v1/resources/book/all', methods=['GET']) 
def api_all(): 
    return jsonify(books) 

@app.route('/api/v1/resources/book', methods=['GET']) 
def api_id(): 
    if 'id' in request.args: 
        id = int(request.args['id']) 
    else: 
        return "Error: No id field provided. Please specify an id." 
    results = [] 
    for book in books: 
        if book['id'] == id: 
            results.append(book) 
    return jsonify(results)


@app.route('/api/v1/resources/book/<string:title>', methods=['GET']) 
def get_by_title(title): 
    for book in books: 
        if book['title'] == title: 
            return jsonify(book) 
    return jsonify({'message': "Book not found"})

@app.route('/api/v2/resources/book', methods=['GET']) 
def get_by_id(): 
    id = int(request.get_json()['id']) 
    for book in books: 
        if book['id'] == id: 
            return jsonify(book) 
    return jsonify({'message': "Book not found"})

@app.route('/api/v1/resources/book', methods=['POST']) 
def post_book(): 
    data = request.get_json() 
    books.append(data) 
    return data


@app.route('/',methods=["GET"])
def home():
    return"<h1>Archivo de Distant Reading</h1><p>Esto es un prototipo de API para leer (distant reading) novelas.</p>"

@app.route('/hola',methods=["GET"])
def home2():
    return"<h1>He entrado a ruta hola</h1><p>ok!</p>"


app.run()

