# imports sqlite
import sqlite3

# connects it to the books-collection database
conn = sqlite3.connect('sqlite3_database.db')

# creates the cursor
c = conn.cursor()

# execute the query which creates the table called books with id and name  #as the columns


# executes the query which inserts values in the table

c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (23, '£15000','A trip to NewYork plus Cash' )   ")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (24, 'Flight Tickets','Plus $5000 Spending Money' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (25, '£4000','50% Reduction in Tuition Fees' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (26, '£25000','Research Grant From Microsoft' ) ")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (27, '£2000','University Allowance' ) ")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (28, '£7000','PostGraduate Scholarship' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (29, '£10000','IBM Masters Grant' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (30, '£26000','UN Scholarship allowance' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (31, '£2000','Maintenance allowance' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (32,'£7000','Alumni Award' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (33,'£82000','A Job with Facebook' )")
c.execute("INSERT INTO Present (ID,GIFT, DESCRIPTION)VALUES (34,'£17000','Google Award' )")
# commits the executions
conn.commit()

# closes the connection
conn.close()

