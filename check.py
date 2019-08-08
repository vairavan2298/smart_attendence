from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def check(name=None):
    return render_template('check.html',name=name)

@app.route('/execc')
#@app.route('/execc',methods = ['POST','GET'])
def execc(name= None):
  # if request.method == 'POST':
  #   execc = request.form
    import face_recognize
    print("done")
    return render_template("check.html",name= name)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    app.debug = True