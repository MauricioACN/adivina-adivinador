from rxconfig import config

import reflex as rx
from adivina_adivinador.styles.styles import Spacing, Size
import adivina_adivinador.utils as utils
from adivina_adivinador.pages.how_to_play import how_to_play
from adivina_adivinador.pages.index import index
from adivina_adivinador.pages.play import play
from adivina_adivinador.pages.contact import contact
from adivina_adivinador.pages.feedback import feedback


class State(rx.State):
    """The app state."""


app = rx.App()
