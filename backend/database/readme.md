### Database api
Database class, see dbutil.py
API for frontend, see db_api.py

usage
```python
from db_api import *
CYWDB.build()		#create a new sqlite database, build tables
CYWDB.load_goods()	#load goods information from specified json file, default jdspider/pL.json
CYWDB.load_goods_keyword(goodsKeyword)		#insert keyword-good relation into database
readWordVec()		#load word vector into memory for good retrieval

register_check_phone_existence(1234567)
...

```
if database has been built, just:
```python
from db_api import *
CYWDB.connect()		#connect to db
readWordVec()		#load word vector into memory for good retrieval

register_check_phone_existence(1234567)
...
```

Test code: test\*\*.py
usage
```bash
python3 testDB.py -v
python3 testDB_api.py -v
```

