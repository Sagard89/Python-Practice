import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
	sys.path.insert(1, path)
	
del path
from UnderstandingDecorators1 import my_decorator

@my_decorator
def sampleFunction(): 
   print("This is a sample function")

##sampleFunction = my_decorator(sampleFunction)
sampleFunction()
