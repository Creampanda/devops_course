info_responses = {
    200: {
        "description": "Service information",
        "content": {
            "application/json": {"example": {"version": "1.0.0", "service": "currency", "author": "a.karaulov"}}
        },
    }
}

currency_responses = {
    200: {
        "description": "Currency information",
        "content": {"application/json": {"example": {"service": "currency", "data": {"USD": 33.4013}}}},
    }
}
