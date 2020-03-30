import flask
import datetime
import requests
import json

app = flask.Flask(__name__)


@app.route('/covidData', methods=('GET', 'POST'))
def get_data():

    country_input = flask.request.args.get('country')
    date_input = flask.request.args.get('date')
    date_split = date_input.split("-")
    date = datetime.datetime(int(date_split[2]),  int(date_split[0]), int(date_split[1])).strftime('%m-%d-%Y')

    data = requests.get('https://covid19.mathdro.id/api/daily/' + date)
    processed_data = data.json()

    for country in processed_data:
        if country['countryRegion'] == country_input:
            target_country = country

    requested_data = {"Country": target_country['countryRegion'], "Cases": target_country["confirmed"], "Recovered": target_country["recovered"], "Died": target_country["deaths"]}

    return flask.jsonify(requested_data)


if __name__ == '__main__':
    app.run(port=5000)
