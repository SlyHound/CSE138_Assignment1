from flask import Flask, request, jsonify, make_response, abort

app = Flask(__name__)

@app.route('/distributed', methods=['GET', 'POST'])
def distributed():
    if request.method == 'GET':
        return make_response(jsonify({"Type": "GET", "message": "Hello Distributed Systems"}), 200)
    else: # otherwise the request type is a POST method
        abort(405)

@app.route('/systems', methods=['GET', 'POST'])
def systems():
    if request.method == 'GET':
        return make_response(jsonify({"Type": "GET", "message": "Get Message Received"}), 200)
    else: # otherwise the request type is a POST method
        post_msg = request.args.get('msg')
        if post_msg:
            return make_response(jsonify({"Type": "POST", "message": post_msg}), 200)
        abort(405) 

if __name__ == "__main__":
    app.run()