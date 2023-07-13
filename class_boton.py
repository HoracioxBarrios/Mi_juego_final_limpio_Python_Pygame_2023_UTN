import pygame
class Button():
	def __init__(self, image : any, pos : int, text_input : str, font : any, base_color : any, hovering_color : any)-> None:
		"""
        Crea un objeto de botón.

        Args:
            image (pygame.Surface or None): La imagen asociada al botón. 
            Puede ser None.
            pos (tuple): La posición (x, y) del botón en la pantalla.
            text_input (str): El texto que se mostrará en el botón.
            font (pygame.font.Font): La fuente de texto utilizada para 
            renderizar el texto del botón.
            base_color (tuple): El color base del texto del botón en formato RGB.
            hovering_color (tuple): El color del texto del botón cuando se 
            encuentra en estado de "hover" en formato RGB.
        Devuelve : None
        """
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font : pygame.font.Font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen : pygame.Surface)-> None:
		"""
        Actualiza y muestra el botón en la pantalla.

        Args:
            screen (pygame.Surface): La superficie de la pantalla en la que 
            se mostrará el botón.
        Devuelve : None
        """
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position : tuple)-> bool:
		"""
        Verifica si una posición dada está dentro de los límites del botón.

        Args:
            position (tuple): La posición (x, y) a verificar.

        Devuelve:
            bool: True si la posición está dentro de los límites del botón, 
            False en caso contrario.
        """
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position : tuple)-> None:
		"""
        Cambia el color del texto del botón cuando el cursor se encuentra 
        sobre él.

        Args:
            position (tuple): La posición (x, y) del cursor.
		Devuelve: None
        """
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)