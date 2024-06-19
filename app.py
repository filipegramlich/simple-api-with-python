from flask import Flask, jsonify

app = Flask(__name__)

planets = [
    {'id': 1, 'name': 'Mercury', 'description': 'The smallest planet in our solar system and closest to the Sun.'},
    {'id': 2, 'name': 'Venus', 'description': 'Second planet from the Sun and has a thick, toxic atmosphere.'},
    {'id': 3, 'name': 'Earth', 'description': 'Our home planet, the third planet from the Sun and the only known place with life.'},
    {'id': 4, 'name': 'Mars', 'description': 'The red planet, known for its iron oxide surface.'},
    {'id': 5, 'name': 'Jupiter', 'description': 'The largest planet in our solar system with a massive storm called the Great Red Spot.'},
    {'id': 6, 'name': 'Saturn', 'description': 'Famous for its extensive ring system.'},
    {'id': 7, 'name': 'Uranus', 'description': 'An ice giant with a blue-green color due to methane in its atmosphere.'},
    {'id': 8, 'name': 'Neptune', 'description': 'The farthest planet from the Sun in our solar system and has strong winds.'}
]

@app.route('/')
def hello_world():
  return 'hello world!'

@app.route('/planets')
def get_planets():
  return jsonify(planets)

@app.route('/planets/<int:id>', methods=['GET'])
def get_planet_by_id(id):
  for planet in planets:
    if planet.get('id') == id:
      return jsonify(planet)

app.run(port=5000, host='localhost', debug=True)
    
