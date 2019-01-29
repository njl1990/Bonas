from pyDes import *
from time import time
from binascii import unhexlify as unhex
import os,random


def count_head(data):
	result = bytes(10)
	resulet_bytes_array =bytearray(result)
	data_bytes_array =bytes(str(data),'utf-8')
	resulet_bytes_array[0:len(data_bytes_array)]=data_bytes_array
	return bytes(resulet_bytes_array)

def decrypt_file(file_path,key_16):
	t = des(unhex(key_16))
	size = 1024*32

	if os.path.exists(file_path):
		obj_file = open(file_path[0:-4],'wb')#make partfile
		src_file = open(file_path,'rb')
		#read head
		head = src_file.read(10)
		mod_str= head.decode('utf-8').strip('\0')
		filesize=os.path.getsize(file_path)-int(mod_str)
		
		sizecount = 0
		while True:
			chunkbuffer = src_file.read(size)
			sizecount=sizecount+size

			if len(chunkbuffer)==size:
				#encrpt
				data=t.decrypt(chunkbuffer)
				percent = (sizecount*100)/(filesize)
				print('Process:'+str(percent)+'%');
				#write
				obj_file.write(data)         #write data into partfile
			else:
				print('last size = '+str(len(chunkbuffer)))
				obj_file.write(chunkbuffer)         #write data into partfile
			if not chunkbuffer:             #check the chunk is empty
				break
		obj_file.close()

def encrypt_file(file_path,key_16):

	t = des(unhex(key_16))
	size = 1024*32

	#check whether todir exists or not
	if os.path.exists(file_path):


		obj_file = open(file_path+'.des','wb')#make partfile
		#open the fromfile
		src_file = open(file_path,'rb')
		filesize=os.path.getsize(file_path)
		mod = int(filesize%size)	#get mod
		num = int(filesize/size)

		obj_file.write(count_head(mod)) 		# write mod in 10 bytes

		count =0
		while True:
			count = count+1
			chunkbuffer = src_file.read(size)
			if len(chunkbuffer)==size:
				#encrpt
				des3_t=t.encrypt(chunkbuffer)
				percent = (count*100)/(num)
				print('Process:'+str(percent)+'%');
				#write
				obj_file.write(des3_t)         #write data into partfile
			else:
				print('last size = '+str(len(chunkbuffer)))
				obj_file.write(chunkbuffer)         #write data into partfile
			if not chunkbuffer:             #check the chunk is empty
				break
		obj_file.close()
	else:
		print("file not exists!")


def create_keyfile():
	ran = hex(random.randint(0,0XFFFFFFFF))

	return ran

if __name__ == '__main__':
	#_example_des_()

	#encrypt_file("test.pdf","77661100DD223311")
	#decrypt_file("test.pdf.des","77661100DD223311")
	print(create_keyfile())
	#_filetest_()
	#_profile_()
