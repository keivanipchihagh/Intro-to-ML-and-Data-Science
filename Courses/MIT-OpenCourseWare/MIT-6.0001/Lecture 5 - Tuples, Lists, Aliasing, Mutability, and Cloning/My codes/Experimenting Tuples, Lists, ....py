def get_data(aTuple):    
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        nums += (t[0],)   
        words += (t[1],)
        
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"),(2015, "Joe"))
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, "Taylor Swift wrote songs about", num_people, "people!", end = '\n' * 3)

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L1.extend([7, 8])

L = [2, 1, 3, 6, 3, 7, 12]
L.remove(2)
print(L)
del(L[1])
print(L)
print(L.pop())

L=[9,6,0,3]
print(sorted(L))
L.sort()
L.reverse()

a = 1
b = a
a = 2
print(a)
print(b)

cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool, end = '\n' * 3)

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
      
def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1, L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)

cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)
print(warm)

colors1 = [cool]
print(colors1)
colors1.append(warm)
print('colors1 = ', colors1)

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)

warm.remove('red') 
print('colors1 = ', colors1)
print('colors2 =', colors2)

for e in colors1:
    print('e =', e)

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1)
    else:
        print(e)

flat = cool + warm
print('flat =', flat)

print(flat.sort())
print('flat =', flat)

new_flat = sorted(flat, reverse = True)
print('flat =', flat)
print('new_flat =', new_flat)

cool[1] = 'black'
print(cool)
print(colors1)
