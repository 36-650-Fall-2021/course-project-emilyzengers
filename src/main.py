# main.py
# This is your code's starting point
# Follow the guidelines in the homework document
# Don't forget to add data folder for your data
# Replace the following line with real application code

import psycopg2

import pandas as pd

# question 1

# select player name, 34 columns of skills, and overall with sql query 
# for loop to copy all 36 columns into an array - link 
# for loop to take the average of 34 columns for each row and compare it to the overall column 
# for loop to find the difference between overall and average
# sort function - sort list of lists (data structures lecture)
# display results with player name 

# conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))
# sql = "select count(*) from table;"
# dat = pd.read_sql_query(sql, conn)
# conn = None

# read in data
players20 = pd.read_csv("c:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_20.csv")
players19 = pd.read_csv("c:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_19.csv")

# select long name and overall columns
df1 = players20[["long_name", "overall"]]
df2 = players19[["long_name", "overall"]]

# merge dataframes so the same players are being displayed
common = df1.merge(df2, on = ["long_name"])

# rename columns
df3 = common.rename(columns={'overall_x': '2020_overall', 'overall_y': '2019_overall', 'long_name': 'Name'})

# add in difference column
df3['Difference'] = df3['2020_overall'] - df3['2019_overall']

# sort largest to smallest difference
df3 = df3.sort_values(by = 'Difference', ascending = False)

# 10 most improved players
df3.head(10)

# question 2
def num_clubs():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select count(club), club from fifa.players where contract_valid_until = 2021 group by club order by count(club) desc limit 5")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

num_clubs()

# question 3
def num_clubs_lim():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select count(club), club from fifa.players where contract_valid_until = 2021 group by club order by count(club) desc offset 5")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

num_clubs_lim()

# question 4
def team_position_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("SELECT team_position, count(*) FROM fifa.players where team_position != 'SUB' and team_position != 'RES' GROUP BY team_position ORDER BY count(*) DESC LIMIT 1")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

team_position_mode()

def nation_position_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select nation_position, count(*) from fifa.players where nation_position !='SUB' and nation_position != 'RES' group by nation_position order by count(*) desc limit 3")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

nation_position_mode()

# question 5
def nationality_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select mode() within group (order by nationality) from fifa.players")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

nationality_mode()
