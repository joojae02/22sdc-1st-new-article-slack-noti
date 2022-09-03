import db_info
import pymysql
import json

class DB :
    def __init__(self) :
        self.blog_db =  pymysql.connect(
            user= db_info.db_username, 
            port = db_info.db_port,
            passwd = db_info.db_password, 
            host = db_info.db_host, 
            db = db_info.db_name, 
            charset='utf8'
        )


    def insert_db (self, title, content, site, url) :
        sql = """
        INSERT IGNORE INTO blog (blog_title, blog_content, blog_site, blog_url) 
        VALUES ("%s", "%s", "%s", "%s");
        """%(title, content, site, url)
        cursor = self.blog_db.cursor()

        cursor_return_value = cursor.execute(sql)
        self.blog_db.commit()
        return cursor_return_value
    
    def is_title_not_exist_in_db(self, title) :
        cursor = self.blog_db.cursor()

        sql = """
        select NOT EXISTS 
        (select * from blog where blog_title='%s' limit 1) 
        as success;
        """%(title)
        cursor.execute(sql)
        fetch_value = cursor.fetchone()
        return fetch_value[0]
    def select_db_title_content(self) :
        pass