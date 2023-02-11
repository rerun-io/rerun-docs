---
title: For Python Users
order: 2
---

### Prerequisites

We assume you have a working Python 3.8+ installation on your system.

### Installing Rerun

Everything you need to use Rerun is available via the [rerun-sdk](https://pypi.org/project/rerun-sdk/) pip package:
```bash
$ pip install rerun-sdk
```

<!-- TODO: make sure that commit hash is up-to-date before final PR -->
That's all! You can now immediately start logging and visualizing data.  
Try running the following [example](https://github.com/rerun-io/rerun/blob/97fc327322fdccbf3fceb30c27c54ab69e5da45f/examples/minimal/main.py):
```python
import rerun as rr  # NOTE: `rerun`, not `rerun-sdk`!
import numpy as np

SIZE = 10

rr.spawn()

x, y, z = np.meshgrid(np.linspace(-5, 5, SIZE), np.linspace(-5, 5, SIZE), np.linspace(-5, 5, SIZE))
positions = np.array(list(zip(x.reshape(-1), y.reshape(-1), z.reshape(-1))))

r, g, b = np.meshgrid(np.linspace(0, 255, SIZE), np.linspace(0, 255, SIZE), np.linspace(0, 255, SIZE))
colors = np.array(list(zip(r.reshape(-1), g.reshape(-1), b.reshape(-1))), dtype=np.uint8)

rr.log_points("my_points", positions=positions, colors=colors)
```
<!-- TODO: s/my_points/cube_cloud -->

Once everything properly is set up, you'll be greeted with the [Rerun Viewer](../reference/viewer/overview.md):
![intro users - result](/docs-media/intro_users1_result.png)

If you're facing any difficulties, don't hesitate to [open an issue](https://github.com/rerun-io/rerun/issues/new/choose), [ask a question](https://github.com/rerun-io/rerun/discussions) or [join the Discord server](https://discord.com/invite/rerun).

### What's next

This simple scene is a good opportunity to start experimenting with the Viewer: have a look at the [Quick Tour](getting-started/quick-tour) and the [Viewer reference](reference/viewer/overview) for an overview of the features available.

If you're ready to move on to more advanced topics, checkout our thorough [Getting Started guide](logging-python) where we will explore the core concepts that make Rerun tick and log our first non-trivial dataset.
