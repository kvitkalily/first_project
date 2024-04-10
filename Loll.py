import pytest
from py_strings import *

a = "fajna pOGODA 78 "    
print(f"Moj tekst przykladowy to: {a}")

#1
#assert reverse("abcd") == "dcba"
print("Pierwsze zadanie")

def reverse(tekst):
        return tekst[::-1]    
        
tekst = "abcd"      
b = reverse(tekst)
print(b)
print(reverse(a))

#2
#assert first_to_upper("abcd") == "Abcd"
#assert first_to_upper("litwo oJCZYZNO MoJa") == "Litwo OJCZYZNO Moja"
print("Drugie zadanie")

def first_to_upper(text):
	c = text.capitalize()
	b = c.split()
	if len(b) >= 2:
		b[1] = b[1].upper()
	result = ' '.join(b)
	#j = b[0] + " " + b[1].upper()
	return result 
	
b = "abcd"
c = "litwo oJCZYZNO MoJa" 
 
print(first_to_upper(b)) 
print(first_to_upper(c))      
print(first_to_upper(a))

print("Trzecie zadanie")
#3	
#assert count_vowels("abcdef") == 2
#assert count_vowels("AbcdeF") == 2
#assert count_vowels("XYZ") == 1
#assert count_vowels("XZ") == 0
 
def count_vowels(t):
	vowels = 0
	l = len(t)
	for i in range (l):
		if t[i] in "AEUOIYyaeuio":
			vowels +=1
	print(vowels)
s = "abcdef" #sprawdzenie 1
ss = "AbcdeF" #sprawdzenie 2
sss = "XYZ" #sprawdzenie 3
ssss = "XZ" #sprawdzenie 4
count_vowels(s)
count_vowels(ss)
count_vowels(sss)
count_vowels(ssss)
print("Teraz to dla mego tekstu ilosc vowels XD")
count_vowels(a)	


print("Czwarte zadanie")
#4
#assert sum_digits("It's 911, what is your emergency?") == 11
#assert sum_digits("3... 2... 1... kaboom!") == 6
#assert sum_digits("Failure is not an option") == 0

def sum_digits(textt):
	total = 0
	for i in textt:
		if i.isdigit():#sprawdzamy znaczek i czy jest cyfra - isdigit.
			total += int(i) #konwertujemy w liczbe calkowita
	print(total)
#cyfry sa tutaj typu str, poniewaz zapisane w "", dlatego musimy ich konwertowac	


k = "It's 911, what is your emergency?"#sprawdzenie 1
kk = "3... 2... 1... kaboom!" #sprawdzenie 2
kkk = "Failure is not an option"#sprawdzenie 3
sum_digits(k)
sum_digits(kk)
sum_digits(kkk)
print("To wynik dla mego tekstu")
sum_digits(a)
#5
#assert search_substr("Litwo, Ojczyzno moja", "wo") == 3
#assert search_substr("Litwo, Ojczyzno moja", "wa") == None


print("Piate zadanie")
def search_substr(te):
	tekst, string = te 
	c = tekst.find(string)
	if c == -1:
		print("None")
	else: print(c)
	
r = ("Litwo, Ojczyzno moja", "wo")
rr = ("Litwo, Ojczyzno moja", "wa")	
search_substr(r)#sprawdzenie 1
search_substr(rr)#sprawdzenie 2
a = ("fajna pOGODA 78 ", "na" )   
search_substr(a)

