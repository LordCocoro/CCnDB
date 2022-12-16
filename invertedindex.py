import sys
import pandas as pd

DIR = 'archivos_txt/'
DICTIONARY = {}

def main():
    a = []
    files = []
    txt= sys.argv[1]
    for i in range(1, 4):
        archivo = open(DIR+txt+str(i)+'.txt', "r")
        a.append(archivo.read().split())
        files.append(txt+str(i))
    archivo.close()

    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            try:
                DICTIONARY[a[i][j]]['count'] +=1
                try:
                    DICTIONARY[a[i][j]]['file'][files[i]] += 1
                except KeyError as g:
                    DICTIONARY[a[i][j]]['file'][files[i]]=1
            except KeyError as e:
                DICTIONARY[a[i][j]]={'count':1,'file':{files[i]:1}}
    
    #print(DICTIONARY)  

    for word in DICTIONARY:
        print(word,DICTIONARY[word])
    
    
    
if __name__ == '__main__':
   main()
    