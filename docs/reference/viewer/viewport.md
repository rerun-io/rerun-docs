---
title: Viewport
order: 4
---

The viewport is a flexible area where you can arrange your Space Views:
You can grab the title of any Space View to doc it to different parts of the viewport or to form tabs.

View controls
-------------
![3d icon](/docs-media/view-controls.png)

Clicking on the title of a Space View has the same effect as selecting it in the [Blueprint view](reference/viewer/blueprint.md)
and will show additional information & settings in the [Selection view](reference/viewer/selection.md) or other means.

For more information on how to navigate a specific Space View, hover its help icon at the top right corner.

The maximize button makes a single Space View fill the entire viewport.
Only one Space view can be maximized at a time.


Kinds of Space Views
--------------------
Rerun distinguishes various kinds of Space Views:
* ![3d icon](/docs-media/spaceview_3d.png) Spatial  
  Generic 2D & 3D data.
* ![tensor icon](/docs-media/spaceview_tensor.png) Tensor  
  Tensor view with support for arbitrary dimensionality.
* ![text icon](/docs-media/spaceview_text.png) Text log  
  Text over time.
* ![scatterplot icon](/docs-media/spaceview_scatterplot.png) Time series plot  
  Scalars over time.
* ![histogram icon](/docs-media/spaceview_histogram.png) Bar chart  
  Bar-chart lots made from 1D tensor data.

Which kind is used is determined upon creation of a Space View.

[TODO(@#1164)](https://github.com/rerun-io/rerun/issues/1164): Allow configuring the category of a space view after its creation 

The kind of Space View determines which Entities it can display, how it displays them and the way they can be interacted with.