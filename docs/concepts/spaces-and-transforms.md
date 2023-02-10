---
title: Spaces and Transforms
order: 2
---

### The Definition of Spaces

Every Entity in Rerun exists in some *Space.* This is at the core of how Rerun organizes the visualizations of the data
that you have logged.  In the [Rerun Viewer](../reference/viewer.md) you view data by configuring a "Space View," which is a view
of a set of entities *as seen from a particular Space.*

A "Space" is, very loosely, a generalization of the idea of a "Coordinate System" to arbitrary data. If a collection of
entities are part of the same Space, it means they can be rendered together in the same view, using the same
"coordinates." As some examples:
- For 2d and 3d geometric primitives this means they share the same origin and coordinate system.
- For scalar plots it means they share the same plot axes.
- For text logs, it means they share the same conceptual stream.

Which entities belong to which Spaces is a function of the Transform system, which uses the following rules to define
the connectivity of Spaces:

1.  Every unique Entity Path defines a potentially unique space.
1.  Unless otherwise specified, every path is trivially connected to its parent by the Identity transform.
1.  Logging a transform to a path defines the relationship between that path and its parent (replacing the Identity
    connection).
1.  Only paths which are connected by the Identity transform are effectively considered to be part of the same
    Space. All others are considered to be disjoint.

Note that in the absence of transforms, all entity paths are fully connected by the Identity transform, and therefore
share the same Space. However, as soon as you begin to log transforms, you can end up with additional spaces.

Consider the following scenario:

```python
rr.log_points("world/mapped_keypoints", ...)
rr.log_points("world/robot/observed_features", ...)
rr.log_rigid3("world/robot", ...)
```

There are 4 parent/child entity relationships represented in this hierarchy.

- `(root)` -> `world`
- `world` -> `world/mapped_keypoints`
- `world` -> `world/robot`
- `world/robot` -> `world/robot/observed_features`

The call: `rr.log_rigid3("world/robot", ...)` only applies to the relationship: `world` -> `world/robot` because the
logged transform (`world/robot`) describes the relationship between the entity and its _parent_ (`world`). All of the
other relationships are considered to be an identity transform.

This leaves us with two spaces. In one space, we have the entities `world`, and `world/mapped_keypoints`. In the other
space we have the entities `world/robot` and `world/robot/observed_features`.

Practically speaking, this means that the position values of the points from `world/mapped_keypoints` and the points
from `world/robot/observed_features` are not directly comparable. If you were to directly draw these points in a single
coordinate system the results would be meaningless. Fortunately, Rerun can still put these entities in the same Space View because it is able to automatically transform data between different spaces.

### Space Transformations

In order to correctly display data from different Spaces in the same view, Rerun uses the information from logged
transforms. Since most transforms are invertible, Rerun can usually transform data from a parent space to a child space
or vice versa.  As long as there is a continuous chain of well defined transforms, Rerun will apply the correct series
of transformations to the component data when building the scene. 

Rerun transforms are currently limited to connections between _Spatial_ views of 2D or 3D data. There are 3 types of
transforms that can be logged:

- Rigid3D transforms define a pure 3D translation + rotation relationship between two paths.
  [rerun.log_rigid3](https://rerun-io.github.io/rerun/docs/python/HEAD/common/transforms/#rerun.log_rigid3))
- Pinhole transforms define a 3D -> 2D camera projection. (See:
  [rerun.log_pinhole](https://rerun-io.github.io/rerun/docs/python/HEAD/common/transforms/#rerun.log_pinhole))
- Unknown transforms specify that the data cannot be transformed. In this case it will not be possible to combine the
  data into a single view and you will need to create two separate views to explore the data. (See:
  [rerun.log_unknown_transform](https://rerun-io.github.io/rerun/docs/python/HEAD/common/transforms/#rerun.log_unknown_transform))

In the future, Rerun will be adding support for additional types of transforms.
 - [#349: Log 2D -> 2D transformations in the transform hierarchy](https://github.com/rerun-io/rerun/issues/349)
