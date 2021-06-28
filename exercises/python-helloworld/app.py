#Adding new comment to check git  push power
#finally i did the change through git checking again
from flask import Flask
from flask import json

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    
    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
