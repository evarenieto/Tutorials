# LISTS

#classcreate a empy LISTS
attendees = []
attendees.append('Laura')
attendees.append('Rocio')
attendees.append('Susan')
print(attendees)
print('There are', len(attendees), 'attendees currently')

#create a empy LISTS
empy_list = []
#add items to the empty list
empy_list.append(9)
print(empy_list)

#crating a new list
temperatures = []
temperatures.append(38.5)
temperatures.append(39.2)
print(temperatures)
tem_ext = [36.8, 39.4, 36.5]
temperatures.extend(tem_ext)
print(temperatures)

#creatin a new list
#first lits
f_grade_family = ['Dani', 'Papa', 'Mama', 'Javier']
#second list
s_grade_family = ['Abuela', 'Abuelo', 'Abbuela']

all_grade_family = f_grade_family + s_grade_family
print(all_grade_family)
#this new variable (all_grade_family)doesnt change the value of the last two
#lets see
print(f_grade_family)

#lets create a new list

att = ['Pepe', 'Romero', 'Julian']
att.append('Justo')
att.extend(['Martin', 'Manuel'])
optional_att = ['Juan', 'Jesus', 'Blasco']
potencial_att = att + optional_att
print('There are', len(potencial_att), 'potencial atendees currently')

#lets create a different list

sp_sent = [
'te voy araña - Cordoba',
'la moño gordo - Miajadas',
'un parali - Cáceres'
]
print(sp_sent[1])
print(sp_sent[0])
print(sp_sent[-1])

print('La mejor de todas es: {}'   .format(sp_sent[0]))
#append add item to the end, insert add in a especific localitation.
sp_sent.insert(0, 'marichocho - tarde Extremadura')
print(sp_sent)
#to remove a item we use del
print(sp_sent)
del sp_sent[0]
print(sp_sent)
