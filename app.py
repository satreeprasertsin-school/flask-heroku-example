"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
#    json_data = {'Hello': 'World!'}
    return jsonify(json_data)                                                                               
    return "นายราเมศ อยู่เจริญ เลข1 ห้อง 4/1"

if __name__ == '__main__':
    app.run()
