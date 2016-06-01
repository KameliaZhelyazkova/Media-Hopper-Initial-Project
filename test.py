from kaltura_lib.KalturaClient import *

config = KalturaConfiguration(123)
# where 123 is your partner ID

config.serviceUrl = "http://devtests.kaltura.co.cc/"
# if you want to communicate with a Kaltura server which is
#    other than the default http://www.kaltura.com

client = KalturaClient(config)

ks = client.generateSession(adminSecret, userId, type, partnerId, expiry, privileges)

client.setKs(ks)

