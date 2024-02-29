from website import create_app
from flask_frozen import Freezer


app = create_app()
freezer = Freezer(app)


if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)