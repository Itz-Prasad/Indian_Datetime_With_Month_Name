from datetime import datetime
import pytz

# Setting Indian time zone
IST = pytz.timezone('Asia/Kolkata')
#Getting Indian time
Date_India = datetime.now(IST)
# Specifying format (Format : %Y:%m:%d %H:%M:%S %Z %z ) or (Format : %Y:%b:%d %H:%M:%S %Z %z )
# Use %m for month number and %b for month name
format = "%d %b %Y %H:%M"
# Printing time
STD_Date_India = Date_India.strftime(format)

print(STD_Date_India)
