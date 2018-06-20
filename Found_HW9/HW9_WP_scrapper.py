
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:


response = requests.get("http://washingtonpost.com")
soup_doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


stories = soup_doc.find_all(class_="moat-trackable")
    
# stories = doc.find_all("article", { 'class': 'story' })


# In[4]:


top_ten = []
for story in stories[8:18]:
    try:
        headline = story.find(class_="headline").find('a').text.strip()
    except:
        pass
    if headline:
        this_story = {'headline': headline}
        try:
            summary = story.find(class_="blurb").text.strip()
            if summary:
                this_story['summary'] = summary
        except:
            this_story['summary'] = "no summary"
        try:
            this_story['url'] = story.find(class_="headline").a['href']
        except:
            this_story['url'] = "no link"
        top_ten.append(this_story)

top_ten


# In[5]:


stories_df = pd.DataFrame(top_ten)
stories_df.to_csv("wp-data.csv")

datestring = time.strftime("%Y-%m-%d-%H-%M")

filename = "wp-data-" + datestring + ".csv"
stories_df.to_csv(filename, index=False)


# stories_df = pd.DataFrame(all_stories)
# stories_df.to_csv("nyt-data.csv")

# datestring = time.strftime("%Y-%m-%d-%H-%M")

# filename = "nyt-data-" + datestring + ".csv"
# stories_df.to_csv(filename, index=False)


# In[6]:


stories_df.head()


# In[7]:


email_timestamp = time.strftime("%-I%p")


# In[8]:


response = requests.post(
        "https://api.mailgun.net/v3/****************/messages",
        auth=("api", "*********************"),
        files=[("attachment", open(filename))],
        data={"from": "Yourself! <************************>",
              "to": ["matt.rehbein@gmail.com"],
              "subject": "Here is your " + email_timestamp + "briefing",
              "text": "See attached."}) 
response.text

