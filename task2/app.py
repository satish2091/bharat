from flask import Flask , request , render_template
import pickle as pkl
import numpy as np

model=pkl.load(open("winequality.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict",methods=["GET","POST"])
def predict():
    a1=request.form.get('a')
    a2=request.form.get('b')
    a3=request.form.get('c')
    a4=request.form.get('d')
    a5=request.form.get('e')
    a6=request.form.get('f')
    a7=request.form.get('g')
    a8=request.form.get('h')
    a9=request.form.get('i')
    a10=request.form.get('j')
    a11=request.form.get('k')


    a1=float(a1)
    a2=float(a2)
    a3=float(a3)
    a4=float(a4)
    a5=float(a5)
    a6=float(a6)
    a7=float(a7)
    a8=float(a8)
    a9=float(a9)
    a10=float(a10)
    a11=float(a11)


    wine=np.array([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11]])
    print(wine)
    data=model.predict(wine)
    return render_template('after.html',prediction=data[0])

if __name__ == "__main__":
    app.run(debug=True)