from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return 'AWS kawan!! Banyak Buaya'

if __name__ == "__main__":
    application.run()