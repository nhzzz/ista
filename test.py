import requests as r
print('成功连接至zombieGitHub')
while True:
	menu = "输入数字进行选择\n1.原理详解\n2.远程端代码\n3.exit\n"
	choose = input(menu)
	if choose == '1':
		print('原理解释：如何做到两行代码实现大量功能')
		print('实现这个功能主要运用了requests库')
		print('从github获取代码再通过exec运行')
	elif choose == '2':
		print('请稍后，正在从GitHub获取源码')
		print(r.get('https://nhzzz.github.io/ista/test.py').text)
	else:
		print('链接断开')
		break
	
