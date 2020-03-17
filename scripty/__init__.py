import os

DEFAULT_FROM_DATE = '1776-07-04'

if os.environ['DEFAULT_FROM_DATE']:
    DEFAULT_FROM_DATE = os.environ['DEFAULT_FROM_DATE']
