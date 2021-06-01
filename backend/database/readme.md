### Database api
Database class, see dbutil.py
API for frontend, see db_api.py

usage
```python
from db_api import *
CYWDB.build()		#create a new sqlite database, build tables
CYWDB.load_goods()	#load goods information from specified json file, default jdspider/pL.json

register_check_phone_existence(1234567)
...

```

Test code: test\*\*.py
usage
```bash
python3 testDB.py -v
python3 testDB_api.py -v
```

