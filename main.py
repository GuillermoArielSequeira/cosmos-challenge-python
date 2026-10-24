from app.polyanet_strategy import PolyanetStrategy
from app.soloon_strategy import SoloonStrategy
from app.cometh_strategy import ComethStrategy
from app.base_element_strategy import BaseElementStrategy
from app.models.input_element import CreateElement, EraseElement



strategies: list[BaseElementStrategy] = [
    PolyanetStrategy(),
    SoloonStrategy(),
    ComethStrategy()
]

new_element = CreateElement(
    row="2",
    column="3",
    candidate_id="123"
)


for strategies in strategies:
    strategies.create(new_element)