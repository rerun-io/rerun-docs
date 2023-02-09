---
title: Blueprint
order: 1
---

This view shows the [Blueprint](reference/concepts/blueprints.md) for active recording.
Everything visible in the [Viewport](reference/viewer/viewport) has a representation here,
making it an easy way to select a [Space View](concepts/spaces) and the [Entities](concepts/entity-component) it shows.

![blueprint view](/docs-media/blueprint-view.png)

Controls
--------
### Reset
The reset button resets **all** blueprints (including all settings and Space Views) back
to their heuristic-chosen default.

### Add Space View
With this control you can add new Space Views for arbitrary [Spaces](concepts/spaces.md).

Contents
--------
Upon hovering any line in the Blueprint panel, you'll find shorthands for removing and hide/show.
### Data Blueprints
All Entities shown in the blueprint panel refer in fact to their "Data Blueprints".
I.e. the entity plus the associated blueprint settings.
As such, all changes made here are only relevant for the Space View in which they reside.

### Blueprint Groups
Whenever Entities are added to a Space View (either manually or automatically), groupings
are automatically created.
Groups, despite being derived from the [Entity Path](concepts/entity-path.md) are independent of logged data.
They are meant to improve the handling of large Space Views and allow for hierarchical manipulation
of blueprints.

[TODO(#1174)](https://github.com/rerun-io/rerun/issues/1174): Editable & user defined Data Blueprint Groups

Adding Space Views / Entities
-----------------------------
To add an object to the Blueprint, you need to interact with the respective controls:
Space Views are added via the add button at the top of the Blueprint view,
Entities/Data Blueprints via a menu which can be reached through the [Selection view](reference/viewer/selection)
whenever a Space View is selected.
