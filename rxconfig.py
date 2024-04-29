import reflex as rx

config = rx.Config(
    app_name="adivina_adivinador",
    cors_allow_origins=[
        "http://localhost:3000",
        "https://juego.alejocano.com",
        "https://adivina-adivinador.vercel.app"
    ],
)
