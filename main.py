from imports import *

term = os.getenv( "TERM" );display = os.getenv( "DISPLAY" )

dirpath = os.path.abspath("/".join(__file__.split("/")[:-2]))

if term is None and display is None:

    os.system(f"python3 {dirpath}/cron.py")

else:

    os.system(f"python3 {dirpath}/user.py")
