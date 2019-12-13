import sys
import logbook
import argparse
import pandas as pd
import numpy as np
from numpy import linalg as la

from kinetics_gs.params import *

DEFAULT_PULSE_ANGLE = 10

logbook.StreamHandler(sys.stdout).push_application()
logger = logbook.Logger()


def get_rate_matrix():
    return pd.DataFrame([[-Ws0, 0,       0,           0],
                         [0,    -Ws1-k1, km1,         0],
                         [0,    k1,      -Wp1-km1-k2, km2],
                         [0,    0,       k2,          -Wp2-km2]])


def simulate_signal(rate_matrix, time_series, pulse_angle):
    eig_vecs, eig_vals = la.eig(rate_matrix)
    eig_vecs_diag = np.diag(eig_vecs)
    initial_polarization = [1 - x1v0, x1v0, 0, 0]
    polarization = pd.DataFrame(np.zeros((4, len(time_series))))
    pulse_angle_cosine = np.cos(pulse_angle)
    for n, t in enumerate(time_series):
        num = eig_vals * np.diag(np.exp(eig_vecs_diag * t))
        den = eig_vals * initial_polarization * (pulse_angle_cosine ** (n - 1))
        polarization.ix[:, n] = np.divide(num, den)
    return polarization


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='This is the path of the file.')
    parser.add_argument('pulse_angle', nargs='?', default=DEFAULT_PULSE_ANGLE,
                        help=f'This is the pulse angle of the experiment. Defaults to {DEFAULT_PULSE_ANGLE} degrees.')
    parser.add_argument('-v', '--verbose', dest='verbose', required=False, default=False, action='store_true',
                        help='This is a flag for testing')
    return parser.parse_args(args)


def main(args):
    global logger
    logger = logbook.Logger('KineticsGS', level=logbook.DEBUG if args.verbose else logbook.NOTICE)
    rm = get_rate_matrix()
    print(rm.iloc[1])


if __name__ == '__main__':
    main(parse_args())
