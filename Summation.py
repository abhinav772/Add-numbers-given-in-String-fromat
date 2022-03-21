def summation_of_two_strings(string1, string2):
    summation = [0] * len(string1)
    if len(string1) == len(string2):
        for i in range(len(string1)-1,-1,-1):
            if i == len(string1)-1:
                summation[i] = str((int(string1[i]) + int(string2[i])) % 10)
            elif i in range(len(string1)-2,0,-1):
                tens_place = (int(string1[i+1]) + int(string2[i+1])) // 10
                summation[i] = str(((int(string1[i]) + int(string2[i])) + tens_place) % 10)
            else:
                tens_place = (int(string1[i+1]) + int(string2[i+1])) // 10
                summation[i] = str((int(string1[i]) + int(string2[i])) + tens_place)  
    else:
       if len(string1) > len(string2):
          larger_string = string1
          smaller_string = string2
          large_length = len(string1)
          small_length = len(string2)
       else:
           larger_string = string2
           smaller_string = string1
           large_length = len(string2)
           small_length = len(string1)
       summation = [0] * (small_length+1)
       new_string = larger_string[(large_length-small_length):large_length]
       left_over = larger_string[0:(large_length-small_length)]
       if len(new_string) == len(smaller_string):
           for i in range(len(new_string)-1,-2,-1):
               if i == len(new_string)-1:
                   summation[i+1] = str((int(new_string[i]) + int(smaller_string[i])) % 10)
               elif i in range(len(new_string)-2,-1,-1):
                   tens_place = (int(new_string[i+1]) + int(smaller_string[i+1])) // 10
                   summation[i+1] = str((int(new_string[i]) + int(smaller_string[i]) + tens_place) % 10)
                   last_place = (int(new_string[i]) + int(smaller_string[i]) + tens_place) // 10
               else:  
                   summation[i+1] = str(int(left_over) + last_place)  
    return summation
    
result_of_summation = summation_of_two_strings('2344','494334')
''.join(result_of_summation)
