
pqact generator
===============

You probably do not want to run this, as it is specific to the way I want ldm
to save files to disk for the WXLAB.

why did you do this?
--------------------

Okay, so the Unidata AWIPS pqact.conf is tuned to IDD feed, and the NWS AWIPS
config is expected to be customized to the exact operational needs of each WFO.
At the house, I want everything, and neither stock config gives me that.

Also, I don't like the 'group/year/month/day/hour/file' layout.  Most sites
don't generate enough products per day to make an hourly split needed.  Not
to mention, ldm's scour process kills off stuff older than a day or two.  The
ldm data_store is transitory.  Files need to hang around long enough to be
ingested by EDEX.  So, may as well make it convenient for my own use.


HEY YOU USED ANY FOR FEED TYPE
------------------------------

Yes.  I have found that noaaportIngester and pqing will do some weird things
with feed type, so I used ANY feeds everywhere.  It would be more important
if we were using the non-WMO products that are fed over IDD, but we are not
running IDD, are we?

WHAT ALL THAT OTHER STUFF?
--------------------------

Why are you so loud?  I have included ncf_rrdupd.pl, which is used to calculate
the delay on NCF's test messages.  The creation of an appropriate rrdb is left
as an exercise for the reader.
