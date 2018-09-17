# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

class WeixinPipeline(object):
	def process_item(self, item, spider):
		host = settings['MYSQL_HOSTS']
		user = settings['MYSQL_USER']
		psd = settings['MYSQL_PASSWORD']
		db = settings['MYSQL_DB']
		c=settings['CHARSET']
		port=settings['MYSQL_PORT']
#数据库连接
		con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
#数据库游标
		cue=con.cursor()
		print("mysql connect succes")#测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
		
		checkSql = "select title from weixin_spider where title='%s'" % (item['title'])
		
		cue.execute(checkSql)
	#	print('data : ',checkSql)
		
		data = cue.fetchone()
	
		try:
			
			if data:
				print('已存在。')
			else:
				content = pymysql.escape_string(item['content'])
				
				sql="insert into weixin_spider (wxId,content,nickname,url,title) values('%s','%s','%s','%s','%s')" % (item['wxId'],content,item['nickname'],item['url'],item['title'])
				cue.execute(sql)
				print("insert success")#测试语句
		except Exception as e:
			print('Insert error:',e)
			con.rollback()
		else:
			con.commit()
		con.close()
		return item
		
		
		