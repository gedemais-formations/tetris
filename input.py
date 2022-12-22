def read_alphachar_input(input_phrase, maxi):
    """
        This function will force the user to input a valid character
        in the console, in order to get informations from him.

        @parameters :
        - input_phrase (string) : Sentence displayed in console to ask data from user.
        - mini (integer) : The minimum valid value to input
        - maxi (integer) : The maximum valid value to input
    """

    # Infinite loop forcing user to input a correct value
    while True:
        # Input phrase that hints user for the data to input
        print('\n' + input_phrase)
        tmp = input('-> ')

        if len(tmp) != 1:
            print("\nFormat invalide. Essayez encore :")
            continue # Back to start

        if tmp.isalpha and ord(tmp.lower()[0]) >= ord(maxi):
            print("Coordonnee invalide. Essayez encore :")
            continue

        if tmp.isalpha and ord(tmp.lower()[0]) < ord(maxi):
            break # tmp value is ok, we can return it

    return tmp.lower()


def read_integer_input(input_phrase, mini, maxi):
    """
        This function will force the user to input a valid integer
        in the console, in order to get informations from him.

        @parameters :
        - input_phrase (string) : Sentence displayed in console to ask data from user.
        - mini (integer) : The minimum valid value to input
        - maxi (integer) : The maximum valid value to input
    """

    # Infinite loop forcing user to input a correct value
    while True:
        # Input phrase that hints user for the data to input
        print('\n' + input_phrase)
        try:
            tmp = int(input('-> '))
        except:
            print("\nFormat invalide. Essayez encore :")
            continue # Back to start

        if tmp >= mini and tmp <= maxi:
            break # tmp value is ok, we can return it

        # If it is a range problem, we display the adapted error message :
        print("\nMerci d'entrer un nombre entre {0} et {1} :".format(mini, maxi))

    return tmp

