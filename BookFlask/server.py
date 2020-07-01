from flask import Flask, request, jsonify
#from movie_output import output_movie, get_title_from_index, get_index_from_title
from book_output import book_output
# from games_output import games_output
import urllib.parse


app = Flask(__name__)

@app.route('/test',methods = ['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return jsonify({"response": "Get request called"})
    elif request.method == 'POST':
        req_Json = request.json
        name = req_Json['name']
        return jsonify({'reponse': 'Hi '+ name})

#@app.route('/movie/<string:a>',methods=['POST'])
#def print_list(a):
#    movie = str(a)
#    return jsonify(output_movie(movie))

@app.route('/book/<string:book>',methods=['GET','POST'])
def return_books(book):
    return jsonify(book_output(book))


# @app.route('/game/<string:game>',methods=['POST'])
# def return_games(game):
#     return jsonify(games_output(game))

#@app.route('/tvs/<string:a>',methods=['POST'])
#def print_list(a):
#    tvs = str(a)
#    return jsonify(output(tvs))

if __name__ == '__main__':
    app.run(debug=True,port=9090)
