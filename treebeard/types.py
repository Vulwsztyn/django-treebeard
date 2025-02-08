from typing import Annotated
from annotated_types import Gt, Le, Len, Ge

PositiveInt = Annotated[int, Gt(0)]
NonNegativeInt = Annotated[int, Ge(0)]
RadixInt = Annotated[
    int, Gt(1), Le(85)]

Char = Annotated[str, Len(1,1)]
