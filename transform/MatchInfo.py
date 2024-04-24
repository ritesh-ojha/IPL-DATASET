#!/usr/bin/env python3

import json
import csv
import os
def get_bowling_team (inning, teams, batting_team):
    if inning == 1:
        return teams[1] if teams[0] == batting_team else teams[0]
    else:
        return teams[0] if teams[1] == batting_team else teams[1]

with open('Match_Info.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
  
  # Write header row
    writer.writerow(["match_number", "team1", "team2", "match_date", "toss_winner", "toss_decision" ,"result", "eliminator","winner", "player_of_match", "venue", "city", "team1_players", "team2_players"])
    for filename in os.listdir('json/ipl_match'):
        if filename.endswith('.json'):
            try:  
                # Open and load JSON file
                with open(os.path.join('json/ipl_match', filename)) as f:
                    data = json.load(f)
                    info = data['info']
                    
                    # Extract match number from filename
                    # Extract match number from filename
                    match_number = filename.split('.')[0]  
                    team1 = info['teams'][0]
                    team2 = info['teams'][1]
                    match_date = info['dates'][0]
                    result = info['outcome'].get('result','Win')
                    winner = (info['outcome']).get('winner','NA')
                    eliminator = info['outcome'].get('eliminator', 'NA')
                    player_of_match = (info.get('player_of_match', 'NA'))[0]
                    venue = info['venue']
                    # city = info['city']
                    city = info.get('city', 'NA')  # Use get() method to avoid
                    
                    toss_winner = info['toss']['winner']
                    decision = info['toss']['decision']
                    team1_players = ', '.join(info['players'][team1])
                    team2_players = ', '.join(info['players'][team2])
                    row = [match_number, team1, team2, match_date, toss_winner, decision ,result, eliminator,winner, player_of_match, venue, city, team1_players, team2_players]
                    writer.writerow(row)
                
            except Exception as e:
                print(filename + " " + str(e))
print("Done")