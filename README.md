# Scribe auth
##### Python package for interacting with Scribe's auth api.

-----
Most calls to Scribe's api on https://api.scribelabs.ai require a [JWT](https://jwt.io) for authentication and authorisation. This library simplifies this process.

You first need a Scribe account and an api key. Both can be requested at contact[atsign]scribelabs[dotsign]ai.

----
This library requires a version of Python 3 that supports typings.

### Installation
```bash
pip install scribe-auth
```

### 1. Fetching an access token and a refresh token
```python
from scribe_auth import get_tokens
tokens = get_tokens('myusername', 'mypassword', 'myapikey')
# tokens = {"access": "token", "refresh": "token"}
```

### 2. Refreshing an access token with a refresh token
```python
from scribe_auth import refresh_access_token
token = refresh_access_token('myrefreshtoken', 'myapikey')
# token = {"access": "token"}
```

### 3. Revoke a refresh token and associated access tokens
```python
from scribe_auth import revoke_refresh_token
revoke_refresh_token('myrefreshtoken', 'myapikey')
```
---
To flag an issue, open a ticket on [Github](https://github.com/scribelabsai/authpy/issues).