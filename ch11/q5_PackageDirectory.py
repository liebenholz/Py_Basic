import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치

import inspect
from travel import *
print(inspect.getfile(thailand)) # thailand 모듈의 위치