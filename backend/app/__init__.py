import os
from app.sgs import SGS


class Welcome:
    """Welcome user"""
    def __init__(self):

        self.ruta = os.getcwd()

        SGS(self.ruta)
