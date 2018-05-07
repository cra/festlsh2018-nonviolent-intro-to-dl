# coding: utf-8

import bottle
import numpy as np

app = bottle.default_app()
app.iteration = 0


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root="./front/")


@bottle.route('/json/color.get')
def color_get():
    wr, wg, wb, br, bg, bb = np.random.randint(0, 255, size=6)
    app.iteration += 1
    ctx = {
        'white': "#%x%x%x" % (wr, wg, wb),
        'black': "#%x%x%x" % (br, bg, bb),
        'iteration': app.iteration,
    }
    return ctx


@bottle.route('/json/color.pick', method="POST")
def color_pick():
    data = bottle.request.json
    color = ''.join(["%x" % int(x) for x in data['color'][4:-1].split(',')])
    print(f"When input is #{color}, user picks {data['pick']}")
    return {}


@bottle.route('/static/<filename>', method="GET")
def serve_static(filename):
    return bottle.static_file(filename, root="./front/static/")


if __name__ == "__main__":
    app.config["debug"] = True
    app.run(host="localhost", port=8080, reloader=True)
