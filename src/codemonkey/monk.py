import time as t

# message, you can set this to whatever

def Monkey(msg: str, range: int):

  monkey1 = """
            __
        w c(..)o   (
        |__(-)    __)
            /|   (
            (_)___)
            /|
           | |
           m  m
             """
  monkey2 = """
             __
       )   c(..)o w
      (__    (-)__|
         )   /|
        (____(_)
             /|
            / |
            m m
             """
  monkey = 1
  for x in range(range):
      for i in range(200):
        print()
      print(msg)
      if monkey == 1:
          print(monkey1)
          monkey = 2
      else:
          print(monkey2)
          monkey = 1
      t.sleep(0.5)
