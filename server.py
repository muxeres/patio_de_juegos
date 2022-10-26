from flask import Flask, render_template

app=Flask(__name__)

@app.route("/",methods=['GET'])
def hola_mundo():
    return "hola mundo"

@app.route("/play",methods=['GET'])
def play():
    return render_template("index.html",num=3)

@app.route("/play/<int:num>",methods=['GET'])
def play_number(num):
    return render_template("index.html",num=num)

@app.route("/play/<int:num>/<string:color>",methods=['GET'])
def play_number_color(num,color):
    return render_template("index.html",num=num,color=color)

if __name__=="__main__":
    app.run(debug=True)
    
    #Karola.Codes