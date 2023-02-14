---
title: Troubleshooting
order: 8
---

You can set `RUST_LOG=debug` before running to get some verbose logging output.

If you run into any issues don't hesitate to [open a ticket](https://github.com/rerun-io/rerun/issues/new/choose)
or [join our Discord](https://discord.gg/Gcm8BbTaAj).

## Running on Linux
Rerun should work out-of-the-box on Mac and Windows, but on Linux you need to first run:

`sudo apt-get install -y libclang-dev libgtk-3-dev libxcb-render0-dev libxcb-shape0-dev libxcb-xfixes0-dev libxkbcommon-dev libssl-dev`

On Fedora Rawhide you need to run:

`dnf install clang clang-devel clang-tools-extra libxkbcommon-devel pkg-config openssl-devel libxcb-devel`

On WSL2 you need to run:

`sudo apt-get install -y libvulkan1 libxcb-randr0 mesa-vulkan-drivers`
