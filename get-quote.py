import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)

  text = quotes[rnd]
  text2 = quotes[rnd2]

  print(text.rstrip('\n')),
  print(text2.rstrip('\n'), end=""),

if __name__== "__main__":
  primary()
