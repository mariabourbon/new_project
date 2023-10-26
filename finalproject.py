#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.atptour.com/en/stats/aces"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response = requests.get(url, headers=headers)

response


# In[3]:


soup = BeautifulSoup(response.content, "html.parser")
type(soup)


# In[4]:


soup.find("title")


# In[5]:


soup.find_all("title")[0].get_text().strip()


# In[6]:


#Web Scraping Page Aces

table = soup.find_all("div", attrs = {"class":"stats-listing-wrapper"}) 
table


# In[7]:


table = soup.find_all("tr", attrs = {"class":"stats-listing-row"})
tennis_dict = {}
index = 0

for element in table:
    name = element.find("td", {"class": "stats-listing-name"}).get_text().strip()
    numbers = element.find_all("td", {'data-type': 'N0'})[0].get_text()
    matches = element.find_all("td", {'data-type': 'N0'})[1].get_text()

    tennis_dict[index] = {
        "name": name,
        "numbers": numbers,
        "number of matches": matches
    }
    index += 1


tennis_df_aces = pd.DataFrame.from_dict(tennis_dict, orient="index")
tennis_df_aces


# In[8]:


aces_top5_df = tennis_df_aces[0:6] # top 5 dos Aces
aces_top5_df


# In[9]:


# WEB SCRAPING PAGE BREAK POINTS


# In[10]:


url1 = "https://www.atptour.com/en/stats/break-points-saved"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response1 = requests.get(url1, headers=headers)

response1


# In[11]:


soup1 = BeautifulSoup(response1.content, "html.parser")
type(soup1)


# In[12]:


soup1.find_all("title")[0].get_text().strip()


# In[13]:


table1 = soup1.find_all("div", attrs = {"class":"stats-listing-wrapper"}) 
table1


# In[14]:


data1_list = []


for table in table1:
    table_element = table.find('table', class_='stats-listing-table')
    rows = table_element.find_all('tr', class_='stats-listing-row')

    for row in rows:
        cells = row.find_all('td', {'data-type': 'N0'})  

        name = row.find('a').get_text()
        percentage = row.find('td', {'data-type': 'N2'}).get_text()
        points_won = cells[0].get_text()
        total_points = cells[1].get_text()
        matches = cells[2].get_text()

        data1_list.append({
            "Name": name,
            "Percentage": percentage,
            "Points Won": points_won,
            "Total Points": total_points,
            "Matches": matches
        })

tennis_df = pd.DataFrame(data1_list)


tennis_df


# In[15]:


top5_breakpoints = tennis_df[0:6]
top5_breakpoints


# In[16]:


#WEB SCRAPING SERVICE GAMES WON


# In[17]:


url2 = "https://www.atptour.com/en/stats/service-games-won"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response2 = requests.get(url2, headers=headers)

response2


# In[18]:


soup2 = BeautifulSoup(response2.content, "html.parser")
type(soup2)


# In[19]:


soup2.find_all("title")[0].get_text().strip()


# In[20]:


table2 = soup2.find_all("div", attrs = {"class":"stats-listing-wrapper"}) 
table2


# In[21]:


data2_list = []

for div in table2:
    table_element = div.find('table', class_='stats-listing-table')

    rows = table_element.find_all('tr', class_='stats-listing-row')

    for row in rows:
        cells = row.find_all('td', {'data-type': 'N0'})  

        name = row.find('a').get_text()
        percentage = row.find('td', {'data-type': 'N2'}).get_text()
        games_won = cells[0].get_text()
        total_games = cells[1].get_text()
        matches = cells[2].get_text()

        data2_list.append({
            "Name": name,
            "Percentage": percentage,
            "Games Won": games_won,
            "Total Games": total_games,
            "Matches": matches
        })

tennisservice_df = pd.DataFrame(data2_list)
tennisservice_df


# In[22]:


top5_service =tennisservice_df[0:6]
top5_service


# In[23]:


#WEB SCRAPING RETURN GAMES WON


# In[24]:


import requests
url3 = "https://www.atptour.com/en/stats/return-games-won"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

response3 = requests.get(url3, headers=headers)

response3


# In[25]:


soup3 = BeautifulSoup(response3.content, "html.parser")
type(soup3)


# In[26]:


soup3.find_all("title")[0].get_text().strip()


# In[27]:


table3 = soup3.find_all("div", attrs = {"class":"stats-listing-wrapper"}) 
table3


# In[28]:


data_list = []

for table in table3:
    table_element = table.find('table', class_='stats-listing-table')

    rows = table_element.find_all('tr', class_='stats-listing-row')

    for row in rows:
        cells = row.find_all('td', {'data-type': 'N0'})  

        name = row.find('a').get_text()
        percentage_element = row.find('td', {'data-type': 'N2'})
        percentage = percentage_element.get_text() if percentage_element else None
        games_won = cells[0].get_text()
        total_games = cells[1].get_text()
        matches = cells[2].get_text()

        data_list.append({
            "Name": name,
            "Percentage": percentage,
            "Games Won": games_won,
            "Total Games": total_games,
            "Matches": matches
        })

tennis_df = pd.DataFrame(data_list)
tennis_df


# In[29]:


top5return_df = tennis_df[0:6]
top5return_df


# In[30]:


import os


# In[31]:


#pip install tk pillow


# In[33]:


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

print("Hello! I hope you share the same passion for tennis as we do!\n Today, you can select from a range of categories to focus on, helping you improve your game.\n Additionally, you can uncover the top players in the rankings for that category.\n Which category would you like to explore and enhance your knowledge in?\n The categories are: aces,break_points,service_game_won and return_game_won. ")

def display_info_with_image(info_text, image_path, dataframe, video_link):
    root = tk.Toplevel()

    
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    image_label = ttk.Label(root, image=image)
    image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

    
    text_label = ttk.Label(root, text=info_text, wraplength=300, justify='left')
    text_label.grid(row=0, column=1, sticky='w', padx=10, pady=10)

    
    dataframe_frame = ttk.Frame(root)
    dataframe_frame.grid(row=1, column=1, columnspan=2, sticky='w', padx=10, pady=10)
    dataframe_table = ttk.Treeview(dataframe_frame, columns=list(dataframe.columns), show='headings')
    for col in dataframe.columns:
        dataframe_table.heading(col, text=col)
    for index, row in dataframe.iterrows():
        dataframe_table.insert("", "end", values=list(row))
    dataframe_table.pack()

    def open_youtube():
        webbrowser.open_new(video_link)
    
    button = ttk.Button(root, text="Watch Video", command=open_youtube)
    button.grid(row=2, column=1, sticky='w', padx=10, pady=10)

    root.mainloop()

def categorychosen():
    while True:
        category_chosen = input(f"Enter one of them: ")
        if category_chosen == "aces":
            info_text = "John Isner holds the record for the most aces, boasting an impressive 14,470 aces across 772 matches. An intriguing fact: Isner delivered a staggering 113 aces during his marathon 11-hour battle with Nicolas Mahut in 2010, setting the record for the most aces in a single match."
            image_path = os.path.abspath('fotoaces.png')
            video_link = "https://www.youtube.com/watch?v=ue0M7ki9G1w"
            display_info_with_image(info_text, image_path, aces_top5_df, video_link)
            return aces_top5_df
            break
        elif category_chosen == "break_points":
            info_text = "Ivo Karlovic is the standout player when it comes to breaking points, securing 1,879 won points out of a total of 2,648. This remarkable achievement spans across 694 matches, showcasing his prowess in this crucial aspect of the game."
            image_path = os.path.abspath('breakpoints.png')
            video_link = "https://www.youtube.com/watch?v=uOAeGl-miB8"
            display_info_with_image(info_text, image_path, top5_breakpoints, video_link)
            return top5_breakpoints
            break
        elif category_chosen == "service_game_won":
            info_text = "Ivo Karlovic takes the top spot with an impressive 92.00% of service games won. He has won a total of 8,845 games across 694 matches, underscoring his dominance in this aspect of the game."
            image_path = os.path.abspath('servicewon.png')
            video_link = "https://www.youtube.com/watch?v=hkO-yo3YJ4o"
            display_info_with_image(info_text, image_path, top5_service, video_link)
            return top5_service
            break
        elif category_chosen == "return_game_won":
            info_text = "In the category of return_game_won, Guillermo Coria emerges as the top performer, securing a notable 35.19% success rate with 1,355 games won out of a total of 3,580 games played across 323 matches."
            image_path = os.path.abspath('returnwon.png')
            video_link = "https://www.youtube.com/watch?v=ds-ZoJDhU6U"
            display_info_with_image(info_text, image_path, top5return_df, video_link)
            return top5return_df
            break
        else:
            print("Please return a valid category")


categorychosen()


# In[ ]:




