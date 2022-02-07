## <h3>Парсер вакансий с Headhunter <img src="https://i.hh.ru/logos/svg/hh.ru__min_.svg" height="32"/> с включением светодиода<h3>

### <h4>подключил к 25 пину на RaspberryPi, выставил пограммную задержку светодиоду</h4>
### <h4>запускать через cron</h4>
## <h4># crontab -e</h4>
     */30 * * * * /usr/bin/python3 /home/pi/Desktop/script-job-led.py
### <h4>можно подключить аудио</h4>
	import os

	path_to_audio = "/home/pi/file.mp3"
	os.system(path_to_audio)	

	