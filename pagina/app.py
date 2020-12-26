from flask import Flask


def create_app():
    app = Flask(__name__)

    import test
    app.register_blueprint(test.bp)


    @app.route('/')
    def hola():
        return 'hola soy un app.route'
    return app


application = create_app()