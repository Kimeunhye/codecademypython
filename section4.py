# 4.1
from datetime import datetime
now = datetime.now()
print now

# 4.2
from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day

# 4.3
from datetime import datetime
now = datetime.now()
print str(now.month) + "/" + str(now.day) + "/" + str(now.year)

# 4.4
from datetime import datetime
now = datetime.now()
print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

# 4.5
print str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
