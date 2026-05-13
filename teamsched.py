from pybaseball import schedule_and_record

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

print(atlsched.head())