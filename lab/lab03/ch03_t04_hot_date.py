from datetime import datetime

now = datetime.now()

print(print('%02d-%02d-%04d' % (now.month, now.day, now.year))
)