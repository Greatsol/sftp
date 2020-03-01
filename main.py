import paramiko
import os

host = '' # ip фдрес сервера
user = 'root'
secret = '' # пароль пользователя
port = 22 # порт для sftp
folder = ''  # путь переносимой директории


transport = paramiko.Transport((host, port))
transport.connect(username=user, password=secret)
sftp = paramiko.SFTPClient.from_transport(transport)

os.chdir(folder)

for file in os.listdir():
	if file.split('.')[-1] == 'py':
		localpath = f'{folder}/{file}'
		remotepath = f'/root/{file}'
		sftp.put(localpath, remotepath)

sftp.close()
transport.close()
