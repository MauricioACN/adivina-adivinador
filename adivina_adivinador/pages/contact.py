import reflex as rx
from adivina_adivinador.routes import Route
import adivina_adivinador.utils as utils


@rx.page(
    route=Route.CONTACT.value,
    title=utils.contact_title,
    description=utils.contact_description,
    image=utils.preview,
    meta=utils.contact_meta
)
def contact() -> rx.Component:
    return rx.box(
        rx.heading("contact")
    )
