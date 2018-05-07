# coding: utf-8

import bottle
import numpy as np

from neural_networks import NeuralNetwork

app = bottle.default_app()
app.iteration = 0
app.nn = NeuralNetwork(3, 3, 2)


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root="./front/")


@bottle.route('/json/color.get')
def color_get():
    r, g, b = np.random.randint(0, 255, size=3)
    app.iteration += 1

    guess = app.nn.predict(np.array([[r, g, b]]))[0]
    if guess[0] < guess[1]:
        guess_label = "white"
    else:
        guess_label = "black"

    ctx = {
        'color': "#%02x%02x%02x" % (r, g, b),
        'iteration': app.iteration,
        'guess': guess_label,
        'black_probability': guess[0],
        'white_probability': guess[1],
    }
    return ctx


@bottle.route('/json/color.pick', method="POST")
def color_pick():
    data = bottle.request.json

    # data["color"] надо сконвертить из "rgb(200, 45, 70)" в input для NN
    color = [float(x) / 255 for x in data['color'][4:-1].split(',', 3)]
    color = np.array([color])
    if data["pick"] == "white":
        target = np.array([[0, 1]])
    else:
        target = np.array([[1, 0]])

    app.nn.train(color, target)
    # error = target - app.nn.predict(color)
    # print(error)
    return {}


@bottle.route('/static/<filename>', method="GET")
def serve_static(filename):
    return bottle.static_file(filename, root="./front/static/")


if __name__ == "__main__":
    app.config["debug"] = True
    app.run(host="localhost", port=8080, reloader=True)
