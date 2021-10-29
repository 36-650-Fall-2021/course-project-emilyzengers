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