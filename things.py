
models = ['HA', 'HE', 'HH', 'HP', 'HR', 'HT', 'HU', 'HV', 'YA', 'YB', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH',
		'YI', 'YJ', 'YK', 'YO', 'YP', 'YQ', 'YR', 'YS', 'YT', 'YU', 'YV', 'YW', 'YX', 'YY', 'YZ',
		'ZA', 'ZB', 'ZC', 'ZD', 'ZE', 'ZF', 'ZG', 'ZH', 'ZO', 'ZP', 'ZQ', 'ZR', 'ZS', 'ZT', 'ZU',
		'ZV', 'ZW', 'ZX', 'ZY', 'ZZ']

nonmod = ['AB', 'AC', 'AE', 'AG', 'AS', 'AT', 'AU', 'AW', 'AX', 'CD', 'CX', 'FA', 'FE', 'FG', 'FL', 'FM',
		'FN', 'FO', 'FP', 'FR', 'FS', 'FT', 'FW', 'FX', 'FZ', 'IS', 
		'NG', 'NO', 'NT', 'NW', 'NX', 'NZ', 'OA',
		'OB', 'OC', 'OJ', 'OK', 'OM', 'ON', 'OP', 'OY', 'PE', 'PG', 'PH', 'PJ', 'PM', 'PP', 'PR',
		'PS', 'PT', 'PW', 'PX', 'PY', 'RX', 'SH', 'SO', 'SR', 'SX', 'TX', 'UB', 'UD', 'XX',
		'UE', 'UF', 'UG', 'UH', 'UK', 'UL', 'UM', 'UP', 'UQ', 'US', 'UX', 'WA', 'WG', 'WH', 
		'WS', 'WU', 'WW']

radars = ['SD']

tstmsg = ['NT']

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
	print "\tFILE\t-log -close -edex -overwrite\t/awips/data_store/radar/\\4/%Y%m%d/\\4_\\5_\\2_\\3_\\1_(seq).%Y%m%d%H.radar"
	print ""

for x in satdat:
	# straight WMO
	print "ANY\t^(%s....) (....) (......)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips/data_store/satdat/%Y%m%d/\\1_\\2_\\3_(seq).%Y%m%d%H"
	print ""
	
	# WMO with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..)$" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""
	
	# straight PIL
	print "ANY\t^(%s....) (....) (......) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_(seq).%Y%m%d%H"
	print ""

	# PIL with BBB
	print "ANY\t^(%s....) (....) (......) ([A-Z0-9]..) /p(.*)" % x
	print "\tFILE\t-log -close -edex -overwrite\t/awips/data_store/satdat/%Y%m%d/\\1_\\2_\\3_\\4_\\5_(seq).%Y%m%d%H"
	print ""
	

#print "NEED SPECIAL HANDLING FOR WO"


