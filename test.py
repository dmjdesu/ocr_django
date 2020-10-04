import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def main():
	cred = credentials.Certificate("privateKey.json")
	firebase_admin.initialize_app(cred)
	db = firestore.client()
	docs = db.collection('test').get()

	ocr_array = []

	for doc in docs:
		print(len(doc.to_dict()))
		dic = {}
		for i in range(int(len(doc.to_dict()) / 2)):
			dic[doc.to_dict()['category' + str(i + 1)]] = doc.to_dict()['value' + str(i + 1)]
		ocr_array.append(dic)

	print(type(ocr_array))

main()