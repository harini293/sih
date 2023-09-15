from flask import Flask, redirect, url_for, render_template, jsonify, request

app = Flask(__name__)


@app.route('/karnataka.html')
def karnataka_page():
    # You can pass any data you need to the template here
    return render_template('karnataka.html')


@app.route('/save_coordinates', methods=['POST'])
def save_coordinates():
    if request.method == 'POST':
        data = request.get_json()
        # Process the coordinates as needed
        print('Received coordinates:', data)
        # You can save the coordinates to a database, perform calculations, or any other desired action
        response_data = {'message': 'Coordinates received successfully'}
        return jsonify(response_data)


@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
