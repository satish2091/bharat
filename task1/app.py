from flask import Flask , request , render_template
import pickle as pkl
import numpy as np

model=pkl.load(open("houseprice.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])
def prdict():
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
    a12=request.form.get('l')
    a13=request.form.get('m')
    a14=request.form.get('n')


    a1=int(a1)
    a2=float(a2)
    a3=int(a3)
    a4=float(a4)
    a5=int(a5)
    a6=int(a6)
    a7=int(a7)
    a8=int(a8)
    a9=int(a9)
    a10=int(a10)
    a11=float(a11)
    a12=float(a12)
    a13=int(a13)
    a14=int(a14)


    house=np.array([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14]])
    print(house)
    data=model.predict(house)
    return render_template("after.html",prediction=round(data[0],2))

if __name__ == "__main__":
    app.run(debug=True)