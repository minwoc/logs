import psycopg2, bleach

db = psycopg2.connect("dbname=news")
c = db.cursor()

query1='''select articles.title, count(*) as num from articles
        join log on articles.slug=substring(log.path, 10)
        group by articles.title order by num desc limit 3'''

query2 = '''select authors.name, count(*) as num from authors join
        articles on authors.id=articles.author join log on
        substring(log.path, 10)=articles.slug group by authors.name order by num desc'''

query3= '''select * from answer where result>=1'''

'''create view e as select DATE(time), count(*) as num from log
        group by DATE(time), status having status='404 NOT FOUND' order by DATE(time)
            create view t as select DATE(time), count(*) as nums from log
        group by DATE(time) order by DATE(time)
            select e.date, (cast(e.num as decimal(5,0))/t.nums)*100 as result
        from e join t on e.date=t.date
            create view answer as select e.date, (cast(e.num as decimal(5,0))/t.nums)*100 as
        result from e join t on e.date=t.date
            select * from answer where result>=1'''

def run_query_function(query_satements):
    c.execute(query_satements)
    posts = c.fetchall()
    #db.close()
    return posts

def take_query_function(query):
    answer1 = run_query_function(query)
    i=0
    for answers in answer1:
        print '"' + str(answers[i]) + '"' + " - " + str(answers[i+1]) + " views"

print "What are the most popular three articles of all time?" +'\n', take_query_function(query1)
print "Who are the most popular article authors of all time?" + '\n', take_query_function(query2)
print "On which days did more than 1% of requests lead to errors?" + '\n', take_query_function(query3)
print "success!"
