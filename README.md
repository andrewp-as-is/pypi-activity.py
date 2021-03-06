<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pypi-activity.svg?maxAge=3600)](https://pypi.org/project/pypi-activity/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pypi-activity.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pypi-activity.py/actions)

### Installation
```bash
$ [sudo] pip install pypi-activity
```

#### Examples
```python
from datetime import timedelta
import pypi_activity

for change in pypi_activity.getchangelog(pypi_activity.gettimestamp(timedelta(minutes=10))):
    print(change.name,change.version,change.action,change.timestamp,)
```

action|example
-|-
`create`|`PyKeeSAP None create 1592239659`
`new release`|`PyKeeSAP 1 new release 1592239659`
`remove project`|`epyauvi None remove project 1592226089`
`add Maintainer`|`pymc3 None add Maintainer id.mosthege.net 1592235439`
`add Owner`|`bsoid None add Owner HSUAI 1592240050`
`change Maintainer`|`virtualenv None change Maintainer gaborbernat to Owner 1591992009`
`change Owner`|`polyswarm None change Owner polyswarm-gitlab to Maintainer 1592225554`
`remove Maintainer`|`pivotal-django-zendesk None remove Maintainer thenautumn 1592238459`
`remove Owner`|`polyswarm-api None remove Owner polyswarmbsadmin 1592225540`
`add ... file`|`pymplschapters 1.0.4 add py3 file pymplschapters-1.0.4-py3-none-any.whl 1592239702`

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
