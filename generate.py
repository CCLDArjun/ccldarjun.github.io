import jinja2
from jinja2 import Environment, FileSystemLoader
import glob
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("file", help="file to generate")
args = parser.parse_args()

templateLoader = jinja2.FileSystemLoader(searchpath=".")
templateEnv = jinja2.Environment(loader=templateLoader)

template = templateEnv.get_template(args.file)
text = template.render()

ofile = re.sub(".jinja", "", args.file)
ofile = re.sub("^templates/", "", ofile)

with open(ofile, "w") as f:
    f.write(text)

