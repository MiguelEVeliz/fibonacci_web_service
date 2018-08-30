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
  
You also need to have flask install.

In Ubuntu, Mint and Debian you can install Python 3 like this:

    $ sudo python3-pip install flask
    
Make sure git is also installed, if not you can install it like this:

    $ sudo apt-get install git  


Quick start
-----------
To get the latest fibonacci_web_service run the following command:

    $ git clone https://github.com/MiguelEVeliz/fibonacci_web_service.git
    $ cd fibonacci_web_service

To run fibonacci_web_service run the following commnad:

    $ python3 fibonacci_web_service.py
