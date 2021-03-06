import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_authentication.mixins import FirebaseAuthMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.auth.models import User
from django.views import generic
from .forms import LoginForm

from django.conf import settings
import pprint


class OCR(TemplateView):
	template_name = 'index.html'


	def get(self,request):
		app = firebase_admin.get_app()
		db = firestore.client()

		user = auth.get_user_by_email('dmjdesu@gmail.com')

		print('Successfully fetched user data: {0}'.format(user.uid))

		docs = db.collection('test').where('value1', '==', user.uid).get()
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

class Top(TemplateView):
    template_name = 'register/top.html'

