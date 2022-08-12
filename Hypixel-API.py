#mod
import os
from re import X
#get program
main_dir = '.mod'
program = {x[:len(x)-3] : main_dir + '/' + x for x in next(os.walk(main_dir))[2]}

#print
print('\n-[ Hypixel API ]-\n')
print('What would you like to do...')
program_print = [x for x in program]
program_print.append('exit')
print(program_print)
#ask selected_program
inpt = input('>>> ')
try:
    exec(open(program[inpt]).read())
except:
    exit()
exec(open('Hypixel-API.py').read())

#remove extra from getAH.py