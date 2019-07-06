#   sys.path is only searched for Python modules. For dynamic linked libraries, 
# the paths searched must be in LD_LIBRARY_PATH. Check if your LD_LIBRARY_PATH
# includes /usr/local/lib, and if it doesn't, add it and try again.

# export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

from pysqlcipher3 import dbapi2 as sqlite3


class Database(object):
    def __init__(self, dbname):
        self.dbname = dbname

    def connDB(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA key='mypassword'")

    def createDB(self):
        self.connDB()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            login TEXT NOT NULL,
            passwd TEXT);
            '''
        )

        self.cursor.execute(
            '''
            INSERT INTO users (name, login, passwd)
            VALUES ("Admininstrator", "admin", "12345")
            '''
        )
        self.conn.commit()
        self.conn.close()

    def queryDB(self, sql):
        self.connDB()
        self.cursor.execute(sql)

        if sql[0:6].lower() == 'select':
            result = self.cursor.fetchall()
            self.conn.close()
            return result
        else:
            self.conn.commit()
            self.conn.close()


if __name__ == "__main__":
    db = Database("mydb")
    db.createDB()
    result = db.queryDB("SELECT * FROM users")
    print(result)
