import os, time
os.system("clear")
print("""
       Свет!  '✨️ 
        '✨️'✨️ ' 
  Камера! '   '   
      🎥️       Мотор! 🎞️
      
Ожидаем птичку...
=Используйте другую сессию, чтобы запустить сервер. \033[43m04\033[0m - команда для запуска.
=Все фотографии будут в папке \033[42mcam\033[0m""")
print("\033[32mНаблюдаю за логами...\033[0m")
while True:
	try:
		f = open('./logs/result.txt','r')
		value_f = f.read()
		if(value_f != ""):
			print(value_f)
			f = open('./logs/result.txt','w')
			f.write("")
		f.close()
	except:
		pass	
	
