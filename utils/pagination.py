def get_pagination(offset: int, limit: int):
    return {
        "next": str(offset + limit),
        "limit": limit,
        "previous": str(offset - limit)
    }
