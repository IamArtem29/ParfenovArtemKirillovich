# -*- coding: utf-8 -*-

#4
seconds = 111111
days = seconds // 86400
seconds = seconds  - 86400 * days
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes  * 60
print(days, hours, minutes, seconds)