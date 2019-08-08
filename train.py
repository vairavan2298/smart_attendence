from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index32(name=None):
    return render_template('index32.html',name=name)


@app.route('/exec2',methods = ['POST', 'GET'])
def exec2(name=None):
  if request.method == 'POST':
    exec2 = request.form
    import create_data
    print("done")
    return render_template('index32.html',name=name)

if __name__ == '__main__':
    app.run(host = '')
    app.debug = True