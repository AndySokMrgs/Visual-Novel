# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The thing that makes the game start

label start:


    # This is the backgound repository

    scene bg mist

    scene bg white

    # This is the character repository

    define g = Character('Ghost', )

#------------------------------------------------------------------------------

#Game and story starts here.

    show bg mist
    with fade

    "A misty figure shows up in the middle of no where."

    show ghost
    with fade

    # These display lines of dialogue.

    "You have no clue on where you are..."

    "....."

    "....."

    "You" "The last thing 'YOU' remember was watching your favorite show Girls
    Panzer..."

    g "Well Looks like you are almost at your destination."

    g "Welp... Looks like you are about to-"

    hide ghost

    hide bg mist

    show bg white

    "....."

    "....."

    "....."

    "You" "Welp... Looks like my old life is gone..."

    "....."



    # This ends the game.

    return
