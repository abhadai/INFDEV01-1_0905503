while True:
    # Ask player 1 for input
    player_one_choice = input("Player 1, type R for rock, P for paper or S for scissors!")
    player_one_choice = player_one_choice.capitalize()

    # Ask player 2 for input
    player_two_choice = input("Player 2, type R for rock, P for paper or S for scissors!")
    player_two_choice = player_two_choice.capitalize()

    # Rock and rock ties
    if(player_one_choice == "R" and player_two_choice == "R"):
        print("No one wins! Both rocks evolved into one Onix.")

    # Paper beats rock
    if(player_one_choice == "R" and player_two_choice == "P"):
        print("P2 wins! Paper wrinkled itself around rock.")
    
    # Rock beats scissors      
    if(player_one_choice == "R" and player_two_choice == "S"):
        print("P1 wins! Scissors broke itself on the rock.")
    
    # Paper beats rock
    if(player_one_choice == "P" and player_two_choice == "R"):
        print("P1 wins! Paper wrinkled itself around rock.")
    
    # Paper and paper ties
    if(player_one_choice == "P" and player_two_choice == "P"):
        print("No one wins! The two papers are now a newsarticle.")

    # Scissors beats paper
    if(player_one_choice == "P" and player_two_choice == "S"):
        print("P2 wins! Scissors cut the paper in half.")

    # Paper beats rock
    if(player_one_choice == "S" and player_two_choice == "R"):
        print("P2 wins! Rock crushed scissor.")
    
    # Paper and paper ties
    if(player_one_choice == "S" and player_two_choice == "P"):
        print("P1 wins! Scissor cut paper in half.")

    # Scissors beats paper
    if(player_one_choice == "S" and player_two_choice == "S"):
        print("No one wins! The two scissor lived happily ever after.")