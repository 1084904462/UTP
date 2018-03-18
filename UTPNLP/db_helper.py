# -*- coding: utf-8 -*-

import pymysql
import db_pool

mysql_host = 'localhost'
mysql_port = 3306
mysql_user = 'root'
mysql_password = '123456'
mysql_db = 'utp'
mysql_charset = 'utf8'


def create_conn():
    return pymysql.Connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password,
                           database=mysql_db, charset=mysql_charset, autocommit=True)


def get_model_id():
    return 1


def get_keyword_ids(model_id):
    pool = db_pool.Pool(create_instance=create_conn)
    conn = pool.get()
    cur = conn.cursor()
    cur.execute("select id from keyword where model_id = %s", model_id)
    cur.close()
    conn.close()
    return cur.fetchall()


def get_patterns(keyword_id):
    pool = db_pool.Pool(create_instance=create_conn)
    conn = pool.get()
    cur = conn.cursor()
    cur.execute("""
    select B.word word,C.pattern pre_pattern,D.pattern gain_pattern,E.pattern aft_pattern 
    from gain_word_pattern_conn as A
    left join gain_word as B on A.gain_word_id = B.id
    left join pattern as C on A.pre_pattern_id = C.id
    left join pattern as D on A.gain_pattern_id = D.id
    left join pattern as E on A.aft_pattern_id = E.id
    where B.keyword_id = %s
    """, keyword_id)
    cur.close()
    conn.close()
    return cur.fetchall()


def get_separator():
    pool = db_pool.Pool(create_instance=create_conn)
    conn = pool.get()
    cur = conn.cursor()
    cur.execute("select word from separator_word order by id")
    cur.close()
    conn.close()
    return cur.fetchall()


def get_contents(model_id):
    pool = db_pool.Pool(create_instance=create_conn)
    conn = pool.get()
    cur = conn.cursor()
    cur.execute("select content.keyword_id, content.content from content,keyword where content.keyword_id = keyword.id and keyword.model_id = %s", model_id)
    cur.close()
    conn.close()
    return cur.fetchall()


def insert_in(item, values):
    doc = (item['title'], item['url'])
    pool = db_pool.Pool(create_instance=create_conn)
    conn = pool.get()
    cur = conn.cursor()
    cur.execute("insert into doc(title, link) values(%s, %s)", doc)
    doc_id = int(cur.lastrowid)
    for (keyword_id, content) in values:
        cur.execute("insert into content(keyword_id, content) values(%s, %s)", [keyword_id, content])
        content_id = int(cur.lastrowid)
        cur.execute("insert into doc_content_conn(doc_id, content_id) values(%s, %s)", [doc_id, content_id])
    conn.commit()
    cur.close()
    conn.close()
