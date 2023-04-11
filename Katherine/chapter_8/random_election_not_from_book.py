import random

candidate_a_votes = 0
candidate_b_votes = 0
candidate_a_win = 0
candidate_b_win = 0



def winning_election():
    global candidate_a_votes
    global candidate_b_votes
    global candidate_a_win
    global candidate_b_win
    for region in range(1,4):
        candidate_a_votes = random.randint(0, 100)
        candidate_b_votes = 100 - int(candidate_a_votes)
        print(f"Region {region}: Candidate A has a {candidate_a_votes} votes")
        if candidate_a_votes > candidate_b_votes:
            candidate_a_win = candidate_a_win + 1
        elif candidate_b_votes > candidate_a_votes:
            candidate_b_win = candidate_b_win + 1
        else:
           continue
    if candidate_a_win == 2:
        print("Candidate A wins the election.")
    else:
        print("Candidate B wins the election.")

winning_election()