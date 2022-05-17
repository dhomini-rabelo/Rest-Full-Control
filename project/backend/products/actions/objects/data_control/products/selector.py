from Core.views.data_control.handlers.selector import SelectorForQueryset


product_selector = SelectorForQueryset({
    "name": {
        "simple_fields": [
            "name"
        ]
    }
})