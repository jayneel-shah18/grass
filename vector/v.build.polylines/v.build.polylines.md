## DESCRIPTION

*v.build.polylines* builds polylines from the lines or boundaries in a
vector map.

A line is defined by one start node, one end node and any number of
vertices between the start and end nodes. The shortest possible line
consists of only two vertices where the coordinates of the start and end
nodes are identical to those of the two vertices.

*v.build.polylines* picks a line and from its start node, walks back as
long as exactly one other line of the same type is connected to this
node. Line directions are reversed as required, i.e. it does not matter
if the next line is connected to the current node by its start or end
node. Once the start line of a polyline is identified, it walks forward
and adds all vertices (in reverse order if needed) of connected lines to
the start line, i.e. the start line and connecting lines are reversed as
needed. That is, if a line is reversed depends on what node is initially
picked for building polylines. If the direction of lines is important
(it's not for boundaries to build areas), you have to manually change
line directions with either *[v.edit](v.edit.md)* or the *[wxGUI vector
digitizer](wxGUI.vdigit.md)*.

Polylines provide the most appropriate representation of curved lines
when it is important that nodes serve to define topology rather than
geometry. Curved lines are usually digitized as polylines, but these are
sometimes broken into their constituent straight line segments during
conversion from one data format to another. *v.build.polylines* can be
used to rebuild such broken polylines.

## NOTES

*v.build.polylines* combines only lines of the same type to a new
polyline, i.e. lines and boundaries are kept separate.

Category number(s) are assigned to a polyline based on **cats**
parameter.

- **cats=no** - No category number is assigned to a polyline. Also
  attributes tables linked to the input vector map are not copied to the
  output vector map.
- **cats=first** - Assign to a polyline category number of the first
  line. All linked attributes tables are copied to the output vector map
  without filtering, but the categories are processed according to the
  cats option.
- **cats=multi** - If the lines that make up a polyline have different
  category numbers then *v.build.polylines* will set the multiple
  category numbers to a polyline. Also all linked attributes tables are
  copied to the output vector map.
- **cats=same** - Assigned lines to a polyline have same category
  numbers in all layers. Linked attributes tables are copied to the
  output vector map.

*v.build.polylines* correctly handles **input** vector maps containing
lines, boundaries, centroids and points. Lines and boundaries will be
converted to polylines. Areas are guaranteed to be preserved.

## ACKNOWLEDGEMENTS

This program was originally written during Mark Lake's tenure of a
Leverhulme Special Research Fellowship at University College London.

## SEE ALSO

*[v.build](v.build.md), [v.in.ascii](v.in.ascii.md),
[v.edit](v.edit.md), [v.split](v.split.md)*

## AUTHORS

Mark Lake, Institute of Archaeology, University College London.  
Major rewrite by Radim Blazek, October 2002  
Category mode added by Martin Landa, FBK-irst, Trento, Italy, October
2007  
Support for categories, attributes, and different line types by Markus
Metz
