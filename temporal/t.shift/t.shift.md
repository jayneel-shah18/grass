## DESCRIPTION

*t.shift* is designed to temporally shift all registered maps in a space
time dataset with a user defined granularity. Raster, 3D raster and
vector space time datasets are supported.

The format of the absolute time granularity is "number unit". Number is
an integer, unit is the temporal unit that can be one of year(s),
month(s), week(s), day(s), hour(s), minute(s) or second(s).

The granularity in case of relative time is an integer. The temporal
unit is the unit of the space time dataset and can not be modified.

## NOTES

Be careful when shifting space time datasets with absolute time. The
temporal granularity may change if you shift a space time dataset with a
unit that is different from the space time dataset granularity. Be aware
that the shifting with months and years may result in incorrect days per
month. Shifting the date 20012-03-31 with a granularity of one month
will result in 2012-04-31 which is incorrect. In this case an error will
raise and the shifting will not performed for the whole dataset.

You can use the extraction module to shift only a subset of maps from a
space time dataset. Be aware that the shifting of maps affect all space
time datasets in which they are registered.

## EXAMPLE

We create 6 raster maps and register them in a space time raster dataset
using an increment of one day. Then we shift the time intervals with a
granularity of 12 hours.

```sh
r.mapcalc expression="prec_1 = rand(0, 550)" -s
r.mapcalc expression="prec_2 = rand(0, 450)" -s
r.mapcalc expression="prec_3 = rand(0, 320)" -s
r.mapcalc expression="prec_4 = rand(0, 510)" -s
r.mapcalc expression="prec_5 = rand(0, 300)" -s
r.mapcalc expression="prec_6 = rand(0, 650)" -s

t.create type=strds temporaltype=absolute \
         output=precipitation_daily \
         title="Daily precipitation" \
         description="Test dataset with daily precipitation"

t.register -i type=raster input=precipitation_daily \
           maps=prec_1,prec_2,prec_3,prec_4,prec_5,prec_6 \
           start=2012-01-01 increment="1 day"

t.info type=strds input=precipitation_daily

 +-------------------- Space Time Raster Dataset -----------------------------+
 |                                                                            |
 +-------------------- Basic information -------------------------------------+
 | Id: ........................ precipitation_daily@PERMANENT
 | Name: ...................... precipitation_daily
 | Mapset: .................... PERMANENT
 | Creator: ................... soeren
 | Temporal type: ............. absolute
 | Creation time: ............. 2014-11-23 19:20:26.004855
 | Modification time:.......... 2014-11-23 19:20:26.471536
 | Semantic type:.............. mean
 +-------------------- Absolute time -----------------------------------------+
 | Start time:................. 2012-01-01 00:00:00
 | End time:................... 2012-01-07 00:00:00
 | Granularity:................ 1 day
 | Temporal type of maps:...... interval
 +-------------------- Spatial extent ----------------------------------------+
 | North:...................... 80.0
 | South:...................... 0.0
 | East:.. .................... 120.0
 | West:....................... 0.0
 | Top:........................ 0.0
 | Bottom:..................... 0.0
 +-------------------- Metadata information ----------------------------------+
 | Raster register table:...... raster_map_register_882043e9afaa4e60b845aceb1a1fee2c
 | North-South resolution min:. 10.0
 | North-South resolution max:. 10.0
 | East-west resolution min:... 10.0
 | East-west resolution max:... 10.0
 | Minimum value min:.......... 0.0
 | Minimum value max:.......... 16.0
 | Maximum value min:.......... 297.0
 | Maximum value max:.......... 647.0
 | Aggregation type:........... None
 | Number of registered maps:.. 6
 |
 | Title:
 | Daily precipitation
 | Description:
 | Test dataset with daily precipitation
 | Command history:
 | # 2014-11-23 19:20:26
 | t.create type="strds" temporaltype="absolute"
 |     output="precipitation_daily" title="Daily precipitation"
 |     description="Test dataset with daily precipitation"
 | # 2014-11-23 19:20:26
 | t.register -i type="rast" input="precipitation_daily"
 |     maps="prec_1,prec_2,prec_3,prec_4,prec_5,prec_6" start="2012-01-01"
 |     increment="1 day"
 |
 +----------------------------------------------------------------------------+

t.rast.list input=precipitation_daily

name|mapset|start_time|end_time
prec_1|PERMANENT|2012-01-01 00:00:00|2012-01-02 00:00:00
prec_2|PERMANENT|2012-01-02 00:00:00|2012-01-03 00:00:00
prec_3|PERMANENT|2012-01-03 00:00:00|2012-01-04 00:00:00
prec_4|PERMANENT|2012-01-04 00:00:00|2012-01-05 00:00:00
prec_5|PERMANENT|2012-01-05 00:00:00|2012-01-06 00:00:00
prec_6|PERMANENT|2012-01-06 00:00:00|2012-01-07 00:00:00


t.shift type=strds input=precipitation_daily granularity="12 hours"

t.info type=strds input=precipitation_daily

 +-------------------- Space Time Raster Dataset -----------------------------+
 |                                                                            |
 +-------------------- Basic information -------------------------------------+
 | Id: ........................ precipitation_daily@PERMANENT
 | Name: ...................... precipitation_daily
 | Mapset: .................... PERMANENT
 | Creator: ................... soeren
 | Temporal type: ............. absolute
 | Creation time: ............. 2014-11-23 19:20:26.004855
 | Modification time:.......... 2014-11-23 19:21:08.240018
 | Semantic type:.............. mean
 +-------------------- Absolute time -----------------------------------------+
 | Start time:................. 2012-01-01 12:00:00
 | End time:................... 2012-01-07 12:00:00
 | Granularity:................ 24 hours
 | Temporal type of maps:...... interval
 +-------------------- Spatial extent ----------------------------------------+
 | North:...................... 80.0
 | South:...................... 0.0
 | East:.. .................... 120.0
 | West:....................... 0.0
 | Top:........................ 0.0
 | Bottom:..................... 0.0
 +-------------------- Metadata information ----------------------------------+
 | Raster register table:...... raster_map_register_882043e9afaa4e60b845aceb1a1fee2c
 | North-South resolution min:. 10.0
 | North-South resolution max:. 10.0
 | East-west resolution min:... 10.0
 | East-west resolution max:... 10.0
 | Minimum value min:.......... 0.0
 | Minimum value max:.......... 16.0
 | Maximum value min:.......... 297.0
 | Maximum value max:.......... 647.0
 | Aggregation type:........... None
 | Number of registered maps:.. 6
 |
 | Title:
 | Daily precipitation
 | Description:
 | Test dataset with daily precipitation
 | Command history:
 | # 2014-11-23 19:20:26
 | t.create type="strds" temporaltype="absolute"
 |     output="precipitation_daily" title="Daily precipitation"
 |     description="Test dataset with daily precipitation"
 | # 2014-11-23 19:20:26
 | t.register -i type="rast" input="precipitation_daily"
 |     maps="prec_1,prec_2,prec_3,prec_4,prec_5,prec_6" start="2012-01-01"
 |     increment="1 day"
 | # 2014-11-23 19:21:08
 | t.shift type="strds" input="precipitation_daily"
 |     granularity="12 hours"
 |
 +----------------------------------------------------------------------------+


t.rast.list input=precipitation_daily

name|mapset|start_time|end_time
prec_1|PERMANENT|2012-01-01 12:00:00|2012-01-02 12:00:00
prec_2|PERMANENT|2012-01-02 12:00:00|2012-01-03 12:00:00
prec_3|PERMANENT|2012-01-03 12:00:00|2012-01-04 12:00:00
prec_4|PERMANENT|2012-01-04 12:00:00|2012-01-05 12:00:00
prec_5|PERMANENT|2012-01-05 12:00:00|2012-01-06 12:00:00
prec_6|PERMANENT|2012-01-06 12:00:00|2012-01-07 12:00:00
```

## SEE ALSO

*[t.create](t.create.md), [t.register](t.register.md),
[t.snap](t.snap.md)*

## AUTHOR

Sören Gebbert, Thünen Institute of Climate-Smart Agriculture
