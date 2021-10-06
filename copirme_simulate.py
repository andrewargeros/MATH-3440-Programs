from random import randint # This is a standard module... I don't feel like reinventing the wheel

def gcd(p,q):
  '''Return the Largest Number that Evenly Divides p and q'''
  while q != 0:
    p, q = q, p%q # returns the remainder of p/q
  return p

def are_coprime(p,q):
  '''Two Integers p,q are coprime if their greatest common factor is 1'''
  return gcd(p,q) == 1

def sample_and_check():
  '''Check if two random ints are coprime'''
  return are_coprime(randint(1,10000), randint(1,10000))

def simulate(draws):
  '''Run Simulation of coprime check and return proportion of coprime'''
  counter = 0
  for i in range(draws):
    if sample_and_check():
      counter += 1 # increments for each coprime

  prop_coprime = counter/draws

  print(f'Proportion of Coprime Integers: {round(prop_coprime*100,2)}%')

def main():
  times = int(input('How many times do you want to simulate? '))
  simulate(times)

if __name__ == '__main__':
  main()