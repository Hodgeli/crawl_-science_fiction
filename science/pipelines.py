# -*- coding: utf-8 -*-

import MySQLdb


class SciencePipeline(object):
    def process_item(self, item, spider):
        DBKWAGS = spider.settings.get('DBKWAGS')
        con = MySQLdb.connect(**DBKWAGS)
        cur = con.cursor()
        sql = ("insert into xici (IP, PORT,TYPE,POSITION ,SPEED,LAST_CHECK_TIME) "
               "value (%s,%s,%s,%s,%s,%s)")
        lis = (item['IP'], item['PORT'], item['TYPE'], item['POSITION'], item['SPEED'], item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql, lis)
        except:
            print("Insert error")
        else:
            con.commit()
        cur.close()
        con.close()
        return item
