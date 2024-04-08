from __future__ import annotations
import argparse
from dateutil.relativedelta import relativedelta
import re
from argparse import ArgumentParser

from .policy import parse_duration





COUNT_OPTS = [
  "--keep-last",
  "--keep-hourly",
  "--keep-daily",
  "--keep-weekly",
  "--keep-monthly",
  "--keep-yearly"
]

WITHIN_OPTS = [
  "--keep-within",
  "--keep-within-hourly",
  "--keep-within-daily",
  "--keep-within-weekly",
  "--keep-within-monthly",
  "--keep-within-yearly"
]


def setup_parser(parser: ArgumentParser) -> None:
  # policy arguments
  parser.add_argument('--keep-name', type=re.compile, metavar="REGEX", default=None)
  for opt in COUNT_OPTS:
    parser.add_argument(opt, type=int, metavar="N", default=0)
  for opt in WITHIN_OPTS:
    parser.add_argument(opt, type=parse_duration, metavar="DURATION", default=relativedelta())

  # # other arguments
  # parser.add_argument('-n', '--dry-run', action='store_true')
  # parser.add_argument('-d', '--dataset', type=str, metavar="DATASET", default=None)
  # parser.add_argument('-r', '--recursive', action='store_true')



def get_args():
  parser = argparse.ArgumentParser("zfsnap_prune")

 

  return parser.parse_args()