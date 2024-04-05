#!/bin/sh

# раскраска текста
WHITE="\033[37m"
VIOLET="\033[35m"
BLUE="\033[36m"
DBLUE="\033[34m"
YELLOW="\033[1;33m"
NORMAL="\033[0m"

# данные для запроса на сайт
search="clusters=true&enable_snippets=true&st=searchVacancy"
time="&order_by=publication_time"  # сортировать по дате
pages="&per_page=100"  # число страниц в ответе
area="&area=113"  # регион для поиска

# проверка параметра на валидность
if [ "$#" -ne 2 ]
	then echo -e "${WHITE}ожидался 2 параметра, а передано $#${NORMAL}"
	exit 1
fi

vacancy=$(echo "&text=$1" | tr -s " " | sed "s/ /%20/g") # название вакансии
#salary="&only_with_salary=true&salary=$2"
period="&period=$2"  # искать за этот период, в днях

# создание запроса к сайту hh.tu
request=$(curl -s --max-time 10 "https://api.hh.ru/vacancies?${search}${time}${vacancy}${pages}${period}${area}")

# если данные вернулись проходим по ним циклами и парсим неодходимые данные
if [ ${#request} -gt 0 ]
  then
  for page in {0..100}
	do
	  
	  # название вакансии, а конце вывод количества вакансий
		name=$(printf "%s" "${request}" | jq -r ".items.[${page}].name")
		found=$(printf "%s" "${request}" | jq -r ".found")
		if [ "${name}" = "null" ] || [ "${page}" -eq 100 ]
			then echo -e "${WHITE}${name}${NORMAL}" | sed "s/null/--- найдено ${found} вакансий ---/g"
			break
		fi	
		echo -e "${WHITE}${name}${NORMAL}"
		
		# название компании
		company=$(printf "%s" "${request}" | jq -r ".items.[${page}].employer.name")
		echo -e "фирма: ${VIOLET}${company}${NORMAL}"
		
		# время публикации вакансии
		date=$(printf "%s" "${request}" | jq -r ".items.[${page}].published_at" | sed "s/+.*//g" | tr "T" " ")
		echo -e "дата: ${DBLUE}${date}${NORMAL}"
		
		# размер зарплаты от и до
		from=$(printf "%s" "${request}" | jq -r ".items.[${page}].salary.from")
		to=$(printf "%s" "${request}" | jq -r ".items.[${page}].salary.to")
		echo -e "зарплата: ${BLUE}${from}${NORMAL} - ${BLUE}${to}${NORMAL}"
		
		# график работы
		schedule=$(printf "%s" "${request}" | jq -r ".items.[${page}].schedule.name" 2>/dev/null)
		echo -e "график работы: ${DBLUE}${schedule}${NORMAL}"
		
		# прямая ссылка на вакансию
		alternate_url=$(printf "%s" "${request}" | jq -r ".items.[${page}].alternate_url")
		echo -e "ссылка: ${YELLOW}${alternate_url}${NORMAL}"
		echo
		
	done
fi
