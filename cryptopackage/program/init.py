import sys
import typer
import subprocess
from .main import program
#from . import common


@program.command(name="init")
def program_init():
    """Initialize a project
    """
    # Return default
    subprocess.call(['sh', './init.sh'])
   