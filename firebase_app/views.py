import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class OCR(TemplateView):
	template_name = 'index.html'
	cred = credentials.Certificate("privateKey.json")
	firebase_admin.initialize_app(cred)
	db = firestore.client()

	def get(self,request):
		docs = self.db.collection('test').get()
		ocr_array = []

		for doc in docs:
			print(len(doc.to_dict()))
			dic = {}
			for i in range(int(len(doc.to_dict()) / 2)):
				dic['value'+ str(i + 1)] = doc.to_dict()['value' + str(i + 1)]
				dic['category'+ str(i + 1)] = doc.to_dict()['category' + str(i + 1)]
			ocr_array.append(dic)
		return render(request, 'index.html',{'ocr_array':ocr_array})

def show(request,id=None):
	db = firestore.client()
	dic = db.collection('test').get()[int(id)].to_dict()
	
	return render(request, 'show.html',{'dic':dic})
