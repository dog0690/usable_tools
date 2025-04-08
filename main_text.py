import random
day_catagory = ['chill', 'coding', 'design']
chill_catagory = ['play games','watch movie', 'go outside']
code_catagory = ['api practice', 'ai practice', 'website practice']
design_catagory = ['newsletter', 'instagram post', 'instagram reels']



def daypicker():
    chosen_day = random.choice(day_catagory)
    return(str(chosen_day))

def activity(chosen_day):
    if chosen_day == 'chill':
        chosen_activity = random.choice(chill_catagory)
    elif chosen_day == 'coding':
        chosen_activity = random.choice(code_catagory)
    else:
        chosen_activity = random.choice(design_catagory)
    return(chosen_activity)
print(daypicker(), activity(daypicker))