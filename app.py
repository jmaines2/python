import pandas as pd
get_ipython().run_line_magic('pylab', 'inline')
get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('config', 'SqlMagic.autopandas = True')
get_ipython().run_line_magic('config', 'SqlMagic.displaylimit=100')

import warnings
warnings.filterwarnings("ignore", message="Data Validation extension is not supported and will be removed")

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from pprint import pprint,pformat
from pslib.jupyter.datafields import DataFields
import pslib.billing as psbill
import pslib.drugdata.medispan as psmedispan
import pslib.statefee.statefee_alt as psstatefee_alt
import pslib.pricing as psprice
import pslib.excel as psexcel
import pslib.ice.ice as psice

pd.options.display.float_format = '{:,.2f}'.format
pd.options.display.max_rows = 1000

def duplicatesInList(l):
    dupes=set()
    for e in l:
        if l.count(e) > 1:
            dupes.add(e)
    return list(dupes)
