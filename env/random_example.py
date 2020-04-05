import random




value = random.random()
print(value)


value2 = random.uniform(1,10)
print(value2)

valueInt =random.randint(1,10)
print(valueInt)

winner=['Won','Try again', 'Hard Luck', 'loser You']

value5 =random.choice(winner)
print(value5 +' '+'Jones')

colours= ['black', 'green', 'blue']
value6 = random.choices(colours, k=10)

print(value6)

def return_sum(x,y):
    c = x + y
    return c

res = return_sum(30,5)
print(res)

deck =list(range(1,100))
hand =random.sample(deck,k=5)
print(hand)


for i in range(10):
 vlaue7=random.random()*100000000
print(vlaue7)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

print (random_with_N_digits(2))
print (str(random_with_N_digits(6)))
print (random_with_N_digits(8))