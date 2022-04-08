from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Olá Mundo!</h1>'


@app.route('/dashboard/<nome>')
def nome(nome):
  return f'Olá, {nome}'

if __name__ == '__main__':
  app.run(host='0.0.0.0')