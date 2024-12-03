from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        # run function to process data/do prediction
        # return prediction
        print(data)
        return jsonify(data)
    else:
        return jsonify({'message': 'Hello World, this is Get request'})
    
if __name__ == '__main__':
    app.run(debug=True)
