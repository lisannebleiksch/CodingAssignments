# Add your code after this line
#Part 1 1988 NL - RU finals report. #1 players names. 
scored_player_1 = 'Ruud Gullit' 
scored_player_2 = 'Marco van Basten' 

#2 goals. 
goal_0 = 32 
goal_1 = 54 

#3 scorers. 
scorers = scored_player_1 + " " + str(goal_0) + ", " + scored_player_2 + ' ' + str(goal_1) 
print(scorers) 

#4 report. 
report = f'{scored_player_1} scored in the {goal_0}nd minute' '\n' f'{scored_player_2} scored in the {goal_1}th minute' 
print(report)


#Part 2 Use slicing and find-method to isolate player firstname.
#1 varible player. 
player = "Ronald Koeman" 

#2 firstname slicing 
find_space = player.find(" ") 
first_name = player [0:find_space] 
print(first_name) 

#3 use find, slicing and len. 
last_name_len = len(player[player.find(" ") + 1:]) 
print(last_name_len) 

#4 isolate firstname. 
name_short = player[0: 1] + "." + player[player.find (" "):] 
print(name_short) 

#5 chant. 
chant0 = (first_name + "!" + " ") * len(first_name) 
chant = chant0.strip() 
print(chant) 

#6 good chant. 
good_chant = chant == "Ronald! Ronald! Ronald! Ronald! Ronald! Ronald!" 
print(good_chant)


