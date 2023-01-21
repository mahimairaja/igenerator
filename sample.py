from igenerator.generate import LiveGenerator

obj = LiveGenerator()
result = obj.randomInt(2,15,4)
obj.writeCsv(result,'data.csv')
table_name = "true"
obj.writeSql(result,'database.db',table_name)