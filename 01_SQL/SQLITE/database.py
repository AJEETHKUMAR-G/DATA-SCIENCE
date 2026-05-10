import sqlite3 as aju

# create connection 

conn = aju.connect('customer.db')

# create cursor

c = conn.cursor()

# create table 

# c.execute("""CREATE TABLE customers(
# 		name text,
# 		address text,
# 		email_address text
# )""")

# insert one record

#c.execute("INSERT INTO customers VALUES('krishna','22 kammapatti','krish@gmail.com')")

# insert many record

# recs = [
# 		('tim','las vegas','tim@gmail.com'),
# 		('corey','las angeles','corey@gmail.com'),
# 		('codemy','mexico','codemy@gmail.com')
# 		]
# c.executemany("INSERT INTO customers VALUES (?,?,?)",recs)


# query records

#c.execute("SELECT * FROM customers")
# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchmany(3))

# formating 

# print(c.fetchone()[2])
#item  = c.fetchall()

# for i in item:
# 	print(i)

# for i in item:
	# print(i[2])

# print("Name"+"\tAddress"+" \tEmail")
# print("---------------------")
# for i in item:
# 	print(i[0]+"\t"+i[1]+"\t\t"+i[2])

# print("Name"+"\tAddress")
# print("---------------------")
# for i in item:
# 	print(i[0]+"\t"+i[1])


#primary key

# c.execute("SELECT rowid,* FROM customers")

# item = c.fetchall()
# for i in item:
# 	print(i)


#where clause

#c.execute("SELECT rowid,* FROM customers WHERE name='krishna'")
# c.execute("SELECT * FROM customers WHERE address LIKE 'la%'")
# c.execute("SELECT rowid,* FROM customers WHERE email_address LIKE '%y@gmail.com'")

# item = c.fetchall()
# for i in item:
# 	print(i)


#update

# c.execute("UPDATE customers SET address='kammapatti' WHERE rowid=3")
# conn.commit()

# c.execute("SELECT * FROM customers")
# item = c.fetchall()
# for i in item:
# 	print(i)

#delete

# c.execute("DELETE FROM customers WHERE rowid=3")
# conn.commit()

# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for i in items:
# 	print(i)


#order by

# c.execute("SELECT * FROM customers ORDER BY name")
# c.execute("SELECT * FROM customers ORDER BY name DESC")
# items  = c.fetchall()
# for i in items:
# 	print(i)

#and/or

#c.execute("SELECT * FROM customers WHERE name LIKE 'k%' AND address='kammapatti'")
# c.execute("SELECT * FROM customers WHERE name LIKE 'c%' or name LIKE 'a%'")
# items = c.fetchall()
# for i in items:
# 	print(i)


#limit

# c.execute("SELECT * FROM customers LIMIT 3")
c.execute("SELECT * FROM customers ORDER BY name DESC LIMIT 3 ")
items = c.fetchall()
for i in items:
	print(i)


# commit 

conn.commit()
#print("processed successfully..")


# close connection

conn.close() 