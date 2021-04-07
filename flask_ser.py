 
 
# client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster-yu.ixch7.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test
from flask import Flask,Response
import pymongo
import json
from bson import json_util

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster-yu.ixch7.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
coll = db.XXXX
# try:
# except:
#     pass

@app.route('/users',methods=['GET'])
def List_user():
    try:
        data = list(coll.find({}))
        print(data)
        # return json.dumps(data,ensure_ascii=False,default=json_util)
        return json.dumps(f'{data}',ensure_ascii=False,default=json_util)
    except Exception as ex:
        print(ex)
        return  Response(response = json.dumps({'massage':'user connot read user ....'}),status = 200,mimetype = 'application/json') 

@app.route('/hi')
def Hello():
    return "Hi is kankan!"
if __name__ == '__main__':
    app.run(port=4000,debug=True)
