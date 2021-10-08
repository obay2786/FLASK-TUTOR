from flask.templating import Environment
from jinja2 import environment
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)