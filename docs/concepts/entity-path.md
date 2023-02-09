---
title: The Entity Path Hierarchy
order: 1
---

As mentioned in the [Entity Component](entity-component.md) overview, all Entities within Rerun have a unique Entity
Path.

Rerun treats these paths as being arranged in a hierarchy with the "/" character acting as a separator between path
elements. The conventional path semantics including concepts of "root" and "parent" / "child" generally apply.

When writing paths in logging APIs the leading "/" is omitted.

Note that there is no path-level distinction between "file-like" and "directory-like" concepts. Any path may be an
entity, and entities may be direct children of other entities. For example:
```
rr.log_image("image", img)
rr.log_points("image/points", points)
```

However, it is also acceptable to leave implicitly "empty" elements in your paths as well.
```
rr.log_image("camera/image", img)
rr.log_points("camera/image/detections/points", points)
```
Nothing needs to be explicitly logged to `"camera"` or `"camera/image/detection"` to make the above valid.

### Path Hierarchy Functions
Path hierarchy plays an important role in a number of different functions within Rerun:

 * With the [Transform System](spaces-and-tranforms.md) the `transform` component logged to any Entity always describes
the relationship between that Entity and its direct parent.
 * When resolving the meaning of `class_id` and `keypoint_id` components, Rerun uses the [Annotation Context](annotations.md) from the nearest ancestor in the hierarchy.
 * When adding data to [Blueprints](blueprints.md), it is common to add a path and all of its descendants.
 * When using the `log_cleared` API, it is possible to mark an entity and all of its descendants as being cleared.
 * In the future, it will also be possible to use path-hierarchy to set default-values for descendants.
   [#1158](https://github.com/rerun-io/rerun/issues/1158)

