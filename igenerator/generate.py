import os
import random as ra
from jax.random import PRNGKey
import jax.random as random
import sqlite3
import csv

class LiveGenerator():
    def __init__(self,key=ra.randint(1, 100000)) -> None:
        self.seed = PRNGKey(key)
        
    def randomInt(self, min, max, len) -> list:
        rand = random.randint(self.seed, shape=(len,),minval=min, maxval=max)
        return rand.tolist()
    
    def randomFloat(self, min, max, len) -> list:
        rand = random.uniform(self.seed, shape=(len,),minval=min, maxval=max)
        rand = rand.tolist()
        rand = [round(num,2) for num in rand]
        return rand
    
    def writeSql(self, randomValues, path, table) -> None:
        if not os.path.exists(path):
            raise Exception(f"Database Not Found at {path}")
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        placeholders = ', '.join('?' * len(randomValues))
        query = f"INSERT INTO {table} VALUES ({placeholders})"
        cursor.execute(query, randomValues)
        conn.commit()
        conn.close()
        print(f"Written to the Table : {table}")
        
    def writeCsv(self, randomValues, path) -> None:
        if not os.path.exists(path):
            raise Exception(f"CSV File Not Found at {path}")
        with open(path,'a') as csvfile:
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(randomValues) 
        csvfile.close()
        print(f"Written to the CSV File : {path}")

# obj = TrueGenerator(key=3)
# randomValue = obj.randomFloat(3,15,4)

# db_path = "database.db"
# table_name = "true"
# obj.writeSql(randomValue,db_path,table_name )
# csv_path = 'data.csv'
# obj.writeCsv(randomValue,csv_path)
# print(randomValue)