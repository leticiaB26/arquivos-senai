def numeros ():
 num = int(input ("Digite um número:")) 
 return num

def contagem (num):
    if num > 0:
     for x in range( 1, num +1):
         print (x)

def main ():
    num = numeros()
    contagem (num)

main()