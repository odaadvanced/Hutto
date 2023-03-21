import random
def election_flip(probability_of_A):
    if random.random() < probability_of_A:
        return "A"
    else:
        return "B"

def election_results():
    A_wins = 0
    for election in range (10000):
        Candidate_A = 0
        if election_flip(.87) == "A":
            Candidate_A = Candidate_A + 1
        if election_flip (.65) == "A":
            Candidate_A = Candidate_A + 1
        if election_flip (.17) == "A":
            Candidate_A = Candidate_A + 1
        if Candidate_A > 1:
            A_wins = A_wins + 1
    return A_wins / 10000 * 100

print (f"Candidate A won {election_results():.2f}% of the time.")