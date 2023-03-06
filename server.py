from flask import Flask, request, jsonify, render_template
from supersighter import searcher
import time
app = Flask(__name__)
request_count = 0
accepted_request_count = 0


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search")
def search():
    global request_count
    request_count += 1
    local_requestCount = request_count
    
    time.sleep(0.300)
    if(local_requestCount==request_count):
        
        global accepted_request_count
        accepted_request_count += 1
    
        results = searcher.get_results(request.args.get(
            'q'), request.args.get('max_results'))
        response = jsonify({
            'results': results
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        print('Acceptance Rate : ', ((accepted_request_count/request_count)*100))
        return response
    else:
        return jsonify('waiting for latest request to reduce server load'), 200

@app.route("/getinfo")
def getinfo_template():
    id = request.args.get('id')
    return render_template('getinfo.html')


@app.route("/getinfo/<id>")
def getinfo(id):
    return jsonify(searcher.allData[int(id)])
    
    



if __name__ == '__main__':
    app.run(debug=False)
