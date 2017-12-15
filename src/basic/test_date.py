# from datetime import datetime
# dt = datetime.now()

# print dt

# import time

# starttime = time.time()

# time.sleep(10)

# endtime = time.time()

# print endtime - starttime

# import time

# start = time.clock()
#end = time.clock()

#print end, start

#elapsed = (end - start)

#print elapsed

import time
import timeit

start_time = timeit.default_timer()

time.sleep(10)

elapsed = timeit.default_timer() - start_time

print('%.10f seconds' % elapsed)