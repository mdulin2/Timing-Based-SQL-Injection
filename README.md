# SQL Injections
I started experimenting with SQL injections of a much more difficult nature. With the blog, it's capable of stealing a ton of information, because it does pass back information. But, a login script does.   
So, the login script used a timing based approach. If the item is found in the database, then the query is told to sleep in an if statement.  
