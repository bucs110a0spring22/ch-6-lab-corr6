
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count                  # the last print is 1

import turtle

def turtleGraph(n):
  dart=turtle.Turtle()
  darty=turtle.Turtle()
  wn=turtle.Screen()
  wn.setworldcoordinates(0,0,10,10)
  max_so_far=0
  for i in range(1, n+1):
    result=seq3np1(i)
    if max_so_far <= result:
      max_so_far=result
      wn.setworldcoordinates(0,0,n+10,max_so_far+10)
      dart.clear()
      dart.goto(0,max_so_far)
      dart.write(("Maximum so far: ", i,max_so_far))
    darty.goto(i,seq3np1(i))
  wn.exitonclick()

def main():
  start=int(input("Enter a Positive Number: "))
  while start<1:
    exit()
  for i in range(1,start+1):
    print(i,seq3np1(i))
  turtleGraph(start)
main()