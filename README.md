What is fibonacci_web_service?
-------------

RESTful web service that accepts a positive number, as input and returns the first n Fibonacci numbers.
If a negative number is used it returns an error stating so.

Requirements
------------

You need Python 3.4 or later to run fibonacci_web_service.  You can have multiple Python
versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo apt-get install python3 python3-pip

For other Linux flavors, OS X and Windows, packages are available at

  http://www.python.org/getit/
  
You also need to have flask installed.

In Ubuntu, Mint and Debian you can install flask like this:

    $ sudo pip3 install flask
    
Make sure git is also installed, if not you can install it like this:

    $ sudo apt-get install git  


Quick start
-----------
To get the latest fibonacci_web_service run the following command:

    $ git clone https://github.com/MiguelEVeliz/fibonacci_web_service.git
    $ cd fibonacci_web_service

To run fibonacci_web_service run the following commnad:

    $ python3 fibonacci_web_service.py

Use a webbrowser and go to http://127.0.0.1:5000/?n='x' where is x is an integer for example: http://127.0.0.1:5000/?n=10

Another option is to use the curl command like this:

    $ curl -i http://127.0.0.1:5000/?n=10
    
Quick start Docker
-----------    
To run the latest fibonacci_web_service from a docker container run the following command:


    $ sudo docker run -p 5000:5000 migueleveliz/fibonacci_web_service
 
 
 Use a webbrowser and go to http://127.0.0.1:5000/?n='x' where is x is an integer for example: http://127.0.0.1:5000/?n=10

Another option is to use the curl command like this:

    $ curl -i http://127.0.0.1:5000/?n=10

Testing and Troubleshooting
-----------
To troubleshoot the fibonacci_web_service i have included an automatic test program, to run it use the following command:

    $ python3 test.py

This will run 4 automated test and report result and time it took to run the specif test.
 
