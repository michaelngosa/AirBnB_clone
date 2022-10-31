#!/usr/bin/python3
"""includes State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """temp"""

    name = ""

    def __init__(self, *args, **kwargs):
        """
        init
        """
        super().__init__(*args, **kwargs)
