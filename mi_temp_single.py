#!/usr/bin/env python3

from btlewrap import available_backends, BluepyBackend, GatttoolBackend, PygattBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, \
    MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY

backend = BluepyBackend
mac = "4c:65:a8:d7:ce:85"
poller = MiTempBtPoller(mac, backend)
print("{}".format(poller.parameter_value(MI_TEMPERATURE)))