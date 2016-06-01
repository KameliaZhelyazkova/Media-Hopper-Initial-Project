from kaltura_lib.KalturaClient import *
from secret import admin_secret, partnerID

userID = "kamelia.zhelyazkova@ed.ac.uk"
ks_type = 2


config = KalturaConfiguration(partnerID)
# where 123 is your partner ID

config.serviceUrl = "http://www.kaltura.com"
# if you want to communicate with a Kaltura server which is
# other than the default http://www.kaltura.com

client = KalturaClient(config)

ks = client.generateSession(admin_secret, userID, ks_type, partnerID)
print ks
client.setKs(ks)


print("DONE!")


entryId = "1_yacymbd7";
# a known ID of media entry that you have

try:
    mediaEntry = client.media.get(entryId)
    print mediaEntry.getName()
except Base.KalturaException, e:
    print "could not get entry from Kaltura. Reason: %s" % repr(e)

