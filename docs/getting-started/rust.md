---
title: Rust Quick Start
order: 2
---

## Installing Rerun
The Rerun SDK for Rust requires a working installation of Rust 1.67+.

Everything you need to use Rerun is available via the [rerun](https://crates.io/crates/rerun) crate.

Let's try it out in a brand new Rust project:
```bash
$ cargo init cube && cd cube && cargo add rerun
```

## Logging some data
Add the following code to your `main.rs`
(This example also lives in the `rerun` source tree [example](https://github.com/rerun-io/rerun/tree/latest/examples/rust/minimal/src/main.rs))
```rust
use rerun::demo_util::grid;
use rerun::external::glam;
use rerun::{
    components::{ColorRGBA, Point3D, Radius},
    MsgSender, Session,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut session = Session::new();

    let points = grid(glam::Vec3::splat(-10.0), glam::Vec3::splat(10.0), 10)
        .map(Point3D::from)
        .collect::<Vec<_>>();
    let colors = grid(glam::Vec3::ZERO, glam::Vec3::splat(255.0), 10)
        .map(|v| ColorRGBA::from_rgb(v.x as u8, v.y as u8, v.z as u8))
        .collect::<Vec<_>>();

    MsgSender::new("my_point")
        .with_component(&points)?
        .with_component(&colors)?
        .with_splat(Radius(0.5))?
        .send(&mut session)?;

    session.show()?;

    Ok(())
}
```

Now start your application:
```
cargo run
```

Once everything finishes compiling, you will be greeted with the [Rerun Viewer](../reference/viewer/overview.md):
![intro users - result](/docs-media/intro_users1_result.png)

## Using the viewer
Try out the following to interact with the viewer:
 * Click and drag in the main view to rotate the cube.
 * Zoom in and out with the scroll wheel.
 * Mouse over the "?" icons to find out about more controls.
 * Click on the cube to select all of the points.
 * Hover and select individual points to see more information.

If you're facing any difficulties, don't hesitate to [open an issue](https://github.com/rerun-io/rerun/issues/new/choose) or [join the Discord server](https://discord.gg/PXtCgFBSmH).

## What's next

If you're ready to move on to more advanced topics, check out the [Viewer Walkthrough](viewer-walkthrough.md) or our
more advanced guide for [Logging Data in Rust](logging-rust.md) where we will explore the core concepts that make
Rerun tick and log our first non-trivial dataset.
