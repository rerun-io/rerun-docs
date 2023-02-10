---
title: Logging Data in Python
order: 3
---

<!-- we really need to be able to show the screenshots as miniature on the side, they take sooo much space otherwise -->

In this section we'll build out, log and visualize our first non-trivial dataset, putting many of Rerun's core concepts and features to use.

In a few lines of code, we'll go from a blank sheet to something you don't see everyday: an animated, interactive, DNA-shaped abacus:  
<!-- ![logging data - result](/docs-media/logging_data1_result.png) -->
![logging data - result](/docs-media/logging_data1_resultx.gif)
<!-- TODO: decent screenshot using a mac or better yet: a GIF -->


We will move fast, optimizing for breadth over depth. As we go along, we will give out points to other pages in the reference where you'll be able to explore these ideads in further details.

At any time, you can checkout the complete listing of what we're building[here](https://github.com/rerun-io/rerun/blob/97fc327322fdccbf3fceb30c27c54ab69e5da45f/examples/dna/main.py) to better keep track of the overall picture.

## Prerequisites

We assume you have working Python and `rerun-sdk` installations: checkout the [setup page](python).

## Initializing the SDK

```python
import rerun as rr

rr.init("DNA Abacus")
```

The first thing we want to do is to name the dataset we're working on by setting an [`ApplicationId`]().  
Among other things, a stable [`ApplicationId`]() will make it so the [Rerun Viewer](../reference/viewer/overview) retains its UI state across runs for this specific dataset, which will make our lives much easier as we iterate.

Check out the reference to learn more about how Rerun deals with [applications and sessions](../concepts/apps-and-sessions).

## Starting the Viewer

```python
rr.spawn()
```

Next up, start the [Rerun Viewer](../reference/viewer/overview) itself.

By default, the SDK will start a viewer in another process and automatically pipe the data through.  
There are other means of sending data to a viewer as we'll see at the end of this section, but for now this default will work great as we experiment.

And with that, we're ready to start sending out data:
![logging data - waiting for data](/docs-media/logging_data2_waiting.png)
<!-- TODO: decent screenshot using a mac -->

## Logging our first points

The core structure of our DNA looking shape can easily be described using two point clouds shaped like spirals:
```python
NUM_POINTS = 100

from rerun_demo.data import build_color_spiral
# points and colors are both np.array((NUM_POINTS, 3))
points1, colors1 = build_color_spiral(NUM_POINTS)
points2, colors2 = build_color_spiral(NUM_POINTS, angular_offset=pi)

rr.log_points("dna/structure/left", points1, colors=colors1, radii=0.08)
rr.log_points("dna/structure/right", points2, colors=colors2, radii=0.08)
```

And just like that, we have a scene!

![logging data - first points](/docs-media/logging_data3_first_points.png)
<!-- TODO: decent screenshot using a mac -->

_This is a good time to gain familiarity with the viewer: try interacting with the scene and exploring the different menus._  
_Checkout the [viewer reference](../reference/viewer/overview) for a complete tour._

### Under the hood

This little snippet of code holds much more than meets the eye at first.

The first thing you'll notice is that [points](../reference/data-types/points), [colors](../reference/data-types/colors), and [radii](../reference/data-types/radii) are all native primitives in Rerun.  
In Rerun these primitives are called [Components](../concepts/entity-component) and in fact a [whole bunch of them](../reference/data-types) are supported natively.

Our [Python SDK](https://rerun-io.github.io/rerun/docs/python) was designed with conciseness and integration with the ecosystem in mind, first and foremost.  
In this example, the points and colors returned by [`build_color_spiral`](https://rerun-io.github.io/rerun/docs/python/HEAD/package/rerun_demo/data/#rerun_demo.data.build_color_spiral) are simple `numpy` arrays: the SDK takes care of mapping those to actual Rerun types depending on the logging function we use ([`log_points`]() in this case)!

---

The next thing to notice are these two strings: `"dna/structure/left"` & `"dna/structure/right"`.  
Those are [Entity Paths](../concepts/entity-component), which uniquely identify each Entity in our scene. These are the two ingredients that make up an Entity in Rerun: one or more Components associated with a unique Entity Path.  

It is no coincidence that these identifiers look like traditional filesystem paths: within Rerun, [Entities form a hierarchy](../concepts/entity-path) and that hierarchy plays a major role in how data is visualized and transformed (as we shall soon see).

---

One final observation: notice how we're logging a whole batch of points and colors all at once here!  
[Batches of data](http://localhost:3000/docs/concepts/batches) are first-class citizens in Rerun and come with all sorts of performance improvements and dedicated features.  
You're looking at one of these dedicated features right now: notice how we're only logging a single radius for all these points, yet it applies to all of them!

---

A _lot_ has happened with these two simple function calls.  
Good news is: once you've digested all of the above, logging any other Component won't be any different. In fact, let's log the rest of the scene right now.

## Adding the missing pieces

<!-- TODO: s/body/scaffolding -->

Adding the missing pieces is just more of the same.

We can log the scaffolding as a batch of [3D line segments]():
```python
points = interleave(points1, points2)
rr.log_line_segments("dna/structure/body", points, color=[128, 128, 128])
```

<!-- ![logging data - body](/docs-media/logging_data4_body.png) -->
<!-- TODO: decent screenshot using a mac -->

Which only leaves the beads!
```python
offsets = np.random.rand(NUM_POINTS)
beads = [bounce_lerp(points1[n], points2[n], offsets[n]) for n in range(NUM_POINTS)]
colors = [[int(bounce_lerp(80, 230, offsets[n] * 2))] for n in range(NUM_POINTS)]
rr.log_points("dna/structure/body/beads", beads, radii=0.06, colors=np.repeat(colors, 3, axis=-1))
```

Once again, although we are getting fancier and fancier with our [`numpy` incantations](https://rerun-io.github.io/rerun/docs/python/HEAD/package/rerun_demo/util/#rerun_demo.util.bounce_lerp), there is nothing new here: it's all about building out `numpy` arrays and feeding them to the Rerun API.  
You'll find this holds true for most of our [Component types](../reference/data-types)!

![logging data - beads](/docs-media/logging_data5_beads.png)
<!-- TODO: decent screenshot using a mac -->

## Animating the beads

### Introducing Time

Up until this point, we've completely set aside one of the core primitives of Rerun: [Time and Timelines](../concepts/timelines)!

Even so, if you look at your [Timeline View](../reference/viewer/timeline) right now, you'll notice that Rerun has kept track of time on your behalf anyhow.  
Rerun always keep track of the logging time by default.

![logging data - timeline closeup](/docs-media/logging_data6_timeline.png)
<!-- TODO: decent screenshot using a mac -->

Unfortunately, the logging time isn't particularly helpful to us in this case: we can't have our beads animate depending on the logging time, else they would move at different speeds depending on the performance of the logging process!  
For that, we need to introduce our own custom timeline, using a deterministic clock that we have full control over.

Rerun has rich support for time: whether you want concurrent or disjoint timelines, out-of-order insertions or even data that lives _beyond time_... you'll find a lot of flexibility in there.

Let's add our custom timeline:
```python
time_offsets = np.random.rand(NUM_POINTS)

for i in range(400):
    time = i * 0.01
    rr.set_time_seconds("stable_time", time)

    times = np.repeat(time, NUM_POINTS) + time_offsets
    beads = [bounce_lerp(points1[n], points2[n], times[n]) for n in range(NUM_POINTS)]
    colors = [[int(bounce_lerp(80, 230, times[n] * 2))] for n in range(NUM_POINTS)]
    rr.log_points("dna/structure/body/beads", beads, radii=0.06, colors=np.repeat(colors, 3, axis=-1))
```

That's all it takes: a call to [`set_time_seconds`](https://rerun-io.github.io/rerun/docs/python/HEAD/package/rerun/__init__/#rerun.set_time_seconds) will create our new Timeline and make sure that any logging calls that follow gets assigned that time.

⚠️  If you run this code as is, the result will be.. surprising: the beads are animating as expected, but everything we've logged until that point is gone!  

Enter...

### Latest At semantics

That's because the Rerun Viewer has switched to displaying your custom timeline by default, and all that data from before does not exist there.
Here's a simple fix:
```python
rr.spawn()
rr.set_time_seconds("stable_time", 0)
```

This fix actually introduces yet another very important concept: so-called "latest at" semantics.  
TODO: we've just introduced the semantics of LatestAt

![logging data - stable time](/docs-media/logging_data7_time.png)
<!-- TODO: decent GIF using a mac -->

### Transforming space


```python
    for i in range(400):
        # [...]

        rr.log_rigid3(
            "dna/structure",
            parent_from_child=(
                [0, 0, 0],
                Rotation.from_euler("z", time / 4.0 * tau).as_quat(),
            ),
        )
```

TODO: this need a GIF

### Sending data to any Rerun Viewer

### Saving, sharing and loading data

TODO: --save, standalone viewer, rrd files and their backwards/forwards compat guarantees (..or lack thereof)

### Closing

This closes our whirldwind tour of Rerun. We've barely scratched the surface of what's possible, but this should already give you many pointers to start experimenting (if it didn't, feel free to open an issue!)

TODO: 1 line summary of what we've covered.

To go further, have a look at some of our more [real-world-like examples](./examples).

<!-- point to full example in github at every step -->

### TODO

Quick-start style guide to a few of the basics of logging data.
 - `save()`
 - `connect()`
 - Pointer to the [Data Types Reference](../reference/data-types)
