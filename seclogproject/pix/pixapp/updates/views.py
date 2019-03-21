import os
import string
import time
import socket

from django.shortcuts import render
from django.views.generic import TemplateView
from itertools import islice
from django.http import HttpResponseRedirect

homedir = os.environ['HOME']
template_path = homedir + '/mon/pix/pixapp/templates/'
py_path = homedir + '/mon/pix/pixapp/'
tmpfile_path = template_path + 'tmp.txt'
key_path = homedir + '/.ssh/' + 'aravind'#private key name

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
				os.system(r'%snovafeed.py'%py_path)
				return render(request,'nova1.html',{"nlist":nlist,"flag":flag})
			else :
				h = open(template_path + 'hash_nova.txt','r+')
				hash_nova = h.read()
				if 'verified' in hash_nova or not hash_nova:
					f = open(template_path + 'output_nova.txt', "r+")
					contents = f.readlines()
					if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
						for ii in range(len(contents)-1):
							nlist.append(contents[ii])
						f.truncate(0)
						h.truncate(0)
						h.close()
						f.close()
						flag=True
						return render(request,'nova1.html',{"nlist":nlist,"flag":flag})
					else :
						f.close()
						return render(request,'nova1.html',{"nlist":nlist,"flag":flag})
				else:
					h.truncate(0)
					h.close()
					return render(request,'fail.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')					
	
class pixpage3(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):
			nlist=[]
			flag=False
			if  os.stat(template_path + 'output_cinder.txt').st_size == 0 :
				os.system(r'%scinderfeed.py'%py_path)
				return render(request,'cinder1.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + 'output_cinder.txt' , "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'cinder1.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'cinder1.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')

class pixpage4(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):
		
			nlist=[]
			flag=False
			if  os.stat(template_path + 'output_neutron.txt').st_size == 0 :
				os.system(r'%sneutronfeed.py'%py_path)
				return render(request,'neutron1.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + 'output_neutron.txt', "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'neutron1.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'neutron1.html',{"nlist":nlist,"flag":flag})	
		else :
			return HttpResponseRedirect('logout.html')


class pixpage5(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		
			nlist=[]
			flag=False
			if  os.stat(template_path + "output_glance.txt").st_size == 0 :
				os.system(r'%sglancefeed.py'%py_path)
				return render(request,'glance1.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "output_glance.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'glance1.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'glance1.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')
	

class pixpage6(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		

			nlist=[]
			flag=False
			if  os.stat(template_path + 'output_keystone.txt').st_size == 0 :
				os.system(r'%skeystonefeed.py'%py_path)
				return render(request,'keystone1.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + 'output_keystone.txt', "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'keystone1.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'keystone1.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')

class pixpage7(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		

			nlist=[]
			flag=False
			if  os.stat(template_path + "conf_output_nova.txt").st_size == 0 :
				os.system(r'%sconf_novafeed.py'%py_path)
				return render(request,'nova2.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "conf_output_nova.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'nova2.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'nova2.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')
	

class pixpage8(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		

			nlist=[]
			flag=False
			if  os.stat(template_path + "conf_output_cinder.txt").st_size == 0 :
				os.system(r'%sconf_cinderfeed.py'%py_path)
				return render(request,'cinder2.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "conf_output_cinder.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'cinder2.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'cinder2.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')	

class pixpage9(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		
		
			nlist=[]
			flag=False
			if  os.stat(template_path + "conf_output_neutron.txt").st_size == 0 :
				os.system(r'%sconf_neutronfeed.py'%py_path)
				return render(request,'neutron2.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "conf_output_neutron.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'neutron2.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'neutron2.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')	

class pixpage10(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		

			nlist=[]
			flag=False
			if  os.stat(template_path + "conf_output_glance.txt").st_size == 0 :
				os.system(r'%sconf_glancefeed.py'%py_path)
				return render(request,'glance2.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "conf_output_glance.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'glance2.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'glance2.html',{"nlist":nlist,"flag":flag})
		else :
			return HttpResponseRedirect('logout.html')		

class pixpage11(TemplateView):
	def get(self, request):
		if request.user.is_authenticated and request.session.get('ip'):		
		
			nlist=[]
			flag=False
			if  os.stat(template_path + "conf_output_keystone.txt").st_size == 0 :
				os.system(r'%sconf_keystonefeed.py'%py_path)
				return render(request,'keystone2.html',{"nlist":nlist,"flag":flag})
					
					
			else :
				f = open(template_path + "conf_output_keystone.txt", "r+")
				contents = f.readlines()
				if contents[len(contents)-1] == "end\n" or contents[len(contents)-1] == "end":
					for ii in range(len(contents)-1):
						nlist.append(contents[ii])
					f.truncate(0)
					f.close()
					flag=True
					return render(request,'keystone2.html',{"nlist":nlist,"flag":flag})
				else :
					f.close()
					return render(request,'keystone2.html',{"nlist":nlist,"flag":flag})	
		else :
			return HttpResponseRedirect('logout.html')

class pixpage12(TemplateView):

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
class pixpage13(TemplateView):
	def __init__(self):
		f1 = open(template_path + "conf_output_keystone.txt", "r+")
		if os.stat(template_path + "conf_output_keystone.txt").st_size != 0 :
			f1.truncate(0)
			f1.close() 
		else:
			f1.close()
		f2 = open(template_path + "conf_output_nova.txt", "r+")
		if os.stat(template_path + "conf_output_nova.txt").st_size != 0 :
			f2.truncate(0)
			f2.close() 
		else:
			f2.close()
		f3 = open(template_path + "conf_output_cinder.txt", "r+")
		if os.stat(template_path + "conf_output_cinder.txt").st_size != 0 :
			f3.truncate(0)
			f3.close() 
		else:
			f3.close()
		f4 = open(template_path + "conf_output_glance.txt", "r+")
		if os.stat(template_path + "conf_output_glance.txt").st_size != 0 :
			f4.truncate(0)
			f4.close() 
		else:
			f4.close()
		f5 = open(template_path + "conf_output_neutron.txt", "r+")
		if os.stat(template_path + "conf_output_neutron.txt").st_size != 0 :
			f5.truncate(0)
			f5.close() 
		else:
			f5.close()
	template_name="metadata.html"

class pixpage14(TemplateView):
	template_name="snapshot.html"

#change APIView to template view
class ip(TemplateView):
	def get(self,request):
		if request.user.is_authenticated:
			return render(request,'ip.html')
		else :
			return HttpResponseRedirect('logout.html')			

class submitIP(TemplateView):
    def post(self,request):
        if not(request.user.is_authenticated ):
            return HttpResponseRedirect('logout.html')

        ip = request.POST['ip']
        host = request.POST['host']
        passw = request.POST['passw']
        self.msg="error"
	
        hostName = ip
        uname = host
        spass = passw
        print(hostName)
        with open(tmpfile_path, 'w+') as tmp:
            tmp.write(ip + '\n')
            tmp.write(host + '\n')
            tmp.write(passw + '\n')
            tmp.close()

        self.status = False
        try:
            socket.inet_aton(ip)
        except :
            self.msg="Invalid IP"
            return render(request,"ip.html",{"status":self.status,"msg":self.msg})

        def myfunc():        
            
            import paramiko
            import string
            import os
            import time
            import sys

            ## flags ##
            err_flag = 0
            authfail_flag = 0
            invusr_flag = 0
            unrhost_flag = 0
            timeout_flag = 0
            fh=[]

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()


            privatekeyfile = os.path.expanduser(key_path)
            key = paramiko.RSAKey.from_private_key_file(privatekeyfile)
            
            try:
                ssh.connect(hostname='%s' %hostName, username='%s' %uname, pkey=key, timeout=10)
                

            except paramiko.AuthenticationException:
                self.msg='invalid user name'
                invusr_flag = 1
                return

            except paramiko.ssh_exception.NoValidConnectionsError:
                self.msg='host unreachable'
                unrhost_flag = 1
                return

            except paramiko.ssh_exception.socket.timeout:
                self.msg='connection timedout'
                timeout_flag = 1
                return

            stdin,stdout,stderr=ssh.exec_command('sudo ls', get_pty= True)
            time.sleep(2)
            stdin.write(spass + '\n')
            stdin.flush()
            time.sleep(5)

            rb = stdout.channel.recv(90)										#capture 100 bytes from socket
            rbd = rb.decode('ascii')											#convert byte to string
            

            if 'Sorry,' in rbd or 'sudoers file' in rbd:
                authfail_flag = 1
                self.msg="Wrong Sudo Password"
                return #sys.exit('auth error')
            
                
            err = stderr.readline()

            if not err_flag:
                err_flag = 0
            else:
                err_flag = 1

            while True:
                temp=stdout.readline()
                if temp=='':
                    break
                fh.append(''.join(temp))
            

            if (err_flag+authfail_flag+invusr_flag+unrhost_flag+timeout_flag)==0:
                self.status=True
            else:
                self.status=False
            self.msg="some error"
        
        myfunc()    


        
        if self.status is True:
            request.session['ip'] = ip
            request.session['host'] = host
            request.session['passw'] = passw
            return HttpResponseRedirect('home.html')
        else:
            return render(request,"ip.html",{"status":self.status,"msg":self.msg})

			
