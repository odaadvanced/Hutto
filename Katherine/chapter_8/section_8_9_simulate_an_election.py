import random

def tilted_election(probability_of_candidate_a_winning):
    if random.random() <= probability_of_candidate_a_winning:
        return 1
    else:
        return 0

candidate_a_elections = 0

for trial in range(10_000):
    candidate_a_regions = 0
    if tilted_election(.87) == 1:
        candidate_a_regions += 1
    if tilted_election(.65) == 1:
        candidate_a_regions += 1
    if tilted_election(.17) == 1:
        candidate_a_regions += 1
    if candidate_a_regions >= 2:
        candidate_a_elections += 1
print(f"Candidate A wins {candidate_a_elections/100}% of elections")