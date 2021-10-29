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
