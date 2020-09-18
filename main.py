# Author: Krish Choudhary ksc5496@psu.edu   

def digit_sum(n):
  if n==0:
    return 0
  else:
    return int((n%10) + digit_sum(n//10))

def run():
  getInp = int(input("Enter an int: "))
  print(f"sum of digits of {getInp} is {digit_sum(getInp)}.")

if __name__ == "__main__":
  run()