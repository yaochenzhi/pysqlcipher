# test
# and test the possibilities as it says

# dd if=/dev/zero of=testdb bs=1M count=1

import sqlite3


DATABASES = ["mydb", "testdb"]
for db in DATABASES:
    try:
        with sqlite3.connect(db) as cursor:
            cursor.execute("SELECT * FROM users")
            print(cursor.fetchall())
    except Exception as e:
        print(e)
