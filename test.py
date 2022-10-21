from tokenize import String
from proof_of_stake import ProofOfStake
import string
import random
def get_random_str(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string
if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update("Gowtham", 30)
    pos.update("Harsha", 39)
    pos.update("Guru",41)

    Gowtham_wins = 0
    Harsha_wins = 0
    Guru_wins=0

    for i in range(100):
        forger = pos.forger(get_random_str(i))
        if forger == "Gowtham":
            Gowtham_wins += 1
        elif forger == "Harsha":
            Harsha_wins += 1
        else:
            Guru_wins +=1
    print("Gowtham won: " + str(Gowtham_wins) + " times")
    print("Harsha won: " + str(Harsha_wins) + " times")
    print("Guru won: " + str(Guru_wins) + " times")
    if(Gowtham_wins>=Harsha_wins and Gowtham_wins>=Guru_wins):
        print("Gowtham is Validating")
    elif(Harsha_wins>=Gowtham_wins and Harsha_wins>=Guru_wins):
        print("Harsha is Validating")
    elif(Guru_wins>=Harsha_wins and Guru_wins>=Gowtham_wins):
        print("Guru is Validating")