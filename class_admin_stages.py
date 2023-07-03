from class_Stage import StagePadre
from levels.class_stage_1 import Stage_1
from levels.class_stage_2 import Stage_2
from levels.class_stage_3 import Stage_3


class AdminStages:
    def __init__(self, screen) -> None:
        '''
        self.screen_slave es la screen donde se va a abrir
        self.stages : guardamos las referecia al constructor de las clases stages
        '''
        self.screen_slave = screen
        self.stages = {"stage_uno" : Stage_1 , "stage_dos" : Stage_2, "stage_tres" : Stage_3}

    
    def get_stage(self, nombre_stage : str):
        '''
        obtiene el nombre del stage
        recibe : el nombre del stage
        devuelve: accede al elemento del diccionario y le pasa como
        argumento la screen. esto mismo eslo que retorna
        '''
        return self.stages[nombre_stage](self.screen_slave)
        