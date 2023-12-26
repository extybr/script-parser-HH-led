### Парсер вакансий <img src="https://i.hh.ru/logos/svg/hh.ru__min_.svg" height="32"/> с включением светодиода

#### В текущей директории создается текстовый файл с вакансиями
#### подключил к 25 пину на RaspberryPi, выставил пограммную задержку светодиоду
#### запускать через cron
    # crontab -e
```
*/30 * * * * /usr/bin/python3 /home/pi/Desktop/script-job-led.py
```
#### можно подключить аудио
    
	import os

	path_to_audio = "/home/pi/file.mp3"
	os.system(path_to_audio)
