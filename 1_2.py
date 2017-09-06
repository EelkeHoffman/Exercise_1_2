#a. Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
a= 'Supercalifragilisticexpialidocious'
b = len(a)
print(b)



#b. Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?

d = 'Supercalifragilisticexpialidocious'
c  = 'ice' in a
print(c)

#c. Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
d = "Antidisestablishmentarianism"
e = "onorificabilitudinitatibus"
f  = len(a)
g  = len(e)
h  = e > d
print(h)

#d. Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?

i = min('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
j = max('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
print ("eerst", i, "laatst", j)

