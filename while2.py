# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入
# 最多輸入3次
# 如果正確，印出"登入成功!"
# 如果失敗，印出"密碼錯誤!還有__次機會!"

err = 3 # 錯誤剩餘次數  
while True:
	password = input('請輸入密碼：')
	if password == 'a123456':
		print('登入成功')
		break # 離開迴圈
	else:
		err = err - 1
		print('密碼錯誤!還有', err, '次機會!')
		if err == 0:
			break
