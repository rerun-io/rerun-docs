---
title: The Library
order: 0
---

[TODO(#1049)](https://github.com/rerun-io/rerun/issues/1049)

- Open-source / github link
- Rust-core:
 - High-level overview of how crates are organized
- Some details on Python bindings via PyO3
- Dependencies of notable significance:
 - egui
 - wgpu
 - arrow

## Controlling logging globally

Rerun logging is enabled by default. The logging behavior can be overridden at runtime using the `RERUN` environment variable:

```sh
export RERUN=off
python my_rerun_enabled_script.py
# or
cargo run my_rerun_package
```

The `RERUN` environment variable is read once during SDK initialization. The accepted values for `RERUN` are `1/on/true`, and `0/off/false`.

ℹ️ Note: When Rerun is disabled, logging statements are bypassed and essentially become no-ops.

### Creating a default-off setup in code

The "default-on" behavior can also be changed to a "default-off" behavior:

code-example: default-off-session

### Dynamically controlling on/off

See the [is_enabled()](https://docs.rs/re_sdk/latest/re_sdk/struct.Session.html#method.is_enabled) and [set_enabled()](https://docs.rs/re_sdk/latest/re_sdk/struct.Session.html#method.set_enabled) methods for Rust on `rerun::Session`.

See the [`is_enabled()`](https://rerun-io.github.io/rerun/docs/python/HEAD/package/rerun/__init__/#rerun.is_enabled) and [`set_enabled()`](https://rerun-io.github.io/rerun/docs/python/HEAD/package/rerun/__init__/#rerun.set_enabled) methods for Python.