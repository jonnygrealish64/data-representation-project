from flask import Flask

app = Flask(__name__, static_url_path = '', static_folder = '../')

@app.route('/games')
def getAll():
    return "in getAll"

@app.route('/games/<int:year>')
def findByYear(year):
    return "in find by Year for year" + str(year)

@app.route('/games', methods = ['POST'])
def create():
    return "in create" + str()

@app.route('/games/<int:year>', methods = ['PUT'])
def update(year):
    return "in update for year" + str(year)

@app.route('/games/<int:year>', methods = ['DELETE'])
def delete(year):
    return "in delete for year" + str(year)

if __name__ == '__main__':
    app.run(debug = True)