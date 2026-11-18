from app.megaverse_repository import MegaVerseRepository
from app.megaverse_service import MegaVerseService
from app.polyanet_strategy import PolyanetStrategy
from app.soloon_strategy import SoloonStrategy
from app.cometh_strategy import ComethStrategy
from app.base_element_strategy import BaseElementStrategy
from app.models.input_element import CreateElement, CreateElementRequest, EraseElement



# strategies: list[BaseElementStrategy] = [
#     PolyanetStrategy(),
#     SoloonStrategy(),
#     ComethStrategy()
# ]

# new_element = CreateElement(
#     row="2",
#     column="3",
#     candidate_id="123"
# )


# for strategies in strategies:
#     strategies.create(new_element)


repository = MegaVerseRepository()
service = MegaVerseService(repository)

# element_1 = CreateElementRequest(
#     row="2",
#     column="3",
#     candidate_id="123",
#     element="RED_SOLOON"
#     )
    
# element_2 = CreateElementRequest(
#     row="2",
#     column="3",
#     candidate_id="123",
#     element="UP_COMETH"
#     )

# repository.create_element(element_1)
# repository.create_element(element_2)

# service.solve_map(1,[
#     ["POLYANET", "SPACE", "SPACE"],
#     ["SPACE", "RIGHT_COMETH", "SPACE"],
#     ["SPACE", "SPACE", "PURPLE_SOLOON"]
#   ])

service.erase_map(1,{
    "map": {
        "content": [
            [{"type": 0}, None],
            [None, {"type": 1, "color": "red"}]
        ]
    }
})