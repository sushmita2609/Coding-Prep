DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "Sush7879"


import psycopg2
conn = psycopg2.connect(dbname= DB_NAME, user=DB_USER, password = DB_PASS, host= DB_HOST)
cur = conn.cursor()
#cur.execute("CREATE TABLE STUDENT1(NAME VARCHAR,PLACE VARCHAR, ID SERIAL PRIMARY KEY, AGE INT);")
#cur.execute("INSERT INTO STUDENT1 (NAME, PLACE, ID, AGE) VALUES (%s, %s, 1107, 22)",("Gaurav","hyderabad"))
s1 = cur.execute("SELECT * FROM STUDENT1 WHERE PLACE = '%s'" % (pune)
#t1 = s1.fetchall()
#print(t1[0])
#cur.execute("DROP TABLE STUD")
#cur.execute("UPDATE STUDENT1 SET AGE = 18 WHERE ID = 1103")
#cur.execute("SELECT * FROM STUDENT1;")
print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
