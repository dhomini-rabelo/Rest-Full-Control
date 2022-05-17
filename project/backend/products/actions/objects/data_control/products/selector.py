from Core.views.data_control.handlers.selector import SelectorQueryset


product_selector = SelectorQueryset({
    "name": {
        "simple_fields": [
            "name"
        ]
    }
})