# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class BaikePipeline(object):
    def process_item(self, item, spider):

        host = '127.0.0.1'
        user = 'root'
        psd = 'mm'
        db = 'form'
        c = 'utf8'
        port = 3306

        # 数据库连接

        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)

        # 数据库游标

        cue = con.cursor()

     #   print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步

        dbTable = 'spider_baike'
     #   print(' ==> ',item['url'])

        checkSql = "select title from %s where title='%s'" % (dbTable,item['title'])

        cue.execute(checkSql)

    #    print('data : ', checkSql)

        data = cue.fetchone()

        try:

            if data:

                print('已存在。')

            else:

                content = pymysql.escape_string(item['content'])
                urlink = pymysql.escape_string(item['url'])

                sql = "insert into %s (content,title,url) values ('%s','%s','%s')" % (dbTable,content, item['title'], urlink)

                cue.execute(sql)

                print("insert success")  # 测试语句

        except Exception as e:

            print('Insert error:', e)

            con.rollback()

        else:

            con.commit()

        con.close()

        return item

    def close_spider(self, spider):

        print('爬虫结束...')