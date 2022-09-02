import db_info
import pymysql
import json

class DB :
    def __init__(self) :
        print("db success! " )
        self.blog_db =  pymysql.connect(
            user= db_info.db_username, 
            port = db_info.db_port,
            passwd = db_info.db_password, 
            host = db_info.db_host, 
            db = db_info.db_name, 
            charset='utf8'
        )
        self.cursor = self.blog_db.cursor()


    def insert_db (self, title, content, site, url) :
        sql = """
        INSERT IGNORE INTO blog VALUES ("%s", "%s", "%s", "%s");
        """%(title, content, site, url)
        self.cursor.execute(sql)
        self.blog_db.commit()


