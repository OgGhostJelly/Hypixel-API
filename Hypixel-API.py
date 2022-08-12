#mod
import os
#programs
main_dir = '.mod'
program = next(os.walk(main_dir))[2]
print('-[ Hypixel API ]-\n')
print('What would you like to do...')
print([x[:len(x)-3] for x in program])
e = input('>>> ')