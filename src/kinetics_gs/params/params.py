import json

_conf = json.load(open('params.json', 'r'))

x1v0 = _conf['x1v0']  # S1/S0, where S1 reacts, and S0 does not
Ws1 = _conf['Ws1']    # 1/T1 of S1, [1/s]
Ws0 = Ws1             # 1/T1 of S0, [1/s]
Wp1 = _conf['Wp1']    # 1/T1 of p1, [1/s]
Wp2 = _conf['Wp2']    # 1/T1 of p2, [1/s]
k1 = _conf['k1']      # conversion rate s-->p1 [1/s]
km1 = _conf['km1']    # conversion rate s<--p1 [1/s]
k2 = _conf['k2']      # conversion rate s-->p2 [1/s]
km2 = _conf['km2']    # conversion rate s<--p2 [1/s]
t0 = _conf['t0']      # time before the first Equ. point (s) was acquired.
