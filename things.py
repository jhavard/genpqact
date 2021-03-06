
models = ['HA', 'HE', 'HH', 'HP', 'HR', 'HT', 'HU', 'HV', 'YA', 'YB', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH',
		'YI', 'YJ', 'YK', 'YO', 'YP', 'YQ', 'YR', 'YS', 'YT', 'YU', 'YV', 'YW', 'YX', 'YY', 'YZ',
		'ZA', 'ZB', 'ZC', 'ZD', 'ZE', 'ZF', 'ZG', 'ZH', 'ZO', 'ZP', 'ZQ', 'ZR', 'ZS', 'ZT', 'ZU',
		'ZV', 'ZW', 'ZX', 'ZY', 'ZZ']

nonmod = ['AB', 'AC', 'AE', 'AG', 'AS', 'AT', 'AU', 'AW', 'AX', 'CD', 'CX', 'FA', 'FE', 'FG', 'FL', 'FM',
		'FN', 'FO', 'FP', 'FR', 'FS', 'FT', 'FW', 'FX', 'FZ', 'IS', 
		'NG', 'NO', 'NW', 'NZ', 'OA',
		'OB', 'OC', 'OJ', 'OK', 'OM', 'ON', 'OP', 'OY', 'PE', 'PG', 'PH', 'PJ', 'PM', 'PP', 'PR',
		'PS', 'PT', 'PW', 'PX', 'PY', 'RX', 'SH', 'SO', 'SR', 'SX', 'TX', 'UB', 'UD', 'XX',
		'UE', 'UF', 'UG', 'UH', 'UK', 'UL', 'UM', 'UP', 'UQ', 'US', 'UX', 'WA', 'WG', 'WH', 
		'WS', 'WU', 'WW', 'UZ', 'UR']

radars = ['SD']

tstmsg = ['NT']

# Special codes WO, NX

# also, any other binary products that aren't model grids...
# may also include some upper air stuff (IU)
satdat = ['IU', 'JA', 'JC', 'JE', 'JG', 'JH', 'JJ', 'JM', 'JP', 'JQ', 'JR', 'JS', 'JU', 'TI']

for x in models:
	# straight WMO
	print "ANY\t^(%s....) (....) (......)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/model/misc/%Y/%m/%d/%H/\\1_\\2_\\3_(seq).%Y%m%d%H"
	print ""

	# WMO with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/model/misc/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# straight PIL/MIL
	print "ANY\t^(%s....) (....) (......) /[mp](.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/model/\\4/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# PIL/MIL with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..) /[mp](.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/model/\\5/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
	print ""

for x in radars:
	print "ANY\t^%s..(..) (....) (......) /p(...)(...)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/radar/\\5/%Y%m%d/%H/\\5_\\4_\\2_\\3_\\1_(seq).%Y%m%d%H.radar"
	print ""

# NXUS6[0-9] is the General Status Message
# AFAICT, this is not decoded by AWIPS, but it is stuffed into the fxatext database.  ick!
print "ANY\t^NXUS6. (....) (......) /p(...)(...)"
print "\tFILE\t-log -close -overwrite\t/awips2/data_store/radar/\\4/%Y%m%d/%H/\\4_\\3_\\1_\\2_(seq).%Y%m%d%H.gsm"
print ""

for x in satdat:
	# straight WMO
	print "ANY\t^(%s....) (....) (......)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/%H/\\1_\\2_\\3_(seq).%Y%m%d%H"
	print ""
	
	# WMO with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""
	
	# straight PIL
	print "ANY\t^(%s....) (....) (......) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# PIL with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/%H/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
	print ""

for x in nonmod:
	# straight WMO
	print "ANY\t^(%s....) (....) (......)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_(seq).%Y%m%d%H"
	print ""

	# WMO with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# straight PIL
	print "ANY\t^(%s....) (....) (......) /[mp](.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# PIL with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..) /[mp](.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
	print ""


# Special handling for all other NX..[0-57-9]. messages

# straight WMO
print "ANY\t^(NX..[0-57-9].) (....) (......)$"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_(seq).%Y%m%d%H"
print ""

# WMO with BBB
print "ANY\t^(NX..[0-57-9].) (....) (......) ([A-Z0-9]..)$"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
print ""

# straight PIL
print "ANY\t^(NX..[0-57-9].) (....) (......) /[mp](.*)"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
print ""

# PIL with BBB
print "ANY\t^(NX..[0-57-9].) (....) (......) ([A-Z0-9]..) /[mp](.*)"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\2/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
print ""


# Special handling for WO to skip KNCF test messages

# straight WMO
print "ANY\t^(WO..[0-8].) (....) (......)$"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/misc/%Y/%m/%d/%H/\\1_\\2_\\3_(seq).%Y%m%d%H"
print ""

# WMO with BBB
print "ANY\t^(WO..[0-8].) (....) (......) ([A-Z0-9]..)$"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/misc/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
print ""

# straight PIL
print "ANY\t^(WO..[0-8].) (....) (......) /[mp](.*)"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\4/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
print ""

# PIL with BBB
print "ANY\t^(WO..[0-8].) (....) (......) ([A-Z0-9]..) /[mp](.*)"
print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/text/\\5/%Y/%m/%d/%H/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
print ""


# Now we handle test messages

# WOUS99 is the KNCF test message

print "# WOUS99 is the KNCF test message so we not only save it, but EXEC"
print "# a script to stat the file and then log the mtime to an rrd file."
print "# That delay is approximately the time it takes for a message to leave"
print "# the NCF servers, travel through the transmission equipment, up to a"
print "# geosynchronuos satellite, bounce off a parabolic reflector in my back"
print "# yard, into a low noise block amplifier, travel through a piece of RG-6"
print "# and into a Novra S300N receiver, be converted back into IP packets, hit"
print "# the switch, dig its way into cp1, be decoded by noaaportIngester, be"
print "# processed by LDM and its pqact and be written to the file system"
print ""
print "ANY\t^WOUS99 KNCF ......"
print "\tFILE\t-log -close -overwrite\t/awips2/data_store/tstmsg/NCF.KNCF"
print ""
print "ANY\t^WOUS99 KNCF (..)(..)(..)"
print "\tEXEC\t/export/stats/ncf_rrdupd.pl \\1 \\2 \\3"
print ""



for x in tstmsg:
	# Usually, these are TSTMSG.  They don't appear to use MONMSG these days.
	# also, PTWC does something a little different.  This is why we save SITE.PIL
	# as it may be important.
	#
	print "ANY\t^%s.... (....) ...... /p(.*)" % x
	print "\tFILE\t-log -close -overwrite\t/awips2/data_store/tstmsg/\\1.\\2"
	print ""

	# turns out, a significant number of those test messages no longer have a PIL code
	# I bet they used to be MONMSG...
	print "ANY\t^%s.... (....) ......$" % x
	print "\tFILE\t-log -close -overwrite\t/awips2/data_store/tstmsg/\\1.\\1"
	print ""

# don't forget the miscellaneous junk... save it but don't feed to EDEX
print "ANY\t^_ELSE_$"
print "\tFILE\t-log -close\t/awips2/data_store/wtf/%Y/%m/%d/%Y%m%d%H%M.(seq)"
