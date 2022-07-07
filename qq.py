import struct
import sys
import argon2
from django.contrib.auth.hashers import make_password
from graphviz import Digraph
from cryptography.fernet import Fernet
# g = Digraph('G', filename='hello.gv')
#
# g.edge('Hello', 'World')
#
# g.view()
pas=123
argon2.argon2_hash("password", "some_salt", )
print(a)
key = Fernet.generate_key()
f = Fernet(key)
pa = '123w'
pa = str.encode(pa)
token = f.encrypt(pa)
num=212
#token = str(token)#only for append mode not wb
#ex = f.extract_timestamp(token)
# with open('PassMngSite/binsp1.bin', 'ab') as mybin:
#      mybin.write(str(num).encode())
#      mybin.write(b'\n')
#      mybin.write(key)
#      mybin.write(b'\n')
#      mybin.write(token)
#      mybin.write(b'\n')
   #   for line in mybin:
   #       en=line
   #       en = line.decode("utf-8")
          ##key=mybin.readlines()[0]
          ##key =Fernet(key)#yek instance
with open('PassMngSite/binsp1.bin', 'rb') as mybin:
          lineid=1
          linekey=0
          linetok=0
          #tok = mybin.readlines()[8]
          #tok=tok.decode()
          #en = mybin.read(1)
          #mybin.readline()
          #en1=mybin.readlines()[2]
          #en2=en1[2]
          # en2=mybin.readlines()
          # en1=en2[1]
          # en2=en2[8]
          # print("en1",en1,"en2",en2)
          #del en1
          en1=mybin.readline()
          #=mybin.readlines()
          for line in mybin:
              lineid+=1
              linekey = lineid+2
              linetok = lineid+3
              en1 = line.strip()
              #print("strip",en1)
              ###if en1== str(num).encode():
              if en1 == str(num).encode():#uid=11
                  print("lineid",lineid)
                  #print(en1)
                  # print(linekey)
                  # print(linetok)
#print (en)
# print(ex)
# dtoken = (f.decrypt(token))
# #print(key)
# #print(f)
# print(token)
# print(dtoken.decode("utf-8"))#