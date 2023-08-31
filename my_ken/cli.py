import argparse
import os
from dotenv import load_dotenv

def cli():
    """My Ken CLI."""
    load_dotenv(".env")

    parser = argparse.ArgumentParser(prog='my_ken')
    args = parser.parse_args()

    print(parser.print_help())