_author_ ='Miguel Veliz'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    fibonacci_web_service.py
    ~~~~~~~~~~~~~~

   RESTful web service that accepts a positive number, 
   as input and returns the first n Fibonacci numbers

"""

from flask import Flask
from flask import request

app = Flask(__name__)

fibonacci_number_list = []

#: Function to Calculate Fibonacci numbers
def calculate_fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1)+calculate_fibonacci(n-2)

#: create the / end point
@app.route('/', methods=['GET'])
#: define main function for endpoint
def return_fibonacci():
    #: 127.0.0.1:5000/?n='int'
    number = int(request.args.get('n'))

    #: check for negative number
    if number < 0:
        return "Invalid Number, please enter a positive number"
    else:
        #: clear list for multiple calls
        fibonacci_number_list.clear()

        #: Calculates the fibonacci number and adds to a list
        for x in range(number+1):
            fibonacci_number_list.append(calculate_fibonacci(x))

        #: returns the list of fibonacci number formated.
        return str(fibonacci_number_list).strip('[]')


#: runs the application and defines the port number
app.run(port=5000)
