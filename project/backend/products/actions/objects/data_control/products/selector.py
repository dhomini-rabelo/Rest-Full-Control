from Core.views.data_control.handlers.selector import SelectorForQueryset


product_selector = SelectorForQueryset({
    "list": {
        "fields": [
            "name",
            "current_price",
            "promotion_price",
            "cashback_value",
            "cashback_is_percent",
            "ratings",
            "categories",
        ],
        "relationship_fields": {
            "ratings": [
                "value",
            ],
            "categories": [
                "name"
            ]
        }
    },
    "details": {
        "fields": [
            "name",
            "description",
            "current_price",
            "promotion_price",
            "cashback_value",
            "cashback_is_percent",
            "company",
            "feedbacks",
            "ratings"
        ],
        "relationship_fields": {
            "ratings": [
                "value",
            ]
        }
    },
    "on_sale": {
        "fields": [
            "name",
            "current_price",
            "promotion_price",
            "cashback_value",
            "cashback_is_percent",
            "coupons"
        ],
        "relationship_fields": {
            "coupons": [
                "name",
                "value",
                "is_percent"
            ]
        }
    },
})