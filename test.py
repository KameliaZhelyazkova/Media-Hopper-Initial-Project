from kaltura_lib.KalturaClient import *

partnerID = 1817881
admin_secret = "1a7227978d8228dde2a574fac2c9b371"
userID = "kamelia.zhelyazkova@ed.ac.uk"
ks_type = 2
expiry = 360
privileges = ""



config = KalturaConfiguration(partnerID)
# where 123 is your partner ID

config.serviceUrl = "http://devtests.kaltura.co.cc/"
# if you want to communicate with a Kaltura server which is
# other than the default http://www.kaltura.com

client = KalturaClient(config)

ks = client.generateSession(admin_secret, userID, ks_type, partnerID, expiry, privileges)

client.setKs(ks)

print("DONE!")