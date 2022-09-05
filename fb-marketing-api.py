# source : https://github.com/facebook/facebook-python-business-sdk

# https://stackoverflow.com/questions/54846532/where-does-pipenv-install-packages
# /home/gada/.local/share/virtualenvs/calls-api-3BrbH1zm/lib/python3.8/site-packages
import sys
sys.path.append('/home/gada/.local/share/virtualenvs/calls-api-3BrbH1zm/lib/python3.9/site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append('/home/gada/.local/share/virtualenvs/calls-api-3BrbH1zm/lib/python3.9/site-packages/facebook_business-12.0.1.dist-info') # same as above

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

# load env
import os
from dotenv import load_dotenv
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
app_secret = os.getenv('APP_SECRET')
app_id = os.getenv('APP_ID')
id = os.getenv('AD_ACCOUNT_ID')
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'objective',
]
params = {
  'effective_status': ['ACTIVE','PAUSED'],
}
print(AdAccount(id).get_campaigns(
  fields=fields,
  params=params,
))

# added some comments here