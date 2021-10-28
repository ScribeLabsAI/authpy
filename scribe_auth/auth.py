from typing import TypedDict
import requests

AccessToken = TypedDict('AccessToken', {'access': str})
AccessRefreshPair = TypedDict('AccessRefreshPair', {'access': str, 'refresh':str})

def get_tokens(username: str, password: str, api_key: str, baseurl: str='https://auth.scribelabs.ai') -> AccessRefreshPair:
  """Generates an access token and a refresh token to use in subsequent calls to the api.

  Args:
      username (str): Username (usually an email address)
      password (str): Password associated with this username
      api_key (str): Api key provided by Scribe (contact support@scribelabs.ai if you need one)
      baseurl (str, optional): Base url for the api. Should not need to be specified, expect in a situation where the url changes and the library has not been updated yet. Defaults to 'https://auth.scribelabs.ai'.

  Returns:
      AccessRefreshPair: Dictionary {"access": "token", "refresh": "token"}
  """
  headers = {
    'X-API-Key': api_key
  }
  resp = requests.get(f"{baseurl}/token", auth=(username, password), headers=headers)
  resp.raise_for_status()
  return resp.json()

def refresh_access_token(refresh_token: str, api_key: str, baseurl: str='https://auth.scribelabs.ai') -> AccessToken:
  """Generates a new access token from a refresh token.

  Args:
      refresh_token (str): Refresh token to use. It can be fetched with get_tokens.
      api_key (str): Api key provided by Scribe (contact contact@scribelabs.ai if you need one)
      baseurl (str, optional): Base url for the api. Should not need to be specified, expect in a situation where the url changes and the library has not been updated yet. Defaults to 'https://auth.scribelabs.ai'.

  Returns:
      AccessToken: Dictionary {"access": "token"}
  """
  headers = {
    'X-API-Key': api_key,
    'Authorization': f"Bearer {refresh_token}"
  }
  resp = requests.get(f"{baseurl}/refresh", headers=headers)
  resp.raise_for_status()
  return resp.json()

def revoke_refresh_token(refresh_token: str, api_key: str, baseurl: str='https://auth.scribelabs.ai') -> None:
  """Revokes a refresh token and all associated access tokens.

  Args:
      refresh_token (str): Refresh token to use. It can be fetched with get_tokens.
      api_key (str): Api key provided by Scribe (contact contact@scribelabs.ai if you need one)
      baseurl (str, optional): Base url for the api. Should not need to be specified, expect in a situation where the url changes and the library has not been updated yet.. Defaults to 'https://auth.scribelabs.ai'.
  """
  headers = {
    'X-API-Key': api_key,
    'Authorization': f"Bearer {refresh_token}"
  }
  resp = requests.get(f"{baseurl}/revoke", headers=headers)
  resp.raise_for_status()
