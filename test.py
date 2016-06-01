from kaltura_lib.KalturaClient import *

partnerID = 
admin_secret =
userID =
ks_type =
expiry =
privileges =




config = KalturaConfiguration(123)
# where 123 is your partner ID

config.serviceUrl = "http://devtests.kaltura.co.cc/"
# if you want to communicate with a Kaltura server which is
#    other than the default http://www.kaltura.com

client = KalturaClient(config)

ks = client.generateSession(admin_secret, userID, ks_type, partnerID, expiry, privileges)

client.setKs(ks)

