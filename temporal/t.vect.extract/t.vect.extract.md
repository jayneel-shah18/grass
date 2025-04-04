## DESCRIPTION

The purpose of **t.vect.extract** is to extract a subset of a space time
vector dataset and to store that subset in a different space time vector
dataset.

## EXAMPLE

In the following example a new space time vector dataset will be create
with all the data later than the year 2000:

```sh
t.vect.extract input=shoreline where="start_time > 2000" \
               output=shoreline_later_2000 basename=new_shoreline

t.info shoreline_later_2000@shoreline type=stvds
 +-------------------- Space Time Vector Dataset -----------------------------+
 |                                                                            |
 +-------------------- Basic information -------------------------------------+
 | Id: ........................ shoreline_later_2000@shoreline
 | Name: ...................... shoreline_later_2000
 | Mapset: .................... shoreline
 | Creator: ................... lucadelu
 | Temporal type: ............. relative
 | Creation time: ............. 2014-11-29 08:43:50.043219
 | Modification time:.......... 2014-11-29 08:43:50.085407
 | Semantic type:.............. mean
 +-------------------- Relative time -----------------------------------------+
 | Start time:................. 2003
 | End time:................... 2009
 | Relative time unit:......... years
 | Granularity:................ 1
 | Temporal type of maps:...... point
 +-------------------- Spatial extent ----------------------------------------+
 | North:...................... 1039175.31479
 | South:...................... 34705.216018
 | East:.. .................... 3052322.44671
 | West:....................... 2130004.16779
 | Top:........................ 0.0
 | Bottom:..................... 0.0
 +-------------------- Metadata information ----------------------------------+
 | Vector register table:...... vector_map_register_8395740fc8de42149fef74a3d25bbb05
 | Number of points ........... 0
 | Number of lines ............ 407
 | Number of boundaries ....... 0
 | Number of centroids ........ 0
 | Number of faces ............ 0
 | Number of kernels .......... 0
 | Number of primitives ....... 407
 | Number of nodes ............ 767
 | Number of areas ............ 0
 | Number of islands .......... 0
 | Number of holes ............ 0
 | Number of volumes .......... 0
 | Number of registered maps:.. 3
 |
 | Title:
 | North Carolina shoreline
 | Description:
 | North Caroline shoreline from 2000 to 2009
 | Command history:
 | # 2014-11-29 08:43:50
 | t.vect.extract input="shoreline"
 |     where="start_time > 2000" output="shoreline_later_2000"
 |     basename="new_shoreline"
 | # 2014-11-29 08:44:14
 | t.support type="stvds"
 |     input="shoreline_later_2000@shoreline"
 |     descr="North Caroline shoreline from 2000 to 2009"
 +----------------------------------------------------------------------------+

t.vect.list shoreline_later_2000
name|layer|mapset|start_time|end_time
shoreline_2003|None|shoreline|2003|None
shoreline_2004|None|shoreline|2004|None
shoreline_2009|None|shoreline|2009|None
```

## SEE ALSO

*[t.create](t.create.md), [t.info](t.info.md)*

## AUTHOR

Sören Gebbert, Thünen Institute of Climate-Smart Agriculture
