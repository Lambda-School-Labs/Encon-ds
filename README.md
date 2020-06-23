# Encon 2020  
You can find the project at [Encon DS API](https://environment-2.eba-j6sk9zsp.us-east-1.elasticbeanstalk.com/)  
## Contributors  
### Labs24  
|Avery Quinn| Gagan Singh |Iulia Stremciuc|
|:----: | :----: | :----: |
|[<img src="https://ca.slack-edge.com/ESZCHB482-W012JQ43VK5-a88ed1ada5a4-512" width = "200" />](https://github.com/Avery1493)|[<img src="https://ca.slack-edge.com/ESZCHB482-W012X6X608Z-7309c1c2dcc5-512" width = "200" />](https://github.com/gagansingh23)|[<img src="https://ca.slack-edge.com/ESZCHB482-W012H6RLYAH-b0a1e701122c-512" width = "200" />](https://github.com/iuliastremciuc)|
|[ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/avery-quinn-a178431a2/)|[ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](http://www.linkedin.com/in/gagandeep-singh-8940821b1)|[ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/iulia-stremciuc-4593191a1/)|  

## Project Overview   
Encon is a application that can help users calculate the cost in dollars and energy consumed in kWh of common household appliances. Through the app, users will also be able to track their daily energy usage of certain appliances.  
[Trello Board](https://trello.com/b/OnnuxZCX/labs24-energy-consumption)  
[Product Canvas](https://www.notion.so/4c573713f21647ca9cec848dfc790263?v=a9bbd8982fad4bf68cdaedd7ecda81f7)  
[Deployed Front End](https://master.d3dr1o3e9t60pz.amplifyapp.com/)

## Tech Stack  
* Python 3  
* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)  
* [Resnet50](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet50)

## Calculator Function  
```cal.py```  
You can test out the function by using the url to insert inputs:  
```/<device>/<state>/<hours>/<days>```  
```https://environment-2.eba-j6sk9zsp.us-east-1.elasticbeanstalk.com/Ceiling%20Fan/Missouri/8/5```  
Where device and state match options in coresponding csv files; hours (0-24); days of the week (0-7)

## Image Detection  
```resnet.py```  
```decode.py```

**Postman API Request Examples**  
<img src="https://github.com/Avery1493/Avery1493.github.io/blob/master/img/enconpostman.PNG" width="600" />  
API Request Route:  
```
https://environment-2.eba-j6sk9zsp.us-east-1.elasticbeanstalk.com/
```
API POST Request:  
```
{
    "imgb64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD//...
{
```
API Response:  
```
[
    "comic_book",
    "Image is not a common household appliance. Please select a different picture."
]
```  
**or**  
```
[
    "laptop",
    "Laptops are 50% more energy efficient than computer desktops. Laptops offer power saving features such as standby mode or sleep mode which will help reduce the energy when not using the device. Also unplug laptop chargers when not using them as even when plugged they are absorbing standby power"
]
```

## DS API Routes  
You can find the project at [Encon DS API](https://environment-2.eba-j6sk9zsp.us-east-1.elasticbeanstalk.com/)
|Route| Description|
|:---|:---|
|`/`| Home: Shows list of devices that can be used in the calculator function |
|`/calculator`| Calculator: Form page to calculate energy cost per year and total energy used |
|`/<device>/<state>/<hours>/<days>`| Alternative Calculator route without form  |
|`/upload`| Upload: Button to upload image that will run through Resnet Model |
|`/image`| Image: Post route - will take json key[imgb64], value[encode image as base64] |

