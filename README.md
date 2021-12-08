# PyFuzzer

## About Pyfuzzer
it was just a project idea, i did it and here it is

## small Documentation

~~~
$ python Pyfuzzer.py -h
usage: Pyfuzzer.py [-h] [-u Target URL] [-c CMS] [-w WordList] [-f Filter] [-v [Values [Values ...]]]

PyFuzzer, Discover hidden files and directories on a web server. The application tries to find url
relative paths of the given website by comparing them with a given set...

optional arguments:
  -h, --help            show this help message and exit
  -u Target URL, --url Target URL
                        Here goes the URL of the objective
  -c CMS                scan CMS that are by default
  -w WordList           Custom wordlist
  -f Filter, --filter Filter
                        Filter the output, hc: Hide code; sc: Show code only
  -v [Values [Values ...]], --values [Values [Values ...]]
                        Values for the --filter parameter
                        
~~~

Example of its use:

* Fuzzing an url with default dictionary(dicc.txt)
~~~
$ python Pyfuzzer.py -u https://127.0.0.1
~~~

* Fuzzing CMS (php: in this example)
~~~
$ python Pyfuzzer.py -u https://127.0.0.1 -c php
~~~

* Fuzzing with a custom Wordlist
~~~
$ python Pyfuzzer.py -u https://127.0.0.1 -w /usr/share/seclists/Discovery/Web-Content/big.txt
~~~

* Fuzzing using filters for the output:
~~~
$ python Pyfuzzer.py -u https://127.0.0.1 -c wp --filter=hc -v 404 403
~~~

## How to Install
#### Clone
 Clone this repository:
 ```
$ git clone https://github.com/justgr0w/Pyfuzzer.git
$ cd Pyfuzzer
$ python angryFuzzer.py
```

## Dependencies
 in Linux enviroments, you need ,to have figlet installed.
 Install the following dependencies with python-pip
 ```bash
$ sudo pip install -r requirements.txt
```
