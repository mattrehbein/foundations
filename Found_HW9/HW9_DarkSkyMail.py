
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.get('https://api.darksky.net/forecast/************/40.7128,-74.0060')


# In[3]:


print(response)


# In[4]:


my_forecast = response.json()


# In[5]:


my_forecast.keys()


# In[6]:


my_forecast['currently'].keys()


# In[7]:


my_forecast['daily']['data'][0].keys()
print(my_forecast['daily']['data'][0]['precipProbability'])


# In[8]:


temperature = my_forecast['currently']['temperature']

summary = my_forecast['currently']['summary'].lower()

low_temp = my_forecast['daily']['data'][0]['temperatureHigh']
high_temp = my_forecast['daily']['data'][0]['temperatureLow']

if high_temp < 50:
    temp_feeling = "cold"
elif high_temp < 65:
    temp_feeling = "moderate"
elif high_temp < 80:
    temp_feeling = "warm"
elif high_temp > 81:
    temp_feeling = "hot"

rain = my_forecast['daily']['data'][0]['precipProbability']
if rain == 0:
    rain_warning = "No rain forecast for today!"
elif rain > 0.1 and rain < 0.5:
    rain_warning = "Bring your umbrella! It may rain today."
elif rain > 0.6:
    rain_warning = "Bring your umbrella! There's more than 50% chance of rain today."


# In[9]:


forecast_sentence = "Right now it is {} degrees out and {}. Today will be {} with a high of {} and a low of {}. {}".format(temperature, summary, temp_feeling, high_temp, low_temp, rain_warning)
print(forecast_sentence)


# In[10]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%b %d %Y")
print(date_string)


# In[11]:


response = requests.post(
        "https://api.mailgun.net/v3/****************.mailgun.org/messages",
        auth=("api", "************************"),
        data={"from": "Yourself! <mailgun@***************************.mailgun.org>",
              "to": ["matt.rehbein@gmail.com"],
              "subject": "8AM Weather Forecast:" + date_string,
              "text": forecast_sentence}) 
response.text

