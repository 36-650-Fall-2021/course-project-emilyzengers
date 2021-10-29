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