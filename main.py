import argparse
import os
from dotenv import load_dotenv
from my_ken.cli import cli

if __name__ == "__main__":
    # load_dotenv(".env")

    # parser = argparse.ArgumentParser(prog='my_ken')
    # args = parser.parse_args()

    # print(parser.print_help())
    cli()