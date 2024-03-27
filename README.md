# forms


## install
``` sh
git clone https://github.com/jackisace/forms.git
cd forms
sh install.sh
```

## initial enumeration
``` console
$ forms http://127.0.0.1:8000/ 
FORM: 0:
=========
action: login.php
username: None
password: None
Login: Login
user_token: b00d9be2028e114a94a08c6227cf9d58

$ | 
```

## quick test
``` sh
forms http://127.0.0.1:8000/ -a "username=admin,password=password"
forms http://127.0.0.1:8000/ -a "username=admin,password=admin"
```

## typical password bruteforce usage
``` console
$ forms http://127.0.0.1:8000/ -a "username=admin,password=/usr/share/wordlists/rockyou.txt"
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': '123456'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': '12345'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': '123456789'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'password'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'iloveyou'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'princess'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': '1234567'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': '12345678'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'abc123'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'nicole'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'daniel'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'babygirl'}
status: 501 	 length: 497 	 fields: {'username': 'admin', 'password': 'monkey'}
...
```

## usage
``` console
$ forms --help
usage: forms [-h] [-f FORM] [-a AUTO] [-t THREADS] [-p PROXY] [-v] [-vv] target

finds all forms, displays them, and automates posting

positional arguments:
  target                target page to parse eg: 'http://10.10.10.10/index.html'

options:
  -h, --help            show this help message and exit
  -f FORM, --form FORM  specify the form number if there are multiple forms on a page
  -a AUTO, --auto AUTO  specify all variables via the command line, eg:
                        'username=admin,password=P@$$w0rd' or 'user=admin,password=./list'. Filenames
                        without a '/' character in will be read as a single word and not opened as a
                        file
  -t THREADS, --threads THREADS
                        specify the number of threads (default: 10)
  -p PROXY, --proxy PROXY
                        set a proxy eg. -p http://127.0.0.1:8080
  -v, --verbose         print all form values
  -vv, --vverbose       print each result data and it's header

Good luck!
```
