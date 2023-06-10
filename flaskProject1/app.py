from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/store.html')
def store():  # put application's code here
    return render_template('store.html')

@app.route('/storequshi.html')
def storequshi():  # put application's code here
    return render_template('storequshi.html')

@app.route('/storeshehui.html')
def storeshehui():  # put application's code here
    return render_template('storeshehui.html')

@app.route('/storeqinggan.html')
def storeqinggan():  # put application's code here
    return render_template('storeqinggan.html')

@app.route('/productbuyi.html')
def productbuyi():  # put application's code here
    return render_template('productbuyi.html')

@app.route('/productdongzu.html')
def productdongzu():  # put application's code here
    return render_template('productdongzu.html')

@app.route('/productyaozu.html')
def productyaozu():  # put application's code here
    return render_template('productyaozu.html')



if __name__ == '__main__':
    app.run()
