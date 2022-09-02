# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys
sys.path.append('/home/gada/.local/share/virtualenvs/calls-api-3BrbH1zm/lib/python3.8/site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append('/home/gada/.local/share/virtualenvs/calls-api-3BrbH1zm/lib/python3.8/site-packages/facebook_business-12.0.1.dist-info') # same as above

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = 'EAAGfdQxJaG4BAGLZCQsj6V8Mxz3eqFrI7rIQZASvTRYnw8GfPg3gnU8maDMu6348qZA74FucGk00qPWfKZCdCXy4ozODRkufmfRQ21yJkRBgKU14BvpoUgXVHTlsXZB7b4pW4KTC4DsgBe1GbrE7GE5Alqc6kKAXJctRvcquJqNUN530HsDrpgzLHgXYys0cZD'
ad_account_id = 'act_372536734266019'
app_secret = '7be3b9c4fc8b4c57e609cccb3be4d44a'
page_id = '106261775324735'
app_id = '456800042838126'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
    'name': 'My Campaign',
    'buying_type': 'AUCTION',
    'objective': 'PAGE_LIKES',
    'status': 'PAUSED',
}
campaign = AdAccount(ad_account_id).create_campaign(
    fields=fields,
    params=params,
)
print('campaign', campaign)

campaign_id = campaign.get_id()
print('campaign_id:', campaign_id, '\n')

fields = [
]
params = {
    'name': 'My AdSet',
    'optimization_goal': 'PAGE_LIKES',
    'billing_event': 'IMPRESSIONS',
    'bid_amount': '20',
    'promoted_object': {'page_id': page_id},
    'daily_budget': '1000',
    'campaign_id': campaign_id,
    'targeting': {'geo_locations':{'countries':['US']}},
    'status': 'PAUSED',
}
ad_set = AdAccount(ad_account_id).create_ad_set(
    fields=fields,
    params=params,
)
print('ad_set', ad_set)

ad_set_id = ad_set.get_id()
print('ad_set_id:', ad_set_id, '\n')

fields = [
]
params = {
    'name': 'My Creative',
    'object_id': page_id,
    'title': 'My Page Like Ad',
    'body': 'Like My Page',
    'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
}
creative = AdAccount(ad_account_id).create_ad_creative(
    fields=fields,
    params=params,
)
print('creative', creative)

creative_id = creative.get_id()
print('creative_id:', creative_id, '\n')

fields = [
]
params = {
    'name': 'My Ad',
    'adset_id': ad_set_id,
    'creative': {'creative_id':creative_id},
    'status': 'PAUSED',
}
ad = AdAccount(ad_account_id).create_ad(
    fields=fields,
    params=params,
)
print('ad', ad)

ad_id = ad.get_id()
print('ad_id:', ad_id, '\n')

fields = [
]
params = {
    'ad_format': 'DESKTOP_FEED_STANDARD',
}
print(Ad(ad_id).get_previews(
    fields=fields,
    params=params,
))

