#!/usr/bin/env python3

import pandas as pd

(pd.read_json('json/ipl_team_info/teams_info.json', orient='records'))\
    .to_csv('teams_info.csv', index=False)