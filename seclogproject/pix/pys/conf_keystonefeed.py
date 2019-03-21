#!/usr/bin/env python
import conf_keystone as d
import nltk
import string
import pickle
import os
import time
import sys
import paramiko

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

homedir = os.environ['HOME']
template_path = homedir + '/mon/pix/pixapp/templates/'
key_path = homedir + '/.ssh/aravind'								#enter private key name
tmpfile_path = template_path + 'tmp.txt'
opfile_path = template_path + 'conf_output_keystone.txt'

with open (opfile_path, 'w+') as gen:
	gen.write('start\n')

fh = []
cred = []

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

with open(tmpfile_path,'r') as fil:
    for line in fil:
        cred1 = line.split()
        cred.extend(cred1)
    fil.close()

host = str(cred[0])
uname = str(cred[1])
spass = str(cred[2])       
        
privatekeyfile = os.path.expanduser(key_path)
key = paramiko.RSAKey.from_private_key_file(privatekeyfile)

ssh.connect(hostname='%s' %host, username='%s' %uname, pkey=key, timeout=10)

#stdin,stdout,stderr=ssh.exec_command('sudo cat /etc/keystone/keystone.conf', get_pty= True)		#path to file keystone.conf	
stdin,stdout,stderr=ssh.exec_command('sudo cat ~/testkey.conf', get_pty= True)
time.sleep(2)
stdin.write(spass + '\n')
stdin.flush()
time.sleep(5)

rb = stdout.channel.recv(100)										#capture 100 bytes from socket
rbd = rb.decode('ascii')										#convert byte to string

while True:
    temp=stdout.readline()
    if temp=='':
        break
    fh.append(''.join(temp))

#ssh.connect(hostname='%s' %host, username='%s' %uname, pkey=key, timeout=10)
#stdin,stdout,stderr=ssh.exec_command('sudo cat /etc/keystone/logging.conf', get_pty= True)		#path to file logging.conf
#time.sleep(2)
#stdin.write(spass + '\n')
#stdin.flush()
#time.sleep(5)

#rb = stdout.channel.recv(100)										#capture 100 bytes from socket
#rbd = rb.decode('ascii')										#convert byte to string

#while True:
#    temp=stdout.readline()
#    if temp=='':
#        break
#    fh.append(''.join(temp))


tokens1 = []
tokens = []
tokensv = []
tokensn = []
temp = []
final= []
result=[]
string.cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.spl='~!@#$%^&*()_+-=\|]}[{:;<>,./?'
string.num='0123456789'

for line in fh:
    tokenst = line.split()
    tokens1.extend(tokenst)
tokens = list(FreqDist(tokens1))

for word in tokens:
    if word not in d.tokens:
        tokensv.append(word)
    else:
        continue

for words in tokensv:
    tokensn.append(d.generate_ngrams(words,3,1))

i=0
dout = []
for word in tokensn:
    dout = d.detect_mod(word)
    if dout[0] == 'pos':
        temp.append(tokensv[i])
        i=i+1
    else:
        i=i+1
        continue

for i in range(len(temp)):
    for j in range(len(temp[i])):
        if (temp[i][j:j+9]=='password=') or (temp[i][j:j+9]=='PASSWORD='):
            result.append(temp[i][j+9:])
            i=i+1
        else:
            continue
    result.append(temp[i])

with open (opfile_path, 'w+') as gen:
	if not result:
		gen.write('No credentials detected')
	else:
		gen.write('\n'.join(str(word) for word in result))
	gen.write('\nend')

#with open(tmpfile_path,'w') as fil:
#    fil.truncate(0)
#    fil.close()


