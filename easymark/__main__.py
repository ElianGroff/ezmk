# USED TO MANAGER ERRORS and PRINT STATEMENTS

ORI = None
DEBUG_PRINTS = True #^m2: could add like button features for stuff like this. for peripherial/scaffolding code
RT_UPDATE = True

def mark(*args, **kwargs): # NEEDS REMADE

    if not args and not kwargs:
        print("\033[31m\nPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG\033[0m")

    global ORI

    #^ sirtiously needds remade
    if 'ori' in kwargs:
        ORI = kwargs['ori']

    if RT_UPDATE and ORI != None:
        ORI.root.update()

    if DEBUG_PRINTS:
        if 'v' in kwargs:
            match kwargs['v']:
                case 'warn':
                    print(f'\033[31m{args}\033[0m')
                case 'test':
                    print(f"\033[95m{args}\033[0m")
                case 'todo': #^ can add the other comments/another system
                    print(f"\033[38;5;214m{args}\033[0m")
                case 'green': 
                    print(f"\033[32m{args}\033[0m")
                case 'main': 
                    print(f"\033[34m{args}\033[0m")

        else:
            print(*args)



class Error:
    ...


    