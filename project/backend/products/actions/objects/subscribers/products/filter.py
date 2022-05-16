from Core.views.data_control.handlers.filter import FilterSubscriber


product_filter_subscriber = FilterSubscriber({
    'name': 'name__startswith',
    'price_gte': 'current_price__gte',
    'price_lte': 'current_price__lte',
    'promotion_price_gte': 'promotion_price__gte',
    'promotion_price_lte': 'promotion_price__lte',
    'not_has_promotion': 'promotion_price__isnull',
    'cashback_value_gte': 'cashback_value__gte',
    'cashback_value_lte': 'cashback_value__lte',
    'not_has_cashback': 'cashback_value__isnull',
    'company': 'company__name__startswith',
    'category': 'categories__name__iexact',
    'coupon': 'coupons__name__iexact',
    'feedbacks': 'feedbacks__user__id',
    'ratings': 'ratings__user__id',
})