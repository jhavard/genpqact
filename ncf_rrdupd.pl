#!/usr/bin/perl

use Data::Dumper;
use RRDs;
use Date::Parse;

use POSIX qw(strftime);

$BASE='/export/stats';
$SATF="$BASE/ncf.rrd";

$TIMESPAN="26h";

$DAY = $ARGV[0];
$HOUR = $ARGV[1];
$MIN  = $ARGV[2];

$now_string = strftime "%Y-%m-%dT$HOUR:$MIN:00", gmtime;

$ideal = str2time($now_string, "GMT");

($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,$atime,$mtime,$ctime,$blksize,$blocks)=stat("/awips2/data_store/tstmsg/NCF.KNCF");

$diff = $mtime - $ideal;

RRDs::update($SATF, "N:$diff");

sub do_graph {
	$file = "$BASE/graphs/" . $_[0];
	$key = $_[1];
	$color = $_[2];
	$comment = $_[3];
	$unit = $_[4];
	RRDs::graph $file, "--start", "end-$TIMESPAN", "--end", "now", "--height", "240", "--width", "879", "-W", "HEATER Labs / WXLAB $now_string", "-E", 
		"DEF:xa=$SATF:${key}:AVERAGE", 
		"DEF:xl=$SATF:${key}:MIN",
		"DEF:xh=$SATF:${key}:MAX",
		"DEF:xn=$SATF:${key}:LAST",
		"LINE1:xa#${color}:${comment}",
		"GPRINT:xn:LAST:Current %5.2lf %s$unit", "GPRINT:xh:MAX:Max %5.2lf %s$unit", "GPRINT:xa:AVERAGE:Avg %5.2lf %s$unit", "GPRINT:xl:MIN:Min %5.2lf %s$unit";
}	

do_graph "day_ncf.png", "delay", "FF0000", "NCF Delay", "s";
