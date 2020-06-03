# python cal.py

# Imports 
import pandas as pd
import os

# Data files
path_states = os.path.join(os.getcwd(),"data/states.csv")
path_devices = os.path.join(os.getcwd(),"data/devices.csv")

# Check if file path exixt
#os.path.exists(path_states)

# Read in csvs
states = pd.read_csv(path_states)
devices = pd.read_csv(path_devices)
# Check shape
#print(states.shape)
#print(devices.shape)

# Calculate Energy Function
def calculator(device,state,hours,days):
  '''
  This function calculates how much energy a device uses per year
  and how much it will cost on a yearly basis based on the state you live.

  Example: The typically wattage level of a ceiling fan 
  is 65 watts. The average utility rate in
  Missouri is $.0928/kWh. If you use your fan for
  eight hours (8) a day for 5 days a week, 
  that's a total of 135.2 kWh, 
  and would cost $12.55 a year. 

  energy_used = (65 * 8 * (5*52)) / 1000
  cost_per_year = energy_used * .0928
  '''
  # Check values
  valid_hours= range(0,25)
  if hours > 24:
    raise ValueError ("calculator: hours must be between %r." % valid_hours)
  valid_days = {0,1,2,3,4,5,6,7} #<class 'set'>
  if days not in valid_days:
    raise ValueError ("calculator: days must be one of %r." % valid_days)
  
  # Function
  device = device
  wattage = devices[devices["device"]== device]["wattage"].item()
  state = state 
  utility_rate = states[states["state"]== state]["rate"].item()
  hours_per_day = hours
  days_per_year = days * 52
  watts_per_kilowatt = 1000

  energy_used = (wattage*hours_per_day*days_per_year)/watts_per_kilowatt
  cost_per_year = round(energy_used* utility_rate,2)

  return {"energy_used": energy_used, "cost_per_year": cost_per_year}

if __name__ == "__main__":
    # Test
    print(calculator("Ceiling Fan","Missouri",8,5))
