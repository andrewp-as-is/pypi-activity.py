from datetime import timedelta
import pypi_activity

for change in pypi_activity.getchangelog(pypi_activity.gettimestamp(timedelta(days=3))):
    print(change.name,change.version,change.action,change.timestamp,)
