import mariadb, datetime
from db01_config import db_config

try:
    
    # 
    # create connection
    #
    con = mariadb.connect(**db_config)

    print("MariaDB connection successfully established:")
    print(con)

    # 
    # select data
    #
    query = "select * from standort"

    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    print(query,":")
    print(result)


    # 
    # select data with params
    #
    query = "select titel, beginn, ende from lehrveranstaltung where beginn between %s and %s and titel like 'ENG%'"
    start = datetime.datetime(2021, 1, 1, 0, 0, 0)
    end   = datetime.datetime(2021, 12, 31, 23, 59, 59)
    
    cursor = con.cursor()
    cursor.execute(query, (start, end))

    print(query,":")
    for (titel, beginn, ende) in cursor:
        print("- ", titel, ":", beginn, "-", end)



except mariadb.Error as e:
    print("MariaDB connection failure: {}".format(e))

finally:
  cursor.close()
  con.close()
