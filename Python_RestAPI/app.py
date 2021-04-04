from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'GET':
        return make_response(jsonify({"message": "I'm alive!!"}), 200)
    else: # otherwise the request type is a POST method
        abort(405)

@app.route('/ping/<name>', methods=['GET', 'POST'])
def dynamic_ping(name):
    if request.method == 'POST':
        return make_response(jsonify({'message': f"I'm alive, {name}!!"}), 200)
    else: # otherwise the request type is a GET method
        abort(405)

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'GET':
        return make_response(jsonify({"message": "Get Message Received"}), 200)
    else: # otherwise the request type is a POST method
        post_msg = request.args.get('msg')
        if post_msg:
            return make_response(jsonify({"message": post_msg}), 200)
        abort(400)

if __name__ == "__main__":
    app.run()