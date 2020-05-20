import pandas as pd
import os

# Data files
path_states = os.path.join(os.getcwd(),"data/states_dataset.csv")
path_devices = os.path.join(os.getcwd(),"data/devices_dataset.csv")
# Check if file path exixt
#os.path.exists(path_states)
# Read in csvs
states = pd.read_csv(path_states)
states["rate"] = (states["rate"]/100)
devices = pd.read_csv(path_devices)


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


if __name__ == '__main__':
    print(calculate('Iron', 'Montana', 1, 100))