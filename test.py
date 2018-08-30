import urllib.request
import time
start_time = time.time()

# Define test results.
TEST_RESULT_1 = "0, 1"
TEST_RESULT_2 = "0, 1, 1, 2, 3, 5"
TEST_RESULT_3 = "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
TEST_RESULT_4 = "Invalid Number, please enter a positive number"

#: First test
response = urllib.request.urlopen('http://localhost:5000/?n=1')
test_response_1 = response.read()
test_response_1 = test_response_1.decode("utf8")
print("Running Test 1:")
if TEST_RESULT_1 == test_response_1:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")
print("--- %s seconds ---\n" % (time.time() - start_time))

#: Second test
response = urllib.request.urlopen('http://localhost:5000/?n=5')
test_response_2 = response.read()
test_response_2 = test_response_2.decode("utf8")
print("Running Test 2:")
if TEST_RESULT_2 == test_response_2:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")
print("--- %s seconds ---\n" % (time.time() - start_time))

#: Third test
response = urllib.request.urlopen('http://localhost:5000/?n=10')
test_response_3 = response.read()
test_response_3 = test_response_3.decode("utf8")
print("Running Test 3:")
if TEST_RESULT_3 == test_response_3:
    print("Test 3 Passed")
else:
    print("Test 3 Failed")
print("--- %s seconds ---\n" % (time.time() - start_time))

#: Forth test
response = urllib.request.urlopen('http://localhost:5000/?n=-1')
test_response_4 = response.read()
test_response_4 = test_response_4.decode("utf8")
print("Running Test 4:")
if TEST_RESULT_4 == test_response_4:
    print("Test 4 Passed")
else:
    print("Test 4 Failed")
print("--- %s seconds ---\n" % (time.time() - start_time))
