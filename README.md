# PyFuzzer
<img src="https://github.com/justgr0w/PyFuzzer/blob/main/photos/logo.png" width="500">
## About Pyfuzzer
it was just a project idea, i did it and here it is.

## What is a Fuzzer?
A fuzzer is a program that tries to discover security vulnerabilities by sending an arbitrary input to an application. If the program contains a vulnerability that can lead to an exception, crash or server error (in the case of web apps), it can be determined that a vulnerability has been discovered. Fuzzers are often called Fault Injectors for this reason, they generate faults and send them to an application. Generally fuzzers are fine for encountering buffer overflow, DoS, SQL Injection, XSS, and Format String bugs. They do a poor job finding vulnerabilities related to information discovery, encryption flaws, and any other vulnerabilities that do not cause the program to crash.

## Recomendation
My recommendation is that you use full word lists, like [SecLists](https://github.com/danielmiessler/SecLists).

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
<img src="https://github.com/justgr0w/PyFuzzer/blob/main/photos/help.png" width="500">

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

* Example
<img src="https://github.com/justgr0w/PyFuzzer/blob/main/photos/fuzz.png" width="500">

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
* Install the following dependencies with python-pip
 ```
$ sudo pip install -r requirements.txt
```
