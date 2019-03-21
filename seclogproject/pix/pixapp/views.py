import os
import string
import time
import socket

from django.shortcuts import render
from django.views.generic import TemplateView
from itertools import islice
from django.http import HttpResponseRedirect

template_path ='/seclogproject/pix/pixapp/templates/'
py_path = '/seclog/'
tmpfile_path = template_path + 'tmp.txt'

nova_list = [] 
cinder_list = []
neutron_list = []
glance_list = []
keystone_list = []
stri=[] 
plist=[]

class pixpage1(TemplateView):
    def get(self, request):
        if request.user.is_authenticated and request.session.get('ip'):
            return render(request,'home.html')
        else :
            return HttpResponseRedirect('logout.html')
                
class pixpage2(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):
			nlist=[]
			flag=False

			if  os.stat(template_path + 'output_nova.txt').st_size == 0 :
				os.system(r'%snovafeedcpy.py'%py_path)
				hf = open(template_path + 'nov_check.txt', "r+")
				hashstatus = hf.read()
				hf.close()

			else :
				f = open(template_path + 'output_nova.txt', "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'nova1.html',{"nlist":nlist,"flag":flag,"hflag":False})

				else :
					f.close()
					return render(request,'nova1.html',{"nlist":nlist,"flag":flag,"hflag":False})

			if 'failed' in hashstatus:
				f = open(template_path + 'output_nova.txt', "r+")
				f.truncate(0)
				f.close()
				return render(request,'nova1.html',{"nlist":nlist,"flag":flag,"hflag":True})

			else:
				return render(request,'nova1.html',{"nlist":nlist,"flag":flag,"hflag":False})

		else :
			return HttpResponseRedirect('logout.html')					
	
class pixpage3(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):
			nlist=[]
			flag=False

			if  os.stat(template_path + 'output_cinder.txt').st_size == 0 :
				os.system(r'%scinderfeedcpy.py'%py_path)
				hf = open(template_path + 'cin_check.txt', "r+")
				hashstatus = hf.read()
				hf.close()
					
					
			else :
				f = open(template_path + 'output_cinder.txt' , "r+")
				contents = f.readlines()

				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'cinder1.html',{"nlist":nlist,"flag":flag,"hflag":False})

				else :
					f.close()
					return render(request,'cinder1.html',{"nlist":nlist,"flag":flag,"hflag":False})

			if 'failed' in hashstatus:
				f = open(template_path + 'output_cinder.txt', "r+")
				f.truncate(0)
				f.close()
				return render(request,'cinder1.html',{"nlist":nlist,"flag":flag,"hflag":True})

			else:
				return render(request,'cinder1.html',{"nlist":nlist,"flag":flag,"hflag":False})

		else :
			return HttpResponseRedirect('logout.html')

class pixpage4(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):
		
			nlist=[]
			flag=False

			if  os.stat(template_path + 'output_neutron.txt').st_size == 0 :
				os.system(r'%sneutronfeedcpy.py'%py_path)
				hf = open(template_path + 'neu_check.txt', "r+")
				hashstatus = hf.read()
				hf.close()
					
					
			else :
				f = open(template_path + 'output_neutron.txt', "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'neutron1.html',{"nlist":nlist,"flag":flag,"hflag":False})

				else :
					f.close()
					return render(request,'neutron1.html',{"nlist":nlist,"flag":flag,"hflag":False})

			if 'failed' in hashstatus:
				f = open(template_path + 'output_neutron.txt', "r+")
				f.truncate(0)
				f.close()
				return render(request,'neutron1.html',{"nlist":nlist,"flag":flag,"hflag":True})

			else:
				return render(request,'neutron1.html',{"nlist":nlist,"flag":flag,"hflag":False})

		else :
			return HttpResponseRedirect('logout.html')


class pixpage5(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):

			nlist=[]
			flag = False

			if  os.stat(template_path + "output_glance.txt").st_size == 0 :
				os.system(r'%sglancefeedcpy.py'%py_path)
				hf = open(template_path + 'glan_check.txt', "r+")
				hashstatus = hf.read()
				hf.close()
					
					
			else :
				f = open(template_path + "output_glance.txt", "r+")
				contents = f.readlines()

				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'glance1.html',{"nlist":nlist,"flag":flag,"hflag":False})

				else :
					f.close()
					return render(request,'glance1.html',{"nlist":nlist,"flag":flag,"hflag":False})

			if 'failed' in hashstatus:
				f = open(template_path + 'output_glance.txt', "r+")
				f.truncate(0)
				f.close()
				return render(request,'glance1.html',{"nlist":nlist,"flag":flag,"hflag":True})

			else:
				return render(request,'glance1.html',{"nlist":nlist,"flag":flag,"hflag":False})

		else :
			return HttpResponseRedirect('logout.html')
	

class pixpage6(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		

			nlist = []
			flag = False
			
			if  os.stat(template_path + 'output_keystone.txt').st_size == 0 :
				os.system(r'%skeystonefeedcpy.py'%py_path)
				hf = open(template_path + 'key_check.txt', "r+")
				hashstatus = hf.read()
				hf.close()

			else :
				f = open(template_path + 'output_keystone.txt', "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag = True
					return render(request,'keystone1.html',{"nlist":nlist,"flag":flag,"hflag":False})

				else :
					f.close()
					return render(request,'keystone1.html',{"nlist":nlist,"flag":flag,"hflag":False})

			if 'failed' in hashstatus:
				f = open(template_path + 'output_keystone.txt', "r+")
				f.truncate(0)
				f.close()
				return render(request,'keystone1.html',{"nlist":nlist,"flag":flag,"hflag":True})

			else:
				return render(request,'keystone1.html',{"nlist":nlist,"flag":flag,"hflag":False})


		else :
			return HttpResponseRedirect('logout.html')

class pixpage7(TemplateView):

	def __init__(self):
		f1 = open(template_path + "output_keystone.txt", "r+")
		if os.stat(template_path + "output_keystone.txt").st_size != 0 :
			f1.truncate(0)
			f1.close() 
		else:
			f1.close()

		f2 = open(template_path + "output_nova.txt", "r+")
		if os.stat(template_path + "output_nova.txt").st_size != 0 :
			f2.truncate(0)
			f2.close() 
		else:
			f2.close()

		f3 = open(template_path + "output_cinder.txt", "r+")
		if os.stat(template_path + "output_cinder.txt").st_size != 0 :
			f3.truncate(0)
			f3.close() 
		else:
			f3.close()

		f4 = open(template_path + "output_glance.txt", "r+")
		if os.stat(template_path + "output_glance.txt").st_size != 0 :
			f4.truncate(0)
			f4.close() 
		else:
			f4.close()

		f5 = open(template_path + "output_neutron.txt", "r+")
		if os.stat(template_path + "output_neutron.txt").st_size != 0 :
			f5.truncate(0)
			f5.close() 
		else:
			f5.close()

	template_name = 'logs.html'


#change APIView to template view
class ip(TemplateView):
	def get(self,request):
		if request.user.is_authenticated:
			return render(request,'home.html')
		else :
			return HttpResponseRedirect('logout.html')			


			
