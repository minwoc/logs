ABOUT:
This project scopes into fundamentals of database backend concepts. Goal is to take the database
and utilize SQL skills to breakdown that database into an information we want to see.
In this case, we have taken database from news company to discover most popular articles, authors, and server log for sites.

Tools:
python3
vagrant
virtual box

Set Up:
Install vagrant and virtual machine on your computer.

Run Outputs:
1. Change directory into vagrant directory.
2. Open up command line.
3. Run vagrant ssh.
4. Type Python logs.py to display output of your python code.

Load Data:
1. Type in psql -d news into your terminal

Views:
I solved the last problem using views. It reads:
create view e as select DATE(time), count(*) as num from log
        group by DATE(time), status having status='404 NOT FOUND' order by DATE(time)
            create view t as select DATE(time), count(*) as nums from log
        group by DATE(time) order by DATE(time)
            select e.date, (cast(e.num as decimal(5,0))/t.nums)*100 as result
        from e join t on e.date=t.date
            create view answer as select e.date, (cast(e.num as decimal(5,0))/t.nums)*100 as
        result from e join t on e.date=t.date
            select * from answer where result>=1
