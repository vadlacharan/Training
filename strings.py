#concatenation
#indexing 
#reverse_indexing


#slicing

string="Helloworld"

#10 9 8 7 6 5 4 3 2 1
#h  e l l o w o r l d
#0  1 2 3 4 5 6 7 8 9 


#first five letters
print(string[:5])
print(string[:6])


#last five letters
print( string[-5:])

#indexing from middle
print( string[3:9])

#string reverse using slicing
print(string[::-1])


#step slicing
print( string[::3])