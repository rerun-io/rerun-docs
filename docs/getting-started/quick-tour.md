---
title: Quick Tour
order: 1
---

This guide is intended to familiarize you with the basics of Rerun using an example dataset. By the end you should be
comfortable launching the viewer and using it to inspect data.

The demo uses the output of the [COLMAP](https://colmap.github.io/) structure-from-motion pipeline on a small
dataset. If you are not familiar with structure from motion, this is a 3D reconstruction of a scene. The data
includes 3D points in space, the source images used for the reconstruction, and information about the relationship between them.

![Preview](/docs-media/quickstart0_preview.png)

The guide is broken up into the following sections:
 * [Installing the Rerun SDK](#installing-the-rerun-sdk)
 * [Launching the Demo](#launching-the-demo)
 * [Overview of the Panels](#overview-of-the-panels)
 * [Exploring Data](#exploring-data)
 * Navigating the Timeline
 * Configuring Views
 * Creating Views

To learn more about logging data with the Rerun SDK see the [Python](logging-python.md) or [Rust](logging-rust.md) getting started guides.

## Installing the Rerun SDK
Although the Rerun SDK is available in both Python and Rust, this quick-start uses the Python installation process. Even
if you plan to use Rerun with Rust, we still recommend having a Rerun python environment available for experimentation
and previewing our our [library of examples](examples.md).

To get started you will need to have [Python-3.8](https://www.python.org/) or greater installed on your system.
We also suggest the use of python [virtual environments](https://docs.python.org/3/tutorial/venv.html) or the
equivalent, such as conda, for managing your installed packages. 

Once your environment is setup, the Rerun SDK can be installed from pypi via the
[`rerun-sdk`](https://pypi.org/project/rerun-sdk/) package.

```bash
$ pip install rerun-sdk
```

The output will hopefully end in a line like:
```bash
Successfully installed numpy-1.24.2 pyarrow-10.0.1 rerun-sdk-0.1.0
```
in which case you're ready to get started.

If this installation doesn't work in your environment, please file an [issue](https://github.com/rerun-io/rerun/issues)
providing details about your environment and the output of the pip command.

## Launching the Demo
The rerun-sdk actually includes two python packages:
- `rerun` is the core rerun library, which you'll learn about in the other guides.
- `rerun_demo` contains assorted helper data to make it easy to test many of the Rerun APIs.

To start the demo, simply run:
```bash
$ python -m rerun_demo
```

*Note: If this is your first time launching rerun you will likely see a notification about the Rerun
anonymous usage data policy. Rerun collects anonymous usage data to help improve the SDK, though you
may choose to opt out if you would like.*

You should see an output along the lines of:
```
2023-02-13T05:16:06.835424Z  INFO rerun::run: Loading "/home/jleibs/venv/lib/python3.10/site-packages/rerun_sdk/rerun_demo/demo.rrd"…
```

A window like the follow should pop up.  

![First Launch](/docs-media/quickstart1_first_launch.png)

Depending on your display size, the panels may have a different arrangements.
You'll note this doesn't yet look like the initial preview. The rest of this guide will walk you through how to
configure the Viewer to meet your needs.
# Overview of the Panels

There are 4 main parts to this window:
- In the middle of the screen is the [Viewport](../reference/viewer/viewport.md). This is where you see your data.
- On the left is the [Blueprint](../reference/viewer/blueprint.md) panel. This is where you configure the different
  views.
- On the right is the [Selection](../reference/viewer/selection.md) panel. This is where you see extra information
  and configuration information for things that you have selected.
- On the bottom is the [Timeline](../reference/viewer/timeline.md) panel. This is where you can control the current
  point in time that is being viewed.

You'll notice that the each of the 3 side panels has a corresponding button in the upper right corner. Try clicking each of these these to hide and show the corresponding panel.

![Toggle Panel](/docs-media/quickstart2_toggle_panel.png)

For now, leave the panels visible.

## Exploring Data

## TODO(jleibs)... keep writing

1. pip install & run first example
2. Click around, hover over some explanations, navigate around the interface
    - Try the main features indicated by the “getting started guide”:
        1. Change timeline
        2. Minimize/maximize blueprint/streams/selection views
        3. Hover over data
        4. Add/remove view / data blueprint
        5. Toggle view/data visibility
        6. Use play controls: play/pause/step/loop 
        7. Make a time range selection
        8. Navigate data in the streams view
3. Checkout repository with copy of first example without any rerun logs
    1. Tutorial going through and adding back logs to make it look the same
4. Try running some other examples
