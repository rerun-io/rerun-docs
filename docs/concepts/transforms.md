---
title: Spaces and Transforms
order: 2
---

Within Rerun, the ideas of "Spaces" and "Transforms" are interconnected.

### The Definition of Spaces

A "Space" is, very loosely, a generalization of the idea of a "Coordinate System" to the arbitrary data
that can be logged to Rerun. It's easiest to describe a Space by its relationship with the Entities it contains.

If a collection of entities are part of the same Space, it means they can be rendered together in the same view, using
the same coordinates. As some examples:
 - For 2d and 3d geometric primitives this means they share the same origin and coordinate system.
 - For scalar plots it means they share the same plot axes.
 - For text logs, it means they share the same conceptual stream.

Which entities belong to which Spaces is a function of the Transform system, which uses the following rules to define
the connectivity of Spaces:
 1. Every unique Entity Path defines a potentially unique space.
 1. Unless otherwise specified, every path is trivially connected to its parent by the Identity transform.
 1. Logging a transform to a path defines the relationship between that path and its parent (replacing the Identity
    connection).
 1. Only paths which are connected by the Identity transform are effectively considered to be part of the same
    Space. All others are considered to be disjoint.

Consider the following scenario:
``` python
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
logged transform (`world/robot`) describes the relationship between the entity and its *parent* (`world`). All of the
other relationships are considered to be an identity transform.

This leaves us with two spaces. In one space, we have the entities `world`, and `world/mapped_keypoints`.  In the other
space we have the entities `world/robot` and `world/robot/observed_features`.

This means that the points from `world/mapped_keypoints` and the points from `world/robot/observed_features` cannot be
natively placed into the same view.

### Space Projections

However, just because two entities are in different Spaces doesn't mean you can't still display them in the same view.

In many cases, Rerun is able to use the information from the logged transforms to *reproject* entities from one Space
into another. As long as there is a continuous chain of well defined transforms, you can create a view containing
entities from multiple disjoint spaces, and the data will be transformed for you when drawing the scene.

Rerun transforms are currently limited to connections between *Spatial* views of 2D or 3D data. There are 3 types of
transforms that can be logged:
 - Rigid3D transforms define a pure 3D translation + rotation relationship between two paths. Rigid3D transforms are
   invertible and allow bidirectional projection between 3D Spaces. (See:
   [rerun.log_rigid3](https://rerun-io.github.io/rerun/docs/python/HEAD/common/transforms/#rerun.log_rigid3))
 - Pinhole transforms define a 3D -> 2D camera projection. As the Pinhole camera projection is non-invertible, these
   transforms only allow projections in one direction. (See:
   [rerun.log_pinhole](https://rerun-io.github.io/rerun/docs/python/HEAD/common/transforms/#rerun.log_pinhole))

In the future, Rerun will be adding support for additional types of transforms.
