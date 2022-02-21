touchfrom cs50 import get_string, get_float, get_int

def main():
  player_name = get_string("Enter player name: ")
  total_goals = get_int("Enter total goals scored: ")
  goals_per_match = get_float("Enter average goals per match: ")

  print(f"Type of player_name: {player_name} is {type(player_name)}")
  print(f"Type of total_goals: {total_goals} is {type(total_goals)}")
  print(f"Type of goals_per_match: {goals_per_match} is {type(goals_per_match)}")
  

if __name__ == "__main__":
    main()