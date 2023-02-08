---
title: Entities and Components
order: 0
---

At the core of Rerun's data model is an Entity Component System (ECS)]. In short, an ECS is a composition-oriented
framework in which: Entities represent generic objects, Components describe data associated with those Entities, and Systems operate on the Entities based on the Components they possess.

Concretely within Rerun:
 - The things that you log are *Entities*. For examples, points, rects, or images.
 - The data that describes these things are *Components.* For example, their positions, colors, or pixel data.
 - The renderers that draw those things are *Systems*. For example, the Point Renderer or the Image Render.

It is important to note that an Entity is nothing more than an identity. In Rerun we refer to entities using a path
(called an Entity Path).  When you log a piece of data, all that you are doing is setting the values of some *Component*
associated with that Entity Path. The Entity is nothing more than the collection of Components that share the same
Entity Path.

For example, consider the function to log a single point:
```python
rr.log_point("world/points", point=[32.7, 45.9], color=[255, 0, 0])
```
Behind the scenes, this function is simply recording data for two components: `point2d`, and `colorrgba`, each
associated with the Entity Path `world/points`.

In the viewer, the 2D Point Renderer later queries the data store for all of the entities that have a `point2d`
component, and uses the data from the associated components to render the points.

The assorted logging APIs and their corresponding renderers all simply set different combinations of components on some
specified entity. For more information on the different components and how they relate to the available datatypes see
the [Data Types reference](../reference/data-types.md)