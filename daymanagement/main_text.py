import random
day_catagory = ['chill', 'coding', 'design']
chill_catagory = ['play games','watch movie', 'go outside']
code_catagory = ['api practice', 'fundamental practice', 'website practice']
design_catagory = ['Minecraft Design', 'Canva Design', 'Figma Design']



def daypicker():
    chosen_day = random.choice(day_catagory)
    return(str(chosen_day))
def research(activity):
    if activity != 'chill_catagory':
        choice = random.random()
        study = True
        if choice > .5:
            return "research"
        else:
            study = False
            return "preform"
def activity(chosen_day):
    if chosen_day == 'chill':
        chosen_activity = random.choice(chill_catagory)
    elif chosen_day == 'coding':
        chosen_activity = random.choice(code_catagory)
    else:
        chosen_activity = random.choice(design_catagory)
    return(chosen_activity)


def main():
    day = daypicker()
    day_activity = activity(day)
    study = research(day)
    print(f'{day}, {day_activity}, {study}')

main()