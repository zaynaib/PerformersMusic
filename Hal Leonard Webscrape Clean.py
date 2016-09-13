
# coding: utf-8

# In[30]:

from bs4 import BeautifulSoup
import requests


# In[43]:

url = "http://www.halleonard.com/product/viewproduct.action?itemid=306850&subsiteid=1&&viewtype=instruments"
r=requests.get(url)

#request the webpage


# In[44]:

data= r.text  #put the request in usuable text
soup = BeautifulSoup(data) #create your soup data object based on information from the request


# In[45]:

tdTag = soup.find_all("td", {"class":"productContent"})


# In[46]:

for tag in tdTag:
    ulTags = tag.find_all("ul")
    for tags in ulTags:
        print(tags.text)


# In[49]:

def createUrl(halLeonardItemNumber):
    url = "http://www.halleonard.com/product/viewproduct.action?itemid=" + str(halLeonardItemNumber) + "&subsiteid=1&&viewtype=instruments"
    return url


# In[58]:

myUrl = createUrl(48002589)


# In[74]:

def getInstrumentation(halLeonardUrl):
    r=requests.get(halLeonardUrl) #request the html page from Hal Leonard site
    data= r.text  #put the request in usuable text
    soup = BeautifulSoup(data) #create your soup data object so you can parse through the html
    instruments = None #this is the text we are going to return
    tdTag = soup.find_all("td", {"class":"productContent"}) #find all the td tags that have the class productContent
    for tag in tdTag: #loop through all the td tags
        ulTags = tag.find_all("ul") #find the one that has an unordedlist (ul)
        for tags in ulTags: #within the ul tag get all the instrumentation text and get rid of the new line character\n
            instruments = tags.text.strip()
    
    instruments = instruments.replace("\n", " ") #get rid of the \n inside the text

    
    return instruments #return all the instruments for that book
    

    


# In[60]:

print(type(getInstrumentation(myUrl)))


# In[67]:

getInstrumentation(myUrl)


# In[75]:

getInstrumentation(myUrl)


# In[ ]:



