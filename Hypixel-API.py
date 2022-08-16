#mod
import os
from json import load as json_load
#get program
main_dir = '.mod'
program = {x[:len(x)-3] : main_dir + '/' + x for x in next(os.walk(main_dir))[2]}
program_extra = json_load(open('.mod/.data/program.json'))
#print
print('\n-[ Hypixel API ]-\n')
print('What would you like to do...\n')
program_print = ''
for x in program:
    program_print = program_print + x + ': ' + program_extra[x]['desc'] + '\n'
print(program_print)
#ask selected_program
inpt = input('>>> ')
try:
    exec(open(program[inpt]).read())
except:
    exit()
exec(open('Hypixel-API.py').read())

#remove extra from getAH.py