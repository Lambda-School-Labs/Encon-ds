from flask import Flask, request, jsonify
from flask import render_template, make_response
import pandas as pd
import os

# Data files
path_states = os.path.join(os.getcwd(),"data/states_data.csv")
path_devices = os.path.join(os.getcwd(),"data/devices_data.csv")
# Check if file path exixt
#os.path.exists(path_states)
# Read in csvs
states = pd.read_csv(path_states)
states["rate"] = (states["rate"]/100)
devices = pd.read_csv(path_devices)
# Check shape
# print(states.shape)
# print(devices.shape)

app = Flask(__name__)


def calculate(device, state, hours, days):
    device = device
    wattage = devices[devices["device"] == device]["wattage"].item()
    state = state 
    utility_rate = states[states["state"] == state]["rate"].item()
    hours_per_day = hours
    days_per_year = days * 52
    watts_per_kilowatt = 1000

    energy_used = (wattage*hours_per_day*days_per_year)/watts_per_kilowatt
    cost_per_year = round(energy_used* utility_rate,2)

    return(energy_used, cost_per_year)

@app.route('/', methods = ['GET', 'POST'])
def Welcome():
    return "Welcome to EnCon"


@app.route('/calculate/<device>/<state>/<hours>/<days>', methods = ['GET', 'POST'])
def show_result(device, state, hours, days):
    device = str(device)
    state = str(state)
    hours = int(hours)
    days = int(days)
    # x = {"device": device,"state": state,"hours": hours,"days": days}
    # y = calculate(device,state,hours,days)
    # return {"inputs": x, "outputs": y}
    result = calculate(device, state, hours, days)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
 