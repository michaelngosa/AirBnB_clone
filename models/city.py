#!/usr/bin/python3

"""contains City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """temp"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
            """
            init
            """
            super().__init__(*args, **kwargs)
