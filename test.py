import os
print('You Are Running In ' + os.name + ' ' + os.getcwd())
os.system('mkdir sb')
f = open('downpack.py','w')
f.write("print ('download from Zombie github')")
