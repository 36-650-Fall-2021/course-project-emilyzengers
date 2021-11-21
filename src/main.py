# main.py
# This is your code's starting point
# Follow the guidelines in the homework document
# Don't forget to add data folder for your data
# Replace the following line with real application code

#!/usr/bin/env python
# coding: utf-8

# ### task ii

# In[8]:


# import libraries

import psycopg2

import pandas as pd


# In[24]:


# question 1
# List the x players who achieved highest improvement across all skillsets

# create connection to postgres database and get data from players20 and players19 tables
conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
sql1 = "select * from fifa.players20;"
sql2 = "select * from fifa.players19;"
players20 = pd.read_sql_query(sql1, conn)
players19 = pd.read_sql_query(sql2, conn)
conn = None

def most_improvement(x):
    # check to make sure x is an integer
    if isinstance(x, int) is not True:
        return("Must input integer")
    
    # check to make sure x is not zero or negative
    if x <= 0:
        return "The number of players to display must be a postive integer"
    
    # select long name, overall, and sofifa (unique) id from players20
    # select sofifa id and overall from players19
    df1 = players20[["sofifa_id", "long_name", "overall"]]
    df2 = players19[["sofifa_id", "overall"]]
    
    # merge dataframes on sofifa id so the same players are being compared
    common = df1.merge(df2, on = ["sofifa_id"])

    # rename columns
    df3 = common.rename(columns={'sofifa_id': 'Sofifa ID', 'overall_x': '2020 Overall', 'overall_y': '2019 Overall', 'long_name': 'Name'})

    # add in difference column
    df3['Difference'] = df3['2020 Overall'] - df3['2019 Overall']

    # sort largest to smallest difference
    df3 = df3.sort_values(by = 'Difference', ascending = False)

    df3 = df3.reindex(columns=['Sofifa ID', 'Name', '2019 Overall', '2020 Overall', 'Difference'])
    
    df3 = df3.head(x)
    
    # convert dataframe to list
    most_improved = df3.values.tolist()
    return most_improved

most_improvement(5)


# In[25]:


# question 2
# What are the y clubs that have largest number of players with contracts ending in 2021?

def num_clubs(y):
    # check to make sure y is an integer
    if isinstance(y, int) is not True:
        return("Must input integer")
    
    # check to make sure y is not zero or negative
    if y <= 0:
        return "The number of clubs to display must be a postive integer"
    
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select count(club), club from fifa.players20 where contract_valid_until = 2021 group by club order by count(club) desc")
    
    # create empty list 
    list = []
    for row in cur:
        list.append(row)
    
    # return list of y clubs that have largest number of players with contracts ending in 2021
    return list[:y]

    cur.close()
    conn.close()

num_clubs(3)


# In[20]:


# question 3
# List the z clubs with largest number of players in the dataset where z >= 5

def num_clubs_lim(z):
    # z has to be at least 5, z >=5
    if z < 5:
        return "The number of clubs to display should at least be 5"
    
    # check to make sure z is an integer
    if isinstance(z, int) is not True:
        return("Must input integer")
    
    # check to make sure z is not zero or negative
    if z <= 0:
        return "The number of clubs to display must be a postive integer"
    
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select count(club) as number_of_players, club from fifa.players20 group by club order by count(club) desc")
    
    # create empty list 
    list = []
    for row in cur:
        list.append(row)
        
    # return list of z clubs with largest number of players in the dataset where z >= 5
    return list[:z]

    cur.close()
    conn.close()

num_clubs_lim(10)


# In[89]:


# question 4
# What is the most popular nation_position and team_position in the dataset? (list the most popular for each)

def team_position_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("SELECT team_position, count(*) FROM fifa.players20 where team_position != 'SUB' and team_position != 'RES' GROUP BY team_position ORDER BY count(*) DESC LIMIT 1")
    
    # create empty list 
    list = []
    for row in cur:
        list.append(row)
        
    # return list of most popular team position that doesn't include substitute or reserve
    return list

    cur.close()
    conn.close()

team_position_mode()


# In[55]:


# question 4 continued
def nation_position_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select nation_position, count(*) from fifa.players20 where nation_position !='SUB' and nation_position != 'RES' group by nation_position order by count(*) desc limit 3")
    
    # create empty list 
    list = []
    for row in cur:
        list.append(row)
        
    # return list of most popular nation position that doesn't include substitute or reserve
    return list

    cur.close()
    conn.close()

nation_position_mode()


# In[56]:


# question 5
# What is the most popular nationality for the players in the dataset?

def nationality_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select nationality, count(nationality) as number_of_players from fifa.players20 group by nationality order by number_of_players desc limit 1;")
    
    # create empty list 
    list = []
    for row in cur:
        list.append(row)
        
    # return list of most popular nationality
    return list

    cur.close()
    conn.close()

nationality_mode()


