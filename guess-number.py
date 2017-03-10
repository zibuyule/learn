#! usr/bin/python #coding=utf-8 

import random



count = 0 
while count <1:
    num = random.randint(0,99)
    print num
    guess_age = int(raw_input("guess_age:" ) )
    if guess_age > num:
        print("you are bigger")
    elif guess_age < num:
        print("you are smaller")
    else:
        print("you are right!")
    count += 1  
    if count ==1:
        countinue_confirm = raw_input("Do you want continue guessing..?输入‘yes‘继续，输入‘no’退出.请输入: ")
        if countinue_confirm == 'yes':
            count =0 
        if countinue_confirm == 'no': 
            break
