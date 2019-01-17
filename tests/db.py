import pymongo
def get_db():
	DB_NAME = 'user_details'
	DB_HOST = 'ds159164.mlab.com'
	DB_PORT = 59164
	DB_USER = 'ManishSinghFartyal'
	DB_PASS = 'Mf@#$2211'
	connection = pymongo.MongoClient(DB_HOST, DB_PORT)
	db = connection['user_details']
	db.authenticate(DB_USER, DB_PASS)
	kyc=db['kyc']
	return kyc
