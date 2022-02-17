
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

# todo-env this
access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'objective',
]
params = {
  'effective_status': ['ACTIVE','PAUSED'],
}
print AdAccount(id).get_campaigns(
  fields=fields,
  params=params,
)

