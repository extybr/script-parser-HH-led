# Парсер вакансий с Headhunter <img src="https://i.hh.ru/logos/svg/hh.ru__min_.svg" height="32"/> с включением светодиода

## подключил к 25 пину на RaspberryPi, выставил пограммную задержку светодиоду
## можно подключить аудио
## запускать через cron
## crontab -e
  */5 * * * * /usr/bin/python3 /home/pi/Desktop/script-job-led.py