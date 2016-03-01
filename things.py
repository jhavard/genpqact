
models = ['HA', 'HE', 'HH', 'HP', 'HR', 'HT', 'HU', 'HV', 'YA', 'YB', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH',
		'YI', 'YJ', 'YK', 'YO', 'YP', 'YQ', 'YR', 'YS', 'YT', 'YU', 'YV', 'YW', 'YX', 'YY', 'YZ',
		'ZA', 'ZB', 'ZC', 'ZD', 'ZE', 'ZF', 'ZG', 'ZH', 'ZO', 'ZP', 'ZQ', 'ZR', 'ZS', 'ZT', 'ZU',
		'ZV', 'ZW', 'ZX', 'ZY', 'ZZ']

nonmod = ['AB', 'AC', 'AE', 'AG', 'AS', 'AT', 'AU', 'AW', 'AX', 'CD', 'CX', 'FA', 'FE', 'FG', 'FL', 'FM',
		'FN', 'FO', 'FP', 'FR', 'FS', 'FT', 'FW', 'FX', 'FZ', 'IS', 
		'NG', 'NO', 'NT', 'NW', 'NZ', 'OA',
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
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/radar/\\5/%Y%m%d/\\5_\\4_\\2_\\3_\\1_(seq).%Y%m%d%H.radar"
	print ""

# NXUS6[0-9] is the General Status Message
# AFAICT, this is not decoded by AWIPS, but it is stuffed into the fxatext database.  ick!
print "ANY\t^NXUS6. (....) (......) /p(...)(...)"
	print "\tFILE\t-log -close -overwrite\t/awips2/data_store/radar/\\4/%Y%m%d/\\4_\\3_\\1_\\2_(seq).%Y%m%d%H.gsm"
	print ""

for x in satdat:
	# straight WMO
	print "ANY\t^(%s....) (....) (......)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/\\1_\\2_\\3_(seq).%Y%m%d%H"
	print ""
	
	# WMO with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""
	
	# straight PIL
	print "ANY\t^(%s....) (....) (......) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# PIL with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips2/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
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
print "ANY\t^WOUS99 (....) ......"
print "\tFILE\t-log -close -overwrite\t/awips2/data_store/tstmsg/NCF.\\1"
print ""

for x in tstmsg:
	# Usually, these are TSTMSG.  They don't appear to use MONMSG these days.
	# also, PTWC does something a little different.  This is why we save SITE.PIL
	# as it may be important.
	#
	print "ANY\t^%s.... (....) ...... /p(.*)" % x
	print "\tFILE\t-log -close -overwrite\t/awips2/data_store/tstmsg/\\1.\\2"
	print ""

# don't forget the miscellaneous junk... save it but don't feed to EDEX
print "ANY\t^_ELSE_$"
print "\tFILE\t-log -close\t/awips2/data_store/wtf/%Y/%m/%d/%Y%m%d%H%M.(seq)"
