import mariadb
from db01_config import db_config

try:
    con = mariadb.connect(**db_config)

    print("MariaDB connection successfully established:")
    print(con)

except mariadb.Error as e:
    print("MariaDB connection failure: {}".format(e))

else:
  con.close()
