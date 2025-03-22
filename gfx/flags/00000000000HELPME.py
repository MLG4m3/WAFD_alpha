import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Map numbers to their corresponding text
    text_map = {
        0: """ Hello ! This program used as a tutorial for WAFD Flag Tools, wich program do you need help with ? :
 For the Copytool, type 1
 For the Copytool Unique, type 2
 For the Downsizer, type 3
 For the All-Downsizer, type 4
 For the Occurence Renamer, type 5
 """,
        1: """
 THE COPYTOOL
 ------------

 The Copytool is used for creating flag templates for all eight ideologies present in the mod,
this is recommended for countries who have numerous paths or outcomes

 For example, if you type AZR, it will create 8 .tga files :
AZR_AN AZR_ML, AZR_RS, AZR_PL, AZR_CL, AZR_AC, AZR_NA and AZR_NF

 It allows you to design the flags without having to copy paste
the placeholders and rename everything multiple times

 There is a variant of this tool, Copytool Unique (2)
""",
        2: """
 THE COPYTOOL UNIQUE
 -------------------

 The Copytool Unique is a variant of the Copytool (1), unlike the original, this version
only creates only one flag, recommended for smaller nations who don't have path for every ideology

 For example, if you type GEO, it will create a file named GEO.tga

 It allows you to not waste time creating unusued design for a country that cannot
even switch to other ideologies

 However if the nation has only few different ideology paths, let's say a Neofascist and a
Marxist-Leninist path, then you can type GEO_NF and GEO_ML, it will work too
""",
        3: """
 THE DOWNSIZER
 -------------

 The Downsizer is used for generating smaller version of flags for all eight ideologies present in the mod,
this is recommended for countries who have numerous paths or outcomes

 For example, if you type AZR, it will create 8 .tga files :
AZR_AN AZR_ML, AZR_RS, AZR_PL, AZR_CL, AZR_AC, AZR_NA and AZR_NF

 It allows you to design the flags without having to copy paste
the placeholders and rename everything multiple times

 There is a variant of this tool, Copytool Unique (2)
""",
        4: """*text four*""",
        5: """
 THE COPYTOOL
 ------------

 The Copytool is used for creating flag templates for all eight ideologies present in the mod,
this is recommended for countries who have numerous paths or outcomes

 For example, if you type AZR, it will create 8 files :
AZR_AN AZR_ML, AZR_RS, AZR_PL, AZR_CL, AZR_AC, AZR_NA and AZR_NF

 It allows you to design the flags without having to copy paste
the placeholders and rename everything multiple times

 There is a variant of this tool called "Copytool Unique" (2)
"""
    }

    # Initial text
    current_text = text_map[0]
    print(current_text)

    while True:
        # Get user input
        user_input = input("Enter a number or type EXIT to quit: ").strip().upper()

        # Check if the user wants to exit
        if user_input == "EXIT":
            print("Exiting the program...")
            break

        # Validate the input
        if user_input.isdigit() and 1 <= int(user_input) <= 5:
            # Clear the screen
            clear_screen()
            # Update the text based on the input
            current_text = text_map[int(user_input)]
            print(current_text)
        else:
            # Clear the screen and show an error message
            clear_screen()
            print(current_text)  # Re-display the current text
            print("Invalid input. Please enter a number between 1 and 5 or type EXIT to quit.")

if __name__ == "__main__":
    main()