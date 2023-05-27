# student un-pickling data
import pickle
try:
     with open("data.txt", "rb") as fp:
         print("-" * 30)
         while True:
              try:
                   print("")
                   obj = pickle.load(fp)
                   for val in obj:
                        print("{}".format(val), end="\t")
              except EOFError:
                   print("\n","-"*30)
                   break

except FileNotFoundError:
     print("File does not exit")