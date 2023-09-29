from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        pokemon_service = PokemonService()
        pokemon_list = pokemon_service.get_pokemon_from_webservice(limit=30)

        self.__questions = [
            {
                "type": "list",
                "message": "Select Pokemon",
                "choices": pokemon_list.name,
            },
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}")

    def make_choice(self):
        answers = prompt(self.__questions)

        another_pokemon = prompt(
            [
                {
                    "type": "confirm",
                    "name": "continue",
                    "message": "Detail another pokemon ?",
                    "default": True,
                }
            ]
        )

        if another_pokemon["continue"]:
            return PokemonListView()

        else:
            from view.start_view import StartView

            return StartView()
