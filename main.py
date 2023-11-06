import tkinter
from tkinter import *
import random

window = Tk()
window.title("Typing Speed Checker")
window.geometry("480x420")
background_color = "#05283b"
window.config(bg=background_color)
window.resizable('False','False')
time = 10



def start_game():
    text_list = [
        "The picturesque landscape was covered in a blanket of fresh snow, glistening in the morning sunlight. Snowflakes fell gently from the sky, creating a winter wonderland that filled the heart with joy and wonder. The trees stood tall and proud, their branches heavy with the weight of the snow, while children bundled up in colorful winter coats played in the soft, powdery snow. It was a scene straight out of a postcard, a sight to behold and cherish. As I walked through this enchanting scene, I couldn't help but feel a sense of peace and tranquility. The crisp, cold air invigorated my senses, and the silence was broken only by the sound of my footsteps crunching in the snow. I marveled at the beauty of nature and the magic of the season, grateful for this moment of serenity in a busy world.",
        "In a quaint little village nestled between rolling hills and a winding river, there was a charming old cottage with a thatched roof and a white picket fence. The garden surrounding the cottage was a riot of colors, with roses in full bloom, and the sweet scent of lavender in the air. Inside, the cottage was cozy and welcoming, with a crackling fireplace and vintage furniture that exuded rustic charm. The windows framed stunning views of the countryside, and the sound of birdsong filled the air. It was a place where time seemed to stand still, a haven of tranquility far removed from the hustle and bustle of the city. The cottage held a timeless charm, a place where memories were made and cherished for generations. It was a reminder that sometimes, the simple joys of life were the most precious of all.",
        "As the sun dipped below the horizon, painting the sky with hues of orange and pink, I found myself standing on the edge of a vast, untouched wilderness. The wilderness stretched out before me, a pristine and unspoiled landscape that seemed to go on forever. It was a place where the forces of nature ruled, and the only sounds were the whisper of the wind through the tall grass and the distant calls of wild animals. The air was filled with the scent of earth and adventure, and as I took a deep breath, I felt a profound sense of freedom and connection to the natural world. The wilderness was a place of raw beauty and untamed majesty, a place where one could find solitude and solace, and where the soul could roam free.",
        "High in the mountains, the air was thin and crisp, and the world seemed to stretch out endlessly in all directions. The rugged terrain was a testament to the power of geological forces, with towering peaks, deep valleys, and winding rivers. The mountains were a place of challenge and exhilaration, where every step was a test of strength and endurance. But they were also a place of breathtaking beauty, with vistas that took your breath away and left you in awe of the natural world. From the summit, I could see the world below, a patchwork of forests, lakes, and meadows. It was a reminder of the vastness of the world and the smallness of our place in it, a place of wonder and humility.",
        "In a bustling city, the streets were alive with the energy of a million lives intersecting and weaving their stories. Skyscrapers loomed overhead, their glass facades reflecting the urban chaos below. People rushed by in all directions, each with their own purpose and destination. The city was a place of dreams and aspirations, a place where fortunes were made and lost, and where the rhythm of life was fast and unrelenting. But amidst the chaos, there was a sense of opportunity and possibility, a feeling that anything was achievable. The city was a melting pot of cultures and ideas, a place where creativity thrived and innovation was born. It was a place of endless possibilities, where the future was being written with each passing moment.",
        "As the waves crashed against the shore, I stood on the beach, feeling the sand between my toes and the salt in the air. The sea stretched out before me, a vast expanse of blue that seemed to go on forever. The sound of seagulls filled the air, and the sun cast a warm glow on the water. It was a place of serenity and contemplation, a place where the worries of the world seemed to melt away with the ebb and flow of the tides. The beach was a place of solace and reflection, where one could find peace and connection to the rhythms of nature. It was a reminder of the beauty and power of the sea, a place where the soul could find respite and renewal.",
        "In a small, sleepy village, time moved at a gentle pace, and the days were marked by the rising and setting of the sun. The streets were lined with quaint cottages, their thatched roofs a testament to a bygone era. The villagers greeted each other with warm smiles and friendly waves, and life was simple and uncomplicated. The village was a place where everyone knew each other, where community and connection were cherished above all else. It was a place of tradition and history, where the old ways were preserved and passed down through generations. The village was a reminder that sometimes, the most meaningful moments in life could be found in the simplest of places.",
        "In a lush, tropical rainforest, the canopy of trees formed a verdant cathedral that blocked out the sun. The air was thick with humidity, and the sounds of wildlife filled the air. Birds with vibrant plumage flitted through the branches, and the leaves rustled with the movement of unseen creatures. The rainforest was a place of mystery and wonder, where every step revealed a new and exotic discovery. It was a place of ancient beauty, where the cycles of life played out in a dazzling display of color and diversity. The rainforest was a reminder of the fragile balance of nature and the need to protect and preserve the world's most precious ecosystems.",
        "Beneath the starry night sky, I lay on a grassy hill, gazing up at the infinite expanse of the universe. The stars twinkled like distant diamonds, and the Milky Way stretched across the heavens in a ribbon of light. The night was silent, save for the occasional chirping of crickets and the hooting of an owl in the distance. It was a moment of pure stillness and awe, a moment where the enormity of the cosmos filled my thoughts. The night sky was a canvas of wonder and mystery, a reminder of our place in the universe and the vastness of the cosmos. It was a place of introspection and contemplation, where the mysteries of the universe unfolded before my eyes.",
        "In a historic library, the shelves were lined with ancient tomes, their weathered pages filled with the knowledge and wisdom of ages past. The scent of old books filled the air, and the hushed whispers of scholars and researchers could be heard in the background. The library was a place of learning and discovery, a place where the secrets of the past were preserved for future generations. It was a place of quiet contemplation, where one could lose themselves in the pages of a book and embark on a journey through time and space. The library was a sanctuary of knowledge, a place where the thirst for understanding was quenched and the spirit of inquiry was kindled.",
    ]

    # You can access each sentence by its index, for example, sentences[0] will give you the first sentence.

    text = random.choice(text_list).lower()

    split_point = 0
    # My Text Label
    global text_label
    text_label = Label(window, text=text[0:split_point], fg="#3d3d3d", font=("Poppins", 24),bg=background_color)
    text_label.place(relx=.5, rely=.45, anchor="e")

    global write_label
    write_label = Label(window, text=text[split_point:], fg="#b7e1f7", font=("Poppins", 24),bg=background_color)
    write_label.place(relx=.5, rely=.45, anchor="w")

    # My Time Label
    global time_label
    time_label = Label(window, text=f"{time} Seconds Left", fg="white", font=("Poppins", 16),bg=background_color)
    time_label.place(relx=.5, rely=.3, anchor="center")

    # My Current Letter Label
    global letter_label
    letter_label = Label(window, text=text[split_point], fg="white", font=("Poppins", 16),bg=background_color)
    letter_label.place(relx=.5, rely=.6, anchor="center")

    global current_time
    global stillWriting
    current_time = 0
    stillWriting = True

    window.bind('<Key>', keyPress)

    window.after(1000, add_secound)
    window.after((str(time) + '000'), stop_secound)

def add_secound():
    global current_time
    current_time += 1
    time_label.configure(text=f"{time-current_time} Seconds Left")

    if stillWriting:
        window.after(1000, add_secound)

def stop_secound():
    global stillWriting
    stillWriting = False

    character = len(text_label.cget('text'))

    text_label.destroy()
    letter_label.destroy()
    write_label.destroy()
    time_label.destroy()

    print(time)
    WPM = round((character / 5) / (time / 60), 2)


    with open("highscore.txt", "r") as highscore_file:
        highscore = float(highscore_file.read())


    if WPM > highscore:
        highscore = WPM
        with open("highscore.txt", "w") as highscore_file:
            highscore_file.write(str(highscore))


    global ResultLabel
    ResultLabel = Label(window, text=f'WPM: {WPM} HS:{highscore}',font=("Poppins", 16), fg='white',bg=background_color)
    ResultLabel.place(relx=0.5, rely=0.4, anchor="center")

    global restartButton
    restartButton = Button(window, text="Restart", command=restart, fg="white", font=("Poppins", 12),
                           bg="#0e6b9e")
    restartButton.place(relx=0.5, rely=0.65, anchor="center")

    global number_scale
    number_scale = Scale(window, from_=5, to=300, orient=HORIZONTAL, length=295, fg="white", bg=background_color)
    number_scale.set(10)
    number_scale.place(relx=0.5, rely=0.5, anchor="center")

def keyPress(e):
    try:
        if e.char.lower() == write_label.cget('text')[0].lower():
            write_label.config(text=write_label.cget('text')[1:])
            text_label.config(text=text_label.cget('text') + e.char.lower())
            letter_label.config(text=write_label.cget('text')[0])

    except IndexError:
        global stillWriting
        stillWriting = False
        stop_secound()

    except tkinter.TclError:
        pass

def restart():
    ResultLabel.destroy()
    restartButton.destroy()
    global time
    time = number_scale.get()
    number_scale.destroy()
    start_game()



start_game()

window.mainloop()


