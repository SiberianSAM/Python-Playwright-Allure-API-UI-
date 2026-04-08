

PRODUCT_SCHEMA = {
    "type": "object",
    "required": [
        "id", "name", "description", "price", "is_location_offer",
        "is_rental", "co2_rating", "in_stock", "is_eco_friendly",
        "product_image", "category", "brand"
    ],
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "price": {"type": "number", "minimum": 0},
        "is_location_offer": {"type": "boolean"},
        "is_rental": {"type": "boolean"},
        "co2_rating": {
            "type": "string",
            "enum": ["A", "B", "C", "D", "E", "F", "G"]
        },
        "in_stock": {"type": "integer"},
        "is_eco_friendly": {"type": "boolean"},

        "product_image": {
            "type": "object",
            "required": ["id", "by_name", "by_url", "file_name"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string"},
                "by_name": {"type": "string"},
                "by_url": {"type": "string", "format": "uri"},
                "source_name": {"type": "string"},
                "source_url": {"type": "string", "format": "uri"},
                "file_name": {"type": "string"},
                "title": {"type": "string"}
            }
        },

        "category": {
            "type": "object",
            "required": ["id", "name", "slug"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "slug": {"type": "string"},
                "parent_id": {"type": ["string", "null"]}
            }
        },

        "brand": {
            "type": "object",
            "required": ["id", "name"],
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"}
            }
        }
    }
}
