from pybaseball import schedule_and_record
from pybaseball import standings

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np  

currseason = pd.DataFrame()
#print(currseason.head(25))

teamlist = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
    'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
    'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WSH' 
]

currseason = pd.concat([currseason, schedule_and_record(2026, 'BAL')])
    

print(currseason.head(5)) 

""" for x in range(0, len(teamlist)):
    currseason = pd.concat([currseason, schedule_and_record(2026, teamlist[x])]) """

print(currseason.shape)
#atlsched = schedule_and_record(2026, 'ATL')

#print(atlsched.head(5))
#print(atlsched.iloc[:, 0:4])
#print(type(atlsched.iloc[1,0]))