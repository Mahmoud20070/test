import glob
import pandas as pd
import os
from datetime import datetime

db_location = r'\\mypath\mypath\DB' #for windows

datecase = datetime(year=2024,month=1,day=1)

# Optimized file listing with glob
file_paths = glob.glob(os.path.join(db_location, datecase.strftime("%b-%y"), "Tickets","*"))


print(file_paths)
