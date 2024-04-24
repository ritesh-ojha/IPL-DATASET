#!/usr/bin/env python3

import json
import csv
import os

# Now you can write your output file
with open('Ball_By_Ball_Match_Data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  
  # Write header row
  writer.writerow(["ID", "Innings", "Overs", "BallNumber", "Batter", "Bowler", "NonStriker", 
                     "ExtraType", "BatsmanRun", "ExtrasRun", "TotalRun",  
                     "IsWicketDelivery", "PlayerOut", "Kind", "FieldersInvolved", "BattingTeam"])
  for filename in os.listdir('json/ipl_match'):
    if filename.endswith('.json'):
        
      # Open and load JSON file
      with open(os.path.join('json/ipl_match', filename)) as f:
        data = json.load(f)
        
      # Extract match number from filename
      match_number = filename.split('.')[0]  
      for i, inning in enumerate(data['innings']):
        if i == 0:
          inning_num = 1
        else:
          inning_num = 2
        team = inning['team']
        for over in inning['overs']:
          over_num = over['over']
          for i, delivery in enumerate(over['deliveries']):
                  ball_num = i + 1
            
                  batter = delivery.get('batter')
                  bowler = delivery['bowler']
                  non_striker = delivery.get('non_striker')
                  
                  extras = delivery.get('extras', {})
                  extra_type = ','.join(extras.keys())
                  
                  batsman_run = delivery['runs'].get('batter', 0)
                  extras_run = delivery['runs'].get('extras', 0)
                  total_run = delivery['runs']['total']
                  
                  is_boundary = total_run in [4, 6]
                  
                  wickets = delivery.get('wickets')
                  is_wicket = 1 if 'wickets' in delivery else 0
                  if is_wicket:
                    player_out = wickets[0]['player_out'] 
                    kind = wickets[0]['kind']
                    
                    fielders = []
                    if kind == 'bowled':
                      fielders = 'NA'
                    else:
                      for f in wickets[0].get('fielders', []):
                        fielders.append(f['name'])
                    
                      fielders = ','.join(fielders) 
                  else:
                    player_out = 'NA'
                    kind = 'NA'
                    fielders = 'NA'
                  
                  row = [match_number,inning_num, over_num,ball_num,
            batter, bowler, non_striker, extra_type, batsman_run,  
            extras_run, total_run, is_wicket,
            player_out, kind, fielders,team]
                  # Write row to CSV
                  writer.writerow(row)
print("Done")
# hello.py

# print("Hello, World!")