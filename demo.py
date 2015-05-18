__author__ = 'MaxTechTV'

import ytstats


userID = "MaxTechTV1"

yt = ytstats.ytstats(userID)


yt.getViews()

print("Aufrufe: " + str(yt.getViews()))
print("Abonnenten: " + str(yt.getSubscribers()))
