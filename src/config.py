import os



# variaveis de banco de dados
db_host     = os.getenv('MYSQL_HOST')
db_user     = os.getenv('MYSQL_USER')
db_password = os.getenv('MYSQL_PASSWORD')
db_port     = 25060
db_database = 'FIAP-FOOD'


mongo_user = os.getenv('MONGO_USER')
mongo_senha = os.getenv('MONGO_SENHA')
mongo_db = os.getenv('MONGO_DB')
mongo_collection = 'faturas'