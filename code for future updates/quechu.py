import pygame, sys,os,pdb
pygame.init()
def write_to_file(file_name, your_name, points):
    score_file = open(file_name, 'a')
    print (your_name+",", points, file=score_file)
    score_file.close()
def top10(screen, file_name):
   
    file = open(file_name, 'r')
    lines=file.readlines()
       
    all_score = []
    for line in lines:
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep+1:-1])
        all_score.append((score, name))
    file.close()
    all_score.sort(reverse=True)  # sort from largest to smallest
    best = all_score[:10]  # top 10 values
def enterbox(screen, txt):
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # enter/return key
                    return name
                elif inkey == 8:  # backspace key
                    name = name[:-1]
                elif inkey <= 300:
                    if 122 >= inkey >= 97:
                        inkey -= 32  # handles CAPITAL input
                    name += chr(inkey)
