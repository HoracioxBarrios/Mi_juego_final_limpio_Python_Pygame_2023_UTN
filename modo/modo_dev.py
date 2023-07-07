DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG
    
def get_modo():
    return DEBUG
    
