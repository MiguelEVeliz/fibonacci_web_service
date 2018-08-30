_author_ = 'Miguel Veliz'

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
    """This Function takes a number and calculate its
    fibonacci, it number is 0 then returns 0, if number
    is 1 then returns 1, if number is greater than 1 then
    Function(n-1)+Function(n-2)"""

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


"""This Function calls the calculate_fibonacci function
builds a list with each result, and prints it out in a
formatted way"""
#: 127.0.0.1:5000/?n='int'
    number = int(request.args.get('n'))
    """The format of the web address is  127.0.0.1:5000/?n='int'
    where int is a integer for example:  127.0.0.1:5000/?n=10"""
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
