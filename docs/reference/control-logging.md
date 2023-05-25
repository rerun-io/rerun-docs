---
title: Control Logging
order: 0
---

## Controlling logging globally

Rerun logging is enabled by default. The logging behavior can be overridden at runtime using the `RERUN` environment variable:

```sh
export RERUN=off
python my_rerun_enabled_script.py
# or
cargo run my_rerun_package

# No log messages will be transmitted.
```

The `RERUN` environment variable is read once during SDK initialization. The accepted values for `RERUN` are `1/on/true`, and `0/off/false`.

ℹ️ Note: When Rerun is disabled, logging statements are bypassed and essentially become no-ops.

## Creating a default-off setup in code

The "default-on" behavior can also be changed to a "default-off" behavior:

code-example: default-off-session
