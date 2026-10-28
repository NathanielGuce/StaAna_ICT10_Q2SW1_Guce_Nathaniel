from pyscript import document, display

def checkbutton(e):
    club_members = ['skibidi', 'sigma', 'pogi', 'gamer', 'chad', 'alpha', 'bruh', 'epic', 'cool', 'funny', 'awesome', 'legendary', 'meme', 'dank', 'savage', 'lit', 'hype', 'swag', 'dope', 'radical', 'tubular', 'gnarly', 'bodacious', 'rad', 'wicked', 'sick', 'epic gamer', 'candidate name', 'epic gamer', 'bruh moment', 'chad energy', 'sigma male', 'alpha male', 'beta male', 'omega male', 'giga chad', 'epic gamer moment', 'bruh moment', 'chad energy', 'sigma male', 'alpha male', 'beta male', 'omega male', 'giga chad', 'epic gamer moment', 'bruh moment', 'chad energy', 'sigma male', 'alpha male', 'beta male', 'omega male', 'giga chad', 'epic gamer moment', 'bruh moment', 'chad energy', 'sigma male', 'alpha male', 'beta male', 'omega male', 'giga chad', 'epic gamer moment',]
    candidate_name = document.getElementById("candidateName").value
    candidate_checker = candidate_name.lower() in club_members

    result = (f'wow you, {candidate_name}, is a member of the club!', f'aww you, {candidate_name}, is not a member of the club!')

    display(result[candidate_checker], target="result_checker")