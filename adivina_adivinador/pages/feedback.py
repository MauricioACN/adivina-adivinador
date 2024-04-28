import reflex as rx
from adivina_adivinador.routes import Route
import adivina_adivinador.utils as utils


@rx.page(
    route=Route.FEEDBACK.value,
    title=utils.feedback_title,
    description=utils.feedback_description,
    image=utils.preview,
    meta=utils.feedback_meta
)
def feedback() -> rx.Component:
    return rx.box(
        rx.heading("feedback")
    )
