from api.database.entity import Entity


def comp_equals_filter_clause(model: Entity, filters: dict):
    
    return [
        getattr(model, field, None) == value
        for field, value in filters.items()
        if getattr(model, field, None) is not None
    ]
