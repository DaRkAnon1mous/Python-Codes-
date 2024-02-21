def orangecap(d):
  player_scores = {}

  for match, players in d.items():
      for player, score in players.items():
          if player in player_scores:
              player_scores[player] += score
          else:
              player_scores[player] = score

  top_player = max(player_scores, key=player_scores.get)
  topscore = player_scores[top_player]

  return (top_player, topscore)

print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))
  # Output: ('player3', 100)

print(orangecap({'test1':{'Pant':84, 'Kohli':120}, 'test2':{'Pant':59, 'Gill':42}}))
  # Output: ('Pant', 143)
