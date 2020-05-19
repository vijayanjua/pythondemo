import mysql.connector as db
mydb=db.connect(host='localhost',user='root',passwd='',database='studentdb')
mycursor=mydb.cursor()
mycursor.execute('select * from students')
#result=mycursor.fetchall()
result=mycursor.fetchone()
for i in result:
    print(i)


