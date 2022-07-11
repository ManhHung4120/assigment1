import io
import sys
import lib2
from lib2 import DATA,get_data,get_data_list
import pytest
from unittest import mock
from unittest.mock import patch
import unittest 
from io import StringIO



# write unittest for this function
def show_square():
    return_data = get_data()
    if not return_data:
        print ("False")
        return False
        
    
    data_list_data = get_data_list()
    for data_object in data_list_data:
        print(data_object.get('number') ** 2)
        if data_object.get('number') == 1:
            print("Found")
    return True

# show_square()
    # print ("True")



# @mock.patch('assigment1.get_data')
@pytest.mark.parametrize(["case","data","expect","stdout"],DATA)
# @patch('assigment1.get_data')
def test_show_square(case,data,expect,stdout):
    # key = data.get('check')
    # if not data.get('check'):
   
    mock.patch('test3.get_data', return_value = data.get('check')).start()
    mock.patch('test3.get_data_list', return_value =  data.get('input')).start()
    # print(case)
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    return_value = show_square()
    sys.stdout = sys.__stdout__
    # mock.patch('test3.get_data', return_value = data.get('check')).stop()
    # assert return_value == expect
    if len(data.get("check")) != 0:
        # print(capturedOutput.getvalue())
        assert capturedOutput.getvalue() == stdout
        assert return_value == expect
        
    else:
        assert return_value == expect
        
    
    
    
