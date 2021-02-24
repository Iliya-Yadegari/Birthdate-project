#!/usr/bin/env python3
'''
Author: "Iliya Yadegari"
The python code in this file (a1_Iliya_Yadegari.py) is original work written by
"Iliya Yadegari". No code in this file is copied from any other source 
except those provided by the teacher, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading. 
'''
import os
import sys

def leap_year(obj):
    '''
    If there is no remainder return This is a leap year else This is not a leap year.
    '''
    if obj % 4 == 0:
        status = 'This is a leap year'
    else:
        status = 'This is not a leap year'
    return status

numbers_of_characters = 256
 
def lst_conv(obj1):
    temp = []
    for i in obj1:
        temp.append(i)
    return temp

def string_conv(lst):
    return ''.join(lst)

def char_count_array(obj1):
    count = [0] * numbers_of_characters
    for i in obj1:
        count[ord(i)] += 1
    return count


def sanitize(obj1,obj2):
    '''
    This function removes the letters in obj2 from obj1 then returns the new obj1
    '''
    count = char_count_array(obj2)
    ip_ind = 0
    res_ind = 0
    temp = ''
    str_list = lst_conv(obj1)
 
    while ip_ind != len(str_list):
        temp = str_list[ip_ind]
        if count[ord(temp)] == 0:
            str_list[res_ind] = str_list[ip_ind]
            res_ind += 1
        ip_ind += 1
    results = string_conv(str_list[0:res_ind])
    return results

def size_check(obj, intobj):
    '''
    This function sees if the number of items in obj matches intobj
    '''
    if len(obj) == intobj:
        return True
    else:
        return False

def range_check(obj1, obj2):
    '''
    This function checks that obj1 is in range of obj2[0] and obj[1]
    '''
    if obj1 in range(obj2[0],obj2[1]):
        return True
    else:
        return False
    
def usage():    
    '''
    If there is something wrond with the input print this
    '''
    if len(user_date) == 8:
        print('Usage: YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD')

if __name__ == "__main__":
   # step 1
   user_date = input('Please Enter your Date of Birth: ')
   usage()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = user_date
   
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   
   # step 8
   print("Your date of birth is:", new_dob)  
