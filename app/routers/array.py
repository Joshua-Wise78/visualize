from fastapi import APIRouter, Path, Query
from app.models.array import ArrayOperation, ArrayBase, ArrayStateResponse

router = APIRouter(prefix="/array", tags=["Array"])


@router.post("/create", status_code=201)
def create_array(config: ArrayBase):
    """Create an array using some UUID standard.

    Arguments:
        config: The base model of the array.

    Returns:
        Static Array and its unique ID identifier.
    """
    pass


@router.post("/{array_id}/insert")
def insert_value(operation: ArrayOperation, array_id: str = Path(...)):
    """Insert a value into the static array.

    Arguments:
        array_id: The id of the array for insertion.
        operation: Array operation model expectation.

    Returns:
        Modified array with new value
    """
    pass


@router.put("/{array_id}/deletion/{index}", response_model=ArrayStateResponse)
def delete_value(array_id: str = Path(...), index: int = Path(...)):
    """Delete a value from the static array.

    Arguments:
        array_id: The id of the static array
        index: the location of the value to be deleted

    Returns:
        Static Array that has been modified.
    """
    pass


@router.get("/{array_id}/contains")
def contain_value(
    array_id: str = Path(...),
    value: str = Query(..., description="Value to search for"),
):
    """Check if the value is contained inside of the array.

    Arguments:
        array_id: The unique id of the array.
        value: The value that is being checked for.

    Returns:
        True/False depending on if it is contained or not.
    """
    pass


@router.get("/{array_id}/display", response_model=ArrayStateResponse)
def display_array(array_id: str = Path(...)):
    """Display the static array nicely to the terminal

    Arguments:
        array_id: The id of said array

    Returns:
        Printout of the array
    """
    pass
