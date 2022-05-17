from Core.views.data_control.handlers.filter import FilterForQueryset


product_filter = FilterForQueryset({
    'name': 'name__startswith',
    'price_gte': 'current_price__gte',
    'price_lte': 'current_price__lte',
    'promotion_price_gte': 'promotion_price__gte',
    'promotion_price_lte': 'promotion_price__lte',
    'not_has_promotion': 'promotion_price__isnull',
    'cashback_value_gte': 'cashback_value__gte',
    'cashback_value_lte': 'cashback_value__lte',
    'cashback_is_percent': 'cashback_is_percent',
    'not_has_cashback': 'cashback_value__isnull',
    'company': 'company__name__startswith',
    'category': 'categories__name__iexact',
    'coupon': 'coupons__name__iexact',
    'feedbacks': 'feedbacks__user__id',
    'ratings': 'ratings__user__id',
}, models = {
    "promotion": [
        {
            "not_has_promotion": False
        }
    ],
    "cashback": [
        {
            "not_has_cashback": False
        }
    ],
    "promotion_or_cashback": [
        {
            "not_has_promotion": False
        },
        {
            "not_has_cashback": False
        }
    ],
    "promotion_and_cashback": [
        {
            "not_has_promotion": False,
            "not_has_cashback": False
        }
    ],
    "price_gte_3000": [
        {
            "price_gte": 3000
        },
        {
            "promotion_price_gte": 3000
        }
    ],
    "cashback_gte_10": [
        {
            "cashback_value_gte": 10,
            "cashback_is_percent": True
        }
    ]
})