from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
if("msg" not in locals()): msg = ""
@app.route('/', methods=['GET', 'POST'])
def main():
    if(request.method == "POST"):
        global msg
        msg = msg + str(request.form.get('share'))
        return render_template("index.html", data=msg)
    else:
        return render_template("index.html", data=msg)

if __name__ == '__main__':
    msg=""
    app.run(debug=True, host='localhost', use_reloader=True)