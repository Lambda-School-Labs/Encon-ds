# Encon--DS

## RC1 - Energy Consumption Calculator  
We created a calculator for residentual users to be able to figure out how much energy typical appliance and devices in their home use.

**Setting Up Environment**    
```requirements.txt```

**Data**  
Average state utility rate as of 2019 ```data/states.csv```  
List of common household devices and typical wattage level they use ```data/devices.csv```

**Calculator Function**  
```cal.py```

**Server:** Flask Ask  
```from flask import Flask```  
```app = Flask(__name__)```  
Commands on Windows: ```set FLASK_APP=app.py``` ```flask run```

**Heroku Deployment**  
Procfile ```web: gunicorn app:app```  
https://encon.herokuapp.com/  
https://encon.herokuapp.com/Iron/Missouri/8/5  

You can test out the function by using the url to insert inputs:  
```/<device>/<state>/<hours>/<days>``` 
Where device and state match options in coresponding csv files; hours (0-24); days of the week (0-7)

**AWS Deployment** (coming soon)
