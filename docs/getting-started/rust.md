---
title: For Rust Users
order: 4
---

This section will set you up with the Rerun SDK and Viewer.

### Prerequisites

We assume you have a working Rust 1.67+ installation on your system.

### Installing Rerun

Everything you need to use Rerun is available via the [rerun](https://crates.io/crates/rerun) crate.
Let's try it out in a new Rust project:
```bash
$ cargo init cube && cd cube && cargo add rerun
```

That's all there is to it: you can immediately start logging and visualizing data.  
Try running the following [example](https://github.com/rerun-io/rerun/blob/97fc327322fdccbf3fceb30c27c54ab69e5da45f/examples/minimal/src/main.rs)!
```rust
use rerun::demo_util::grid;
use rerun::external::glam;
use rerun::{ColorRGBA, MsgSender, Point3D, Session};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut session = Session::new();

    let points = grid(glam::Vec3::splat(-5.0), glam::Vec3::splat(5.0), 10)
        .map(Point3D::from)
        .collect::<Vec<_>>();
    let colors = grid(glam::Vec3::ZERO, glam::Vec3::splat(255.0), 10)
        .map(|v| ColorRGBA::from_rgb(v.x as u8, v.y as u8, v.z as u8))
        .collect::<Vec<_>>();

    MsgSender::new("my_point")
        .with_component(&points)?
        .with_component(&colors)?
        .send(&mut session)?;

    session.show()?;

    Ok(())
}
```

Once everything is set up properly, you'll be greeted with the [Rerun Viewer]():
![intro users - result](/docs-media/intro_users1_result.png)
<!-- TODO: real screenshot on a mac -->

If you're facing any difficulties, don't hesitate to [open an issue](https://github.com/rerun-io/rerun/issues/new/choose), [ask a question](https://github.com/rerun-io/rerun/discussions) or [join the Discord server](https://discord.com/invite/rerun).

### What's next

This simple scene is a good opportunity to start experimenting with the Viewer: have a look at the [Quick Tour](getting-started/quick-tour) and the [Viewer reference](reference/viewer/overview) for an overview of the features available.

If you're ready to move on to more advanced tasks, checkout our thorough [Getting Started guide](logging-rust) where we will explore the core concepts that make Rerun tick and log our first non-trivial dataset.
