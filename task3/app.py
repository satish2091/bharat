from flask import Flask,request,render_template
import pickle as pkl
import numpy as np

app=Flask(__name__)
model = pkl.load(open('iris1.pkl','rb'))
@app.route("/")
def home():
    return render_template("home.html")


@app.route('/predict',methods=["POST","GET"])
def prdict():
    a=float(request.form.get('sl'))
    b=float(request.form.get('sw'))
    c=float(request.form.get('pl'))
    d=float(request.form.get('pw'))
    arr=np.array([[a,b,c,d]])
    data=model.predict(arr)
    print(data[0])
    return render_template("after.html",prediction=data[0])

if __name__ == "__main__":
    app.run(debug=True)
