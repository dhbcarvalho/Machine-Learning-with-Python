# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[],player_history=[]):
    #Defining the array of possible moves
    moves=["R","P","S"]
    #If prev_play is empty, the first move is selected randomly.
    if prev_play=="":
        guess=moves[random.randint(0,2)]
        player_history.append(guess)
        return (guess)
    
    #We append the prev_play to opponent_history.
    opponent_history.append(prev_play)
    
    #Initializing the model dictionary. We keep track of opponents next move given the previous round state (there are 3x3=9 possible states).
    #"RP" means last round opponent played "R", we played "P". 
    model = {"RR":{"R":0,"P":0,"S":0},
             "RP":{"R":0,"P":0,"S":0},
             "RS":{"R":0,"P":0,"S":0},
             "PR":{"R":0,"P":0,"S":0},
             "PP":{"R":0,"P":0,"S":0},
             "PS":{"R":0,"P":0,"S":0},
             "SR":{"R":0,"P":0,"S":0},
             "SP":{"R":0,"P":0,"S":0},
             "SS":{"R":0,"P":0,"S":0},         
            }
    
    #memory indicates how far back we keep track of enemy moves.
    memory=-1*min(30,len(opponent_history))
    
    #We update the model dictionary by looping through opponent history.
    for (i,move) in enumerate(opponent_history[memory:-1]):
        state=move+player_history[memory+i]
        opponent_next_move=opponent_history[memory+i+1]
        model[state][opponent_next_move]+=1

    #Our current state is "Opponent's Previous Move+ Our Previous Move".
    state=prev_play+player_history[-1]
    
    #We predict what would the opponent play by looking up the most frequent response to current state
    prediction=max(model[state],key=model[state].get)

    #We pick the counter to that move.
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess=ideal_response[prediction]
    
    #finally we append our move to our own history
    player_history.append(guess)
    return guess
    