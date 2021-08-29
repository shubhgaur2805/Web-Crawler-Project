import sqlite3
import csv
class Api_database:
    def __init__(self, get_metadata):
        self.get_metadata = get_metadata
    def database(self):
        conn = sqlite3.connect("api_database.db")
        my_cursor = conn.cursor()
        try:
            my_cursor.execute("CREATE TABLE Api_metadata(S_No INTEGER PRIMARY KEY AUTOINCREMENT, API_Name text,Description text,Auth text,HTTPS text,Cors text,Link text,Category_ID int)")
            conn.commit()
            my_cursor.execute("CREATE TABLE Api_category(ID INTEGER PRIMARY KEY AUTOINCREMENT,Category text)")
            conn.commit()
            conn.close()
        except:
            my_cursor.execute("DROP TABLE Api_metadata")
            conn.commit()
            my_cursor.execute("DROP TABLE Api_category")
            conn.commit()
            my_cursor.execute(
                "CREATE TABLE Api_metadata(SNo INTEGER PRIMARY KEY AUTOINCREMENT, API_Name text,Description text,Auth text,HTTPS text,Cors text,Link text,Category_ID int)")
            conn.commit()
            my_cursor.execute("CREATE TABLE Api_category(ID INTEGER PRIMARY KEY AUTOINCREMENT,Category text)")
            conn.commit()
            conn.close()
            print("Table is Created")

        conn = sqlite3.connect("api_database.db")
        my_cursor = conn.cursor()
        for key, value in self.get_metadata.items():
            my_cursor.execute("INSERT INTO Api_category(Category) VALUES(:name)", {"name": str(key)})
            conn.commit()

        conn = sqlite3.connect("api_database.db")
        my_cursor = conn.cursor()
        no = 0
        for key, value in self.get_metadata.items():
            no += 1
            for i in value:
                if i["Auth"] == "":
                    i["Auth"] = 'No'
                my_cursor.execute("""INSERT INTO Api_metadata(API_Name,Description,Auth,HTTPS,Cors,Link,Category_ID) VALUES(:api,:desc,:auth,:https,:cors,:link,:cat)""",
                                  {"api": i["API"], "desc": i['Description'], "auth": i['Auth'],
                                   "https": str(i['HTTPS']),
                                   "cors": i['Cors'], "link": i["Link"], "cat": int(no)})
                conn.commit()
        conn.close()

    def excel(self):
        field_name=["API","Description","Auth","HTTPS","Cors","Link","Category"]
        with open("Data.csv","w",newline='') as f:
            csvwriter=csv.writer(f)
            csvwriter.writerow(field_name)
            for key,value in self.get_metadata.items():
                for i in value:
                    x=i["API"],i['Description'],i['Auth'],str(i['HTTPS']),i['Cors'],i["Link"],i["Category"]
                    csvwriter.writerow(x)
