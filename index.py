from flask import Flask # type: ignore
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "<p>Hello this is flask</p>"

if __name__=="__main__":
    helloworld.run(host="0.0.0.0",port = int("3000"),debug=True)