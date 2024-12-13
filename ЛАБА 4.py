import random
import tkinter
import tkinter.filedialog
import json

file = open('file.txt', 'w+')

a = []
b = 0

i=0
while(i < 10):
    rand = random.randint(0, 100)
    b = b + rand
    a.append(rand)
    i = i+ 1
    
print(a)




file.write(f'{a}')
file.close()

filePath = tkinter.filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files","*.txt"), ("All files", "*.*")])
file = open(filePath, 'r')

content = file.read()
content = json.loads(content)

print(content)
print(sum(content) / len(content))