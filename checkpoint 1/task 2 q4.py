# question 4
def team_position_mode():
    conn = psycopg2.connect(host="localhost", 
                    port="5432", 
                    user="postgres", 
                    password="114645", 
                    database="postgres")
    
    cur = conn.cursor()
    cur.execute("select mode() within group (order by team_position) from fifa.players")
    
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
    cur.execute("select mode() within group (order by nation_position) from fifa.players")
    
    print("\n\n Formatted Results:")
    for row in cur:
        print (row)

    cur.close()
    conn.close()

nation_position_mode()
