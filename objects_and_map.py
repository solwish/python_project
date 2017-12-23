class Person:
    department = 'Information Technology'
    
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location
        
person = Person()
person.set_name('Christopher Nolan')
person.set_location('Ann Fisher, KR')
print('{} live in {} and work in {}').format(person.name, person.location, person.department)

#map

s1 = [1.2, 4.5, 4.4, 3.0]
s2 = [1.2, 3.4, 5.6, 6.7]
min = map(min, s1, s2)

print min

m = 100
for i in min:
    if m > i:
        m = i
print m