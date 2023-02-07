---
title: The Viewer
order: 1
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

### Timeline controls
The timeline controls allows you to control the playback and what [timeline](concepts/timelines) is active.

### Streams
The streams on the active timeline are shown in the streams view. Each circle shown is a new timepoint for the respective [entity/component](concepts/entity-component).

### Viewport
The viewport is where your visualizations live. It is composed of one or more [Space Views](concepts/spaces) that you can arrange freely.


Command Palette
----------------------------
The command palette is a powerful tool to reach arbitrary actions from anywhere via a simple text search.
You reach it with `Cmd/Ctrl + P` or via the menu.
![screenshot of the command palette](/docs-media/command-palette.png)
Once it's open just start typing to filter and press `Enter` to execute the selected action or cancel with `Esc`.

[TODO(#1132)](https://github.com/rerun-io/rerun/issues/1132): The command palette is too limited right now.


View specific navigation
----------------------------
Most views have an info icon at the top right corner. On hover it displays additional information on how to use a view.
