from flask import Flask, render_template, request, redirect, session

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    application.run(debug = True)