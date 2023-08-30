import string
import random

# printing lowercase
letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(10)))
