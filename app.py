from flask import Flask
from flask import redirect
import requests

app = Flask(__name__)

url = 'https://icanhazdadjoke.com'
headers = {'Accept': 'applicati/js'}


@app.route('/')
def index():
    return redirect(f'/dadjoke')

@app.route('/dadjoke')
def get_joke():
   
    respse = requests.get(url=url, headers=headers,)
        data = respse.js()
            return data


        @app.route('/dadjoke/search/<string:srch_term>')
        def joke_search(srch_term):
                srch_url = url + '/search'
                    params = dict(
                                    term = srch_term,
                                        )

                        respse = requests.get(url=srch_url, params=params, headers=headers)
    data = respse.js()
    return data

@app.route('/dadjoke/j/<string:joke_code>')
def joke_code(joke_code):
    srch_url = url + '/j/' + joke_code
    respse = requests.get(url=srch_url, headers=headers)
        data = respse.js()
            return data

        if __name__ == '__main__':
                app.run(host="0.0.0.0", port=3000)
