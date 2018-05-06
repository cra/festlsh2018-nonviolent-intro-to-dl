# coding: utf-8

import bottle


@bottle.route('/')
def index():
    return bottle.static_file('index.html', root="./front/")


@bottle.route('/json/color.get')
def route():
    return {"hello": "color"}


@bottle.route('/static/<filename>', method="GET")
def serve_static(filename):
    return bottle.static_file(filename, root="./front/static/")


if __name__ == "__main__":
    bottle.debug(True)
    bottle.run(host="localhost", port=8080, reloader=True)
