$config.screen_width = 1000
$config.screen_height = 600

#character list
define s = Character ('Secretary Jules', color="#c8ffc8")
define m = Character ('Me', color="#c8c8ff")
define p = Character ('Principal', color=" #ffe4c8")
define h = Character ('Mentor', color= "ffc8c8")
define a = Character ('Siam', color= "#C70039")
define b = Character ('William', color= "#FFC300")
define c = Character ('Joshua', color= "#FF5733")
define d = Character ('Sarah', color= "069400")
define e = Character ('Hanley', color= "2387CA")
define f = Character ('Charlotte', color= "#7E23CA")

label first_day:
    scene bg main_hall at truecenter
    show secretary greet main hall
    with fade
    play music "bensound-sweet.mp3"
    $save_name = "Introduction to KHA"

    s "Hi there! Are you here for the KinderHelper Academy training week?"

    m "Yes! I'm here for the KHA program."

    "I was surprised by his enthusiasm. I am very nervous coming to this program at this academy. "

    m "Is there anything I should know before I start?"

    s "Yes! My name is Mr. Jules. Welcome to the Kenton-Hines Elementary School. I am the secretary for the principal."
    s "You are going to be joining our KinderHelper Academy training program where you will test your classroom management skills"

    s "Here is your NOTEBOOK"

    show notebook
    with dissolve

    "You recieve a NOTEBOOK from Secretary Jules"

    s "This NOTEBOOK contains basic profiles for each of your students. You can update it as you learn more about your students"
    s "It will also keep track of your students' current AFFINITY for you."

    hide notebook

    s "Would you like me to explain AFFINITY?"

menu:
        "Yes":
            jump affinity_explain

        "No":
            jump intro_continue

label affinity_explain:
    scene bg main_hall at truecenter
    show secretary explain
    with fade
    show affinity_gauge at truecenter

    s "The AFFINITY GAUGE is the measure of how likely a student is willing to comply with your requests. It measures their AFFINITY for you, the teacher."
    s "It is very helpful for being able to tell how a student may respond to conflicts with their peers."

    hide affinity_gauge
    hide secretary explain
    show great_smile at truecenter
    with fade

    s "When a student's affinity is at its highest (HAPPY), it is often due to a combination of a good mood, an understanding of classroom rules, and agreement with the teacher's (your) guidance."
    s "This state is often achieved by having a rapport with the student, resolving most of the issues causing lower affinity through conversing with the student before conflicts arise,"
    s "and acknoledging the student's feelings when intervening in an conflict."

    hide great_smile
    show angry at truecenter
    with fade
    s "The gauge can go as low as an extremely confrontational ANGER. The student will more often be involved with conflicts with peers, and will require more intervention. "
    s "Just like any child, understanding why the student is so upset and advising the student on dealing with that anger can help them manage their emotions and raise their affinity level."
    s "After all, if the student feels that they can turn to you for help, they will be more accepting of your instruction and advice."

    show secretary end talk

    s "I hope that this has been helpful for you."
    s "What would you like to do now?"

label intro_continue:
    scene bg main_hall at truecenter
    show secretary greet main hall
    with wipeleft

    s "Be prepared to enlist tested classroom strategies in order to defuse situations in your classroom."
    s "What would you like to do next?"

    jump firstdayopt

label firstdayopt :
    menu firstmeet:
        "Meet the Principal":
            scene bg main_hall at truecenter
            show secretary end talk

            m "I would like to meet the principal."

            hide secretary end talk
            show secretary greet main hall

            s "Sure! I'll bring you to her office."
            hide bg main_hall
            scene bg principal office at truecenter with fade

        "Talk to Secretary Jules more":

            scene bg main_hall at truecenter
            show secretary end talk
            s "There is a lot more to learn as you start your work here"

#label meet_students :
#    $save_name = "Day 1"






#Ending
#label ending:

#    $ save_name = "Ending"

#    p "Thank you again for participating in this training week."

#    e "I hope you'll consider using Ren'Py for your next game
#       project."

    #show principal vhappy

#    e "Thanks for viewing this demo!"

#    if date:
#        e "And I'll see you on Saturday."

#    scene black with dissolve

#    "Ren'Py and the Ren'Py demo were written by PyTom."

#    'The background music is "Sun Flower Slow Drag" by S. Joplin
#     (1868-1917). Thanks to the Mutopia project for making it
#       available.'

#    'The author would like to thank everyone who makes original
#     English-language bishoujo games, and the people on the Lemmasoft forums
#     who encouraged him.'

#    "We can't wait to see what you do with this. Good luck!"

#    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
#    "It took you %(minutes)d minutes and %(seconds)d seconds to
#     finish this demo."

#    $ renpy.full_restart()
