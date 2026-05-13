from pybaseball import schedule_and_record
from pybaseball import standings

import pandas as pd

teamlist = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
    'KC', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
    'SD', 'SEA', 'SF', 'STL', 'TB', 'TEX', 'TOR', 'WSH' 
]

#print(teamlist)


""" for team in teamlist:
    print(team) """
        
atlsched = schedule_and_record(2026, 'ATL')
standings2026 = standings(2026)

print(standings2026)

#print(atlsched.iloc[:, 0:4])
#print(type(atlsched.iloc[1,0]))