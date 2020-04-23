err = 3
while True:
	password = input('請輸入密碼：')
	if password == 'a123456':
		break
	else:
		print('密碼錯誤!還有', err, '次機會!')
		err = err - 1
print('登入成功')