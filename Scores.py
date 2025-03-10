import json



def openfile():
    with open('./Scores.json') as file:
        scoresdict = json.load(file)
    return scoresdict

def closefile(scoresdict):
    json_object = json.dumps(scoresdict, indent=4)

    with open("Scores.json", "w") as outfile:
        outfile.write(json_object)


def write(equipe, level, score):
    scoresdict = openfile()
    equipe_name = f'equipe{equipe}'
    if equipe_name not in scoresdict.keys():
        scoresdict[equipe_name] = {}
        scoresdict[equipe_name][f'{level}'] = score
    elif f'{level}' not in scoresdict[equipe_name].keys():
        scoresdict[equipe_name][f'{level}'] = score
    else:
        old_score = scoresdict[equipe_name][f'{level}']
        if old_score < score:
            scoresdict[equipe_name][f'{level}'] = score
    closefile(scoresdict)

def read(equipe, level='all'):
    scoresdict = openfile()
    if level != 'all':
        if f'equipe{equipe}' in scoresdict.keys():
            if f'{level}' in scoresdict[f'equipe{equipe}'].keys():
                return scoresdict[f'equipe{equipe}'][f'{level}']
        return 0
    else:
        score_tot = 0
        for key in scoresdict[f'equipe{equipe}'].keys():
            score_tot += scoresdict[f'equipe{equipe}'][key]
        return score_tot

def reset():
    openfile()
    closefile({})

# reset()