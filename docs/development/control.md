---
layout: template
title: Control
permalink: /development/control/
link_group: development
---
# Control

Controlling a device is done with the remote control interface,
{% include api i="interface.RemoteControl" %}. It allows you navigate the menus and
change playback (play, pause, etc.).

## Using the Remote Control API

After connecting to a device, you get the remote control via {% include api i="interface.AppleTV.remote_control" %}:

```python
atv = await pyatv.connect(config, ...)
rc = atv.remote_control
```

You can then control via the available functions:

```python
await rc.up()
await rc.select()
await rc.set_position(100)
```

All available actions can be found in {% include api i="interface.RemoteControl" %}.
