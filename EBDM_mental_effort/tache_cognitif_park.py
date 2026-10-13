'''exeperiment to test the motivation in parkinson patients'''


'''


---- Columns output data ----

output = "subject_id, block, trial, round_number, correct_resp, keys, acc, rt,triall, trigg_resp, incent, congruence, trial_duration\n"

|  | Columns Name           | Signification      | Var   | Details                                                                                                                                            |
|  |                        |                    |       |                                                                                                                                                    |
|0 | subject_id             | ID Subject         | Int   | Subject number.                                                                                                                                    | 
|1 | trial                  | trial number       | Int   | trial number                                                                                                                                       |
|2 | round_number           | Block number       | Int   | Number of trial in total for all block (1 -> 10 blocks).                                                                                           |                                                                                                                                                                              
|3 | correct_resp           | Expected key       | Int   | The key response expected for a correct response (1-left or 2-right).                                                                              |
|4 | keys                   | Pressed key        | Int   | The key response pressed (1-left or 2-right).                                                                                                      |                                                                                                        
|5 | accuracy               | Accuracy           | Int   | The accuracy pf each subject for the task:  0 if incorrect response, 1 if correct response, else -1.                                               |
|6 | rt                     | RT                 | Float | Response Time of participant from start of stimulus to button press (in ms).                                                                       |                                                            
|7 | triall                 | Type of block      | Str   | e.g.win(for each right answer the participant got the monetory incent) loss (for each wrong answer the participant loses money already earned).    |                                                 
|8 | trigg_resp             | Response trigger   | Int   | The response trigger indicate response subject (correct or not, left or right).                                                                    |
|9 | incent                 | the monetary incent| Int   | the monetary incentive chosen for the block.                                                                                                       |                                                 
|10| congruence             | Type of block      | Str   | e.g., congruent (greater number is high fontsize) / incongruent.                                                                                   |                                                 
|11| trial_duration         | trial duration     | Int   | the duration for a trial determined in the calibration phase                                                                                       |                                                 

Response trigger
| 100              | Incorrect left response      |
| 102              | Incorrect right response     |
| 101              | Correct left response        |
| 103              | Correct right response       |
'''



from psychopy import core, data, event, visual, gui, monitors
import random
import os
from psychopy.hardware import keyboard

#-------------------------------------------------------------------------------------------------
# ------------------------------------- Experiments variables ------------------------------------
#-------------------------------------------------------------------------------------------------

# Initialize keyboard
resp = keyboard.Keyboard()
defaultKeyboard = keyboard.Keyboard()

# Experiment parameters
touchIs = ['left', 'right']
monetary_incentives = [0.01, 0.2, 0.5, 1, 5, 20]
valence_condition = ['gain', 'loss']
total = 0

# File save path
folder = r"C:\Users\Mohamed\Documents\Modèles Office personnalisés"


#------------------------------------------------------------------------------------------------------------
# -------------------------------- Experiments infos and parameters -----------------------------------------
#------------------------------------------------------------------------------------------------------------

# Experiment info dialog
expName = "Exp_parkinson_motivation"
expInfo = {
    'id_participant': '',
    'age': '',
    'sexe': ['Homme', 'Femme'],
    'groupe': ['Contrôle', 'Parkinson']
}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName, order=['id_participant', 'age', 'sexe', 'groupe'])
if not dlg.OK: 
    core.quit()
date_exp = data.getDateStr()

# File save
filename = expName + '_s' + expInfo['id_participant'] + '_' + date_exp
running_filename = os.path.join(folder, filename + '_TEMP.txt')

# Output header
output = "subject_id, block, trial, round_number, correct_resp, keys, acc, rt,triall, trigg_resp, incent, congruence, trial_duration\n"

with open(running_filename, 'a') as f_handle:
    f_handle.write(output)

subject_id = int(expInfo['id_participant'])

# Window configuration
mon = monitors.Monitor('default', width=29, distance=70.0)
win = visual.Window(fullscr=True, monitor=mon, size=(1280, 720), color=[0, 0, 0], colorSpace='rgb255', units='deg')

# Image stimulus paths
image_paths = {
    0.01: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\france-1-euro-cent-2001.jpg",
    0.2: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\IMAGE20CENTIMES.jpeg",
    0.5: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\50CENTIMES.jpeg",
    1: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\1euro.jpeg",
    5: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\5EURO.jpeg",
    20: r"C:\Users\Mohamed\Downloads\exp_cognitive_task_parkinson_motivation\IMAGE20EUROS.jpeg",
}

# Function to get the image path based on the incentive
def get_image_path(incentive):
    path = image_paths.get(incentive, "path/to/default/image.png")
    if path == "path/to/default/image.png":
        print(f"Warning: Image path for incentive {incentive} not found. Using default image.")
    return path

# Text settings
police = 'Consolas'
win.setMouseVisible(False) # hide the mouse cursor
size_instruc = 0.5
size_feedback = 0.7
text_dict = {'win': win, 'ori': 0, 'font': police, 'pos': [0, 0], 'colorSpace': 'rgb255'}
instruc_dict = {**text_dict, 'height': size_instruc, 'color': [255, 255, 255]}
feedback_dict = {**text_dict, 'height': size_feedback, 'color': [1, 0, 0]}  
feedback_dict['pos'] = [0, 4]  # Change the position here



#-------------------------------------------------------------------------------------------------
# ------------------------------------------ Instructions ----------------------------------------
#-------------------------------------------------------------------------------------------------

# Instructions
instructions_1 = visual.TextStim(**instruc_dict, text=u"Bienvenue !\nAppuyez sur la touche droite ou gauche pour continuer .")  
instructions_2 = visual.TextStim(**instruc_dict, text=u"Devant vous, une échelle apparaîtra avec deux chiffres différents et de tailles différentes à chaque niveau, un de chaque côté. Vous devez choisir le chiffre ayant la plus grande valeur, et un point montera sur l'échelle si vous donnez la bonne réponse")  
instructions_3 = visual.TextStim(**instruc_dict, text=u"il existe 2 typed d'essais : \
                                 Gain : chaque réponse correcte sera récompensée en fonction de l'incitation monétaire associée à l'essai, représentée par un point vert sur l'échelle \
                                 Perte : chaque réponse correcte vous permet de conserver l'argent déjà gagné, représenté par un point rouge sur l'échelle.\
                                 le type d'essai sera choisi aléatoirement pour chaque essai.\
                                 le point jaune représente votre position actuelle sur l'échelle.")  
instructions_4 = visual.TextStim(**instruc_dict, text=u"Nous commencerons par une phase d'entraînement pour vous familiariser avec la tâche.\
                                 Répondez le plus rapidement possible à chaque essai.")
instructions_5 = visual.TextStim(**instruc_dict, text=u"Pour commencer l'expérience principale, appuyez sur la barre d'espace. \
                                 Bonne chance !") 
fin= visual.TextStim(**instruc_dict, text=u"Fin de l'expérience .\
                      Merci d'avoir participé !")

#-------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------Functions------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------


# Function to determine monetary incentive
def monetary_incentive(triall, correct_resp, keys, incentive, correct_respponse):
    global total
    incent = 0 
    if triall == 'gain' and correct_resp in keys:
        total += incentive*(correct_respponse/10)
        incent += incentive*(correct_respponse/10)
        print(f"Added {incentive} to total. New total: {total}")
    elif triall == 'loss' and correct_resp not in keys:
        total -= incentive*(1-correct_respponse/10)
        incent += incentive*(1-correct_respponse/10)
        if total < 0:
            total = 0
        print(f"Subtracted {incentive} from total. New total: {total}")
    return total, incent

# Generate ladder values
def generate_ladder_values(num_steps, Block_type):
    nombres = list(range(1, 10))
    tailles = [0.5, 1]
    trials = []
    
    for _ in range(num_steps):
        n1, n2 = random.sample(nombres, 2)
        taille1, taille2 = random.sample(tailles, 2)
        correct_resp = touchIs[0] if n1 > n2 else touchIs[1]
        congruence = "Congruent" if taille1 > taille2 and n1 > n2 or taille1 < taille2 and n1 < n2 else "Incongruent"
        trials.append((n1, taille1, n2, taille2, congruence, correct_resp, Block_type))
    
    random.shuffle(trials)
    return trials

def instruction_exp(instruction, touchIs):
    kb_delay = 0
    win.callOnFlip(resp.clearEvents, eventType='keyboard')
    while True:
        if kb_delay:
            theseKeys = resp.getKeys(keyList=touchIs, waitRelease=False)
            if len(theseKeys):
                break
            if defaultKeyboard.getKeys(keyList=["escape"], waitRelease=False):
                core.quit()
        instruction.draw()
        win.flip()
        if not kb_delay:
            kb_delay = 1
    win.flip()
    core.wait(1)

#Function to draw the ladder with digits and participant position

def draw_ladder(win, trials, current_position, current_position1, colors):
    z = -3.6
    print("Starting to draw ladder...")
    print("Current position:", current_position)

    for i, (n1, taille1, n2, taille2, condition, correct_resp, trial) in enumerate(trials):
        rectangle = visual.Rect(win, width=3.2, height=0.2, pos=(0, z), fillColor="white")
        rectangle.draw()
        left_text = visual.TextStim(win, text=str(n1), pos=(-2.4, z + 0.2), color="white", height=taille1)
        right_text = visual.TextStim(win, text=str(n2), pos=(2.4, z + 0.2), color="white", height=taille2)
        left_text.draw()
        right_text.draw()
        print(f"Drawing trial {i}: n1={n1}, taille1={taille1}, n2={n2}, taille2={taille2}, z={z}")
        z += 0.8

    left_rectangle = visual.Rect(win, width=0.08, height=9.4, pos=(-1.6, 1), fillColor="white")
    left_rectangle.draw()
    right_rectangle = visual.Rect(win, width=0.08, height=9.4, pos=(1.6, 1), fillColor="white")
    right_rectangle.draw()

    participant_position = visual.Circle(win, radius=0.08, pos=(0, -3.6 + current_position * 0.8), fillColor=colors)# moves up when answer is right
    participant_position.draw()
    participant_position1 = visual.Circle(win, radius=0.08, pos=(1, -3.6 + current_position1* 0.8), fillColor="yellow")# indicate participant position (it moves up when an answer is made)
    participant_position1.draw()
    print("Drawing participant position at:", (0, -0.9 + current_position * 0.1))
    win.flip()

#-------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------Calibration phase-------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

try:
    instruction_exp(instructions_1,touchIs)
    instruction_exp(instructions_2,touchIs)
    instruction_exp(instructions_3,touchIs)
    instruction_exp(instructions_4,touchIs)
except Exception as e:
    print(f"An error occurred during instructions: {e}")
    win.close()
    core.quit() 

num_rounds = 5
rectangle_number = 10
calibration = []

for round_number in range(num_rounds):
    for _ in range(3): win.flip()  # Warm up GPU
    current_position = 0
    current_position1 = 0
    ladder_values = generate_ladder_values(rectangle_number , Block_type='gain')
    print(ladder_values)
    incentives = random.choice(monetary_incentives)
    print(f"Round {round_number + 1}: Selected monetary incentive is {incentives}")
    
    horloge = core.Clock()
    horloge.reset()
    correct_respponse = 0
    for trial in range(rectangle_number):
        if len(ladder_values[trial]) > 6:
            triall = ladder_values[trial][6]
        else:
            print(f"Error: Unexpected trial structure: {ladder_values[trial]}")
            continue  # Skip this iteration if it's invalid

        colors = 'blue'
        draw_ladder(win, ladder_values, current_position, current_position1 ,colors)
        keys = []

        response_timer = core.Clock()
        while True:  # Infinite loop until a break condition is met
            keys = event.getKeys(keyList=['left', 'right', 'escape'])
            
            if 'escape' in keys:
                win.close()
                core.quit()
            
            if keys:
                break  # Break the loop if any key is pressed
        if not keys:
            print("No response detected. Moving to next trial.")

        correct_resp = ladder_values[trial][5]
        total, incent = monetary_incentive(triall, correct_resp, keys, incentives, correct_respponse)
        current_position1 += 1
        if correct_resp in keys:
            print(f"Round {round_number + 1}: Trial {trial + 1}: Correct response!")
            current_position += 1
            correct_respponse += 1
            print(f"Total: {total}")

    elapsed_time = horloge.getTime()
    calibration.append(elapsed_time)

    win.flip()
    core.wait(2)

# Check if calibration is empty
if calibration:
    trial_duration = min(calibration) * 0.7  #to get the participant response time (70% of the fastest response time)
    print(trial_duration)

#-------------------------------------------------------------------------------------------------------------------------------
#---------------------------------- Instructions for the main experiment-------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------

try:
    instruction_exp(instructions_5,touchIs)  # Show the last instruction
except Exception as e:
    print(f"An error occurred during instructions: {e}")
    win.close()
    core.quit() 

num_rounds = 12
rectangle_number = 10
data_container = []
total = 0
block = 0

#main experiment loop 

for Block in range(10):
    #valence condition (loss or win)
    Block_type = random.choice(valence_condition)
    for round_number in range(num_rounds):
        for _ in range(3): win.flip()
        current_position = 0
        current_position1 = 0
        ladder_values = generate_ladder_values(rectangle_number, Block_type)
        print(ladder_values)
        incentives = random.choice(monetary_incentives)
        print(f"Round {round_number + 1}: Selected monetary incentive is {incentives}")
        
        timer = core.Clock()
        timer.reset()

        rt = -1   # RT
        acc = -1  # accuracy with 0 if incorrect, 1 if correct, else -1
        correct_response = 0
        correct_respponse = 0
        for trial in range(rectangle_number):
            if timer.getTime() > trial_duration:
                print("Time's up!")
                break
            
            if len(ladder_values[trial]) > 6:
                triall = ladder_values[trial][6]
            else:
                print(f"Error: Unexpected trial structure: {ladder_values[trial]}")
                continue  # Skip this iteration if it's invalid

            colors = "green" if triall == 'gain' else "red" # Change the color of the circle based on the trial type

            draw_ladder(win, ladder_values, current_position, current_position1, colors)

            response_timer = core.Clock()
            keys = []
            while True:  
                keys = event.getKeys(keyList=['left', 'right', 'escape'])
                
                if keys:
                    break

                if 'escape' in keys:
                    win.close()
                    core.quit()
                rt = response_timer.getTime()
            if not keys:
                print("No response detected. Moving to next trial.")
                acc=-1

            
            congruence = ladder_values[trial][4]
            correct_resp = ladder_values[trial][5]
            
            total, incent = monetary_incentive(triall, correct_resp, keys, incentives, correct_respponse)

            # Load the image stimulus
            image_path = get_image_path(incentives)
            print(f"Loading image from: {image_path}")
            try:
                image_stim = visual.ImageStim(win=win, image=image_path, pos=(-10, 5.5), size=(3, 2))
                image_stim.draw()
            except Exception as e:
                print(f"Error loading image: {e}")
            
            current_position1 += 1
            if correct_resp in keys:
                print(f"Round {round_number + 1}: Trial {trial + 1}: Correct response!")
                current_position += 1
                correct_respponse +=1
                print(f"Total: {total}")
                acc = 1
                if correct_resp == 'left':
                    trigg_resp = 101
                else:
                    trigg_resp = 103
            if correct_resp not in keys:
                print(f"Round {round_number + 1}: Trial {trial + 1}: Incorrect")
                acc = 0
                if keys == 'left':
                    trigg_resp = 100
                else:
                    trigg_resp = 102    

            #data saving
            data_array = [subject_id, trial, block, round_number, correct_resp, keys, acc, rt, Block_type, trigg_resp, incent, congruence,trial_duration]
            data_container.append(data_array)
            with open(running_filename, 'a') as f_handle:
                f_handle.write(','.join([str(data) for data in data_array]) + '\n')

        win.flip()
        core.wait(0,5)
        
    feedback = visual.TextStim(win, text=f"Votre total est : {total:.2f} euros\n\nVous avez gagné : {incent:.2f} euros." ) 
    feedback.draw()    
    core.wait(3.5)
    #end of a trial aka 10 comparaison
    win.flip()
    core.wait(2)

try:
    win.flip()
    fin.draw()
    win.flip()
    core.wait(4)
finally:
    # Close PsychoPy properly
    print("Closing experiment properly...")
    win.close()
    core.quit()


# End of experiment
# [X]



