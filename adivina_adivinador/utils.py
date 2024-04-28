import reflex as rx


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview = "https://media.idownloadblog.com/wp-content/uploads/2022/04/Preview-Pixelmator-Mac.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    # {"name": "twitter:site", "content": "@mouredev"}
]

# Index

index_title = "Jugo | Juego de adivinar la palabra"
index_description = "Juego de adivinar la palabra con descripción y pistas."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# How to play
how_to_play_title = "Cómo jugar | Juego de adivinar la palabra"
how_to_play_description = "Instrucciones para jugar al juego de adivinar la palabra."

how_to_play_meta = [
    {"name": "og:title", "content": how_to_play_title},
    {"name": "og:description", "content": how_to_play_description},
]

how_to_play_meta.extend(_meta)


# Play
play_title = "Jugar | Juego de adivinar la palabra"
play_description = "Juego de adivinar la palabra."

play_meta = [
    {"name": "og:title", "content": play_title},
    {"name": "og:description", "content": play_description},
]

play_meta.extend(_meta)

# Contact

contact_title = "Contacto | Juego de adivinar la palabra"
contact_description = "Contacta con el equipo de Jugo."

contact_meta = [
    {"name": "og:title", "content": contact_title},
    {"name": "og:description", "content": contact_description},
]

contact_meta.extend(_meta)

# Feedback

feedback_title = "Feedback | Juego de adivinar la palabra"
feedback_description = "Envía tus comentarios y sugerencias sobre Jugo."

feedback_meta = [
    {"name": "og:title", "content": feedback_title},
    {"name": "og:description", "content": feedback_description},
]

feedback_meta.extend(_meta)
