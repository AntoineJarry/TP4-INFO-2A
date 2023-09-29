from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService


class PokemonDetailsView(AbstractView):
    def __init__(self, pokemon):
        self.__pokemon = pokemon
