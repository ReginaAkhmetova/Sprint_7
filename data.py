class DataMessage:
    MES_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    MES_LOGIN_MISSED_DATA = "Недостаточно данных для входа"
    MES_LOGIN_ALREADY_IN_USE = "Этот логин уже используется"
    MES_CREATE_COURIER_MISSED_DATA = "Недостаточно данных для создания учетной записи"


class DataOrders:
    CREATE_ORDERS_NO_COLORS = {
        "firstName": "Котофей",
        "lastName": "Котофеев",
        "address": "проспект Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "Покатушки",
        "color": [],
    }

    CREATE_ORDERS_GREY_COLOR = {
        "firstName": "Котопес",
        "lastName": "Мультяшный",
        "address": "улица Зверей, 1",
        "metroStation": 1,
        "phone": "+7 900 000 00 00",
        "rentTime": 1,
        "deliveryDate": "2025-07-07",
        "comment": "Веселуха",
        "color": ["GREY"],
    }

    CREATE_ORDERS_BLACK_COLOR = {
        "firstName": "Солнце",
        "lastName": "Светит",
        "address": "улица Рассветная, 1",
        "metroStation": 2,
        "phone": "+7 900 111 11 11",
        "rentTime": 2,
        "deliveryDate": "2025-08-08",
        "comment": "Жжём",
        "color": ["BLACK"],
    }

    CREATE_ORDERS_TWO_COLORS = {
        "firstName": "Клубника",
        "lastName": "Спелая",
        "address": "проспект Роста, 1",
        "metroStation": 3,
        "phone": "+7 900 222 22 22",
        "rentTime": 3,
        "deliveryDate": "2025-06-26",
        "comment": "Вкуусно",
        "color": ["BLACK", "GREY"],
    }
