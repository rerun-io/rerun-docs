---
title: Overview
order: 0
---

Overview
--------------------------

![screenshot of the viewer with different parts annotated](/docs-media/viewer-concept.png)

### Top bar & Menu
The top bar contains operating system controls and generic information.
In the menu you find application wide options and actions.

With the buttons at the top right corner you can hide/show the Blueprint/Selection/Streams panels respectively.

### Blueprint
The Blueprint view is where you see and edit the [Blueprint](reference/blueprint-cfg) for the whole viewer, i.e. what is shown in the viewer (and how it is shown).
It’s also an easy way to select a [Space View](concepts/spaces) and the [Entities](concepts/entity-component) it shows.

### Selection
The selection view let's you see details and edit configurations of the current [selection(s)](concepts/selections).

TODO:
* Context of selections etc..
* Selection History


### Timeline

The timeline panel gives you controls over what point in time you're looking at on which [timeline](concepts/timelines) for the rest of the viewer.
Additionally, it gives you an overview of all events on a given timeline. Learn more about the timeline panel [here](reference/viewer/timeline)

### Viewport
The viewport is where your visualizations live. It is composed of one or more [Space Views](concepts/spaces) that you can arrange freely.


Command Palette
----------------------------
The command palette is a powerful tool to reach arbitrary actions from anywhere via a simple text search.
You reach it with `Cmd/Ctrl + P` or via the menu.
![screenshot of the command palette](/docs-media/command-palette.png)
Once it's open just start typing to filter and press `Enter` to execute the selected action or cancel with `Esc`.

[TODO(#1132)](https://github.com/rerun-io/rerun/issues/1132): The command palette is too limited right now.


Help icons
----------
Most views have an info icon at the top right corner.

TODO: Image

On hover it displays additional information on how to use a view.
