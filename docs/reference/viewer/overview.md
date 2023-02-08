---
title: Overview
order: 0
---

The following sections give an overview of the basic ui concepts and where to find which functionality.

Generally, the viewer tries to be as self-explaining as possible - most items in the ui show a tooltip upon hovering which should give additional information.
If you are missing a piece of information, don't hesitate to [file an issue](https://github.com/rerun-io/rerun/issues/new/choose)!

Overview
--------------------------

![screenshot of the viewer with different parts annotated](/docs-media/viewer-overview.png)

### [Blueprint](reference/viewer/blueprint.md)
The Blueprint view is where you see and edit the Blueprint for the whole viewer, i.e. what is shown in the viewer (and how it is shown).

### [Selection](reference/viewer/selection.md)
The selection view let's you see details and edit configurations of the current [selection(s)](concepts/selections).

### [Timeline](reference/viewer/timeline.md)
The timeline panel gives you controls over what point in time you're looking at on which [timeline](concepts/timelines) for the rest of the viewer.
Additionally, it gives you an overview of all events on a given timeline.

### [Viewport](reference/viewer/viewport.md)
The viewport is where your visualizations live. It is composed of one or more [Space Views](concepts/spaces) that you can arrange freely.

### Top bar & Menu
The top bar contains operating system controls and generic information.
In the menu you find application wide options and actions.
Use the buttons at the top right corner to hide/show parts of the viewer.

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

![help icon](/docs-media/help-icon.png)

On hover it displays additional information on how to use a view.
