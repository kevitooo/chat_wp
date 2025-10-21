RESPONSE_CONFIG = {
    # region Caladores de mano
    "caladores_manuales": {
        "type": "interactive",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "interactive",
            "interactive": {
                "type": "list",
                # "header": {"type": "text", "text": "Caladores Manuales"},
                "body": {
                    "text": "Los caladores manuales de Tornomar están diseñados para cumplir con los más altos estándares de calidad, garantizando precisión y durabilidad. Contamos con una variedad de modelos adaptables a cada necesidad, considerando el tipo de trabajo, la composición del suelo y el presupuesto."
                },
                "action": {
                    "button": "Ver opciones",
                    "sections": [
                        {
                            "title": "Caladores Manuales",
                            "rows": [
                                {
                                    "id": "modelos",
                                    "title": "Modelos",
                                    "description": "Pedir cotización, ver detalles, confirmar pedido y más.",
                                },
                                {
                                    "id": "pedir_cotizacion",
                                    "title": "Pedir cotización",
                                    "description": "Confirmar pedido, datos de envío y más.",
                                },
                                {
                                    "id": "descargar_catalogo",
                                    "title": "Descargar catálogo",
                                    "description": "Archivo pdf con el catálogo completo.",
                                },
                                {
                                    "id": "precios",
                                    "title": "Precios",
                                    "description": "Precios de caladores manuales",
                                },
                            ],
                        }
                    ],
                },
            },
        },
    },
    "modelos": {
        "type": "interactive",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "interactive",
            "interactive": {
                "type": "list",
                # "header": {"type": "text", "text": "Modelos"},
                "body": {"text": "Selecciona el modelo para ver más detalles:"},
                "footer": {"text": "Tornomar - Caladores"},
                "action": {
                    "button": "Ver Modelos",
                    "sections": [
                        {
                            "title": "Modelos Principales",
                            "rows": [
                                {
                                    "id": "pico_pato",
                                    "title": "Pico Pato (PP)",
                                    "description": "Descarga Rápida para Análisis Químico en Suelos Pesados",
                                },
                                {
                                    "id": "sr20_sr30",
                                    "title": "SR20-SR30 - Equipo Prolongable",
                                    "description": "Robustez y Profundidad en Cada Muestra",
                                },
                                {
                                    "id": "e20_e30",
                                    "title": "E20-E30 - Equipo Entero",
                                    "description": "Robustez y Precisión en Cada Muestra",
                                },
                                {
                                    "id": "m20_m30",
                                    "title": "M20-M30 - Equipo Desarmable",
                                    "description": "Practicidad y Precisión en Cada Muestra",
                                },
                                {
                                    "id": "st20",
                                    "title": "ST20 - Modelo Estándar",
                                    "description": "Ligereza y Precisión para Muestreo de Suelos",
                                },
                            ],
                        },
                        # {
                        #     "title": "Equipos Especializados",
                        #     "rows": [
                        #         {
                        #             "id": "t20",
                        #             "title": "T20 - Equipo con Tachito",
                        #             "description": "Muestreo Compuesto para Diagnóstico de Fertilidad",
                        #         },
                        #         {
                        #             "id": "martillo_csp",
                        #             "title": "Martillo CSP",
                        #             "description": "Golpes eficientes y protección duradera",
                        #         },
                        #         {
                        #             "id": "pi20_p30",
                        #             "title": "PI20-P30 - Calador Manual para Estudios de Agua Útil",
                        #             "description": "Durabilidad y precisión para extracciones de profundidad",
                        #         },
                        #         {
                        #             "id": "d63",
                        #             "title": "D63 - Muestreador de Densidad Aparente (DAP)",
                        #             "description": "Para medición precisa de la densidad del suelo",
                        #         },
                        #         {
                        #             "id": "td",
                        #             "title": "Testeador de Dureza (TD)",
                        #             "description": "Precisión y calidad en la evaluación de capas limitantes",
                        #         },
                        #     ],
                        # },
                        # {
                        #     "title": "Accesorios",
                        #     "rows": [
                        #         {
                        #             "id": "helicoidal",
                        #             "title": "Helicoidal (H1)",
                        #             "description": "Penetración eficiente en suelos difíciles",
                        #         },
                        #         {
                        #             "id": "accesorio_h1",
                        #             "title": "Accesorio Helicoidal H1",
                        #             "description": "Accesorio H1",
                        #         },
                        #     ],
                        # },
                    ],
                },
            },
        },
    },
    "pico_pato": {
        "type": "interactive",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": user_id,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "header": {
                    "type": "image",
                    "image": {
                        "link": "https://tornomar.com/wp-content/uploads/2025/03/FOTO-9-2-scaled.png"
                    },
                },
                "body": {
                    "text": "El Pico Pato (PP) es un calador manual ideal para análisis químico en suelos pesados, capaz de obtener muestras de 20 cm de profundidad. Su sistema de apertura rápida permite que la muestra se desprenda fácilmente, y su diseño con pie de apoyo facilita la penetración en suelos duros. Construido con acero inoxidable AISI 304, ofrece la durabilidad y calidad necesarias para el muestreo intensivo."
                },
                "footer": {"text": "Pico Pato (PP)"},
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "pico_pato_pedir_cotizacion",
                                "title": "Pedir cotización",
                            },
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "modelos",
                                "title": "Volver",
                            },
                        },
                    ]
                },
            },
        },
    },
    "sr20_sr30": {
        "type": "interactive",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": user_id,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "header": {
                    "type": "image",
                    "image": {
                        "link": "https://tornomar.com/wp-content/uploads/2025/03/SR30.png"
                    },
                },
                "body": {
                    "text": "El SR20-SR30 es un calador manual diseñado para obtener muestras de 20 y 30 cm por toma, con la posibilidad de alcanzar hasta 2 metros de profundidad mediante prolongaciones. Su construcción robusta y materiales de alta calidad lo convierten en una herramienta confiable para muestreo en suelos duros y exigentes."
                },
                "footer": {"text": "SR20-SR30 - Equipo Prolongable"},
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "sr20_sr30_pedir_cotizacion",
                                "title": "Pedir cotización",
                            },
                        }
                    ]
                },
            },
        },
    },
    "pedir_cotizacion": {
        "type": "text",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Perfecto. Para generar una cotización, por favor, indícame qué modelo te interesa o qué tipo de trabajo necesitas realizar."
            },
        },
    },
    "descargar_catalogo": {
        "type": "document",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "document",
            "document": {
                "id": "24679026485053834",
                "caption": "Le comparto nuestro catálogo para que pueda ver todos los productos disponibles.",
                "filename": "Catalogo-Caladores-Tornomar.pdf",
            },
        },
    },
    "precios": {
        "type": "text",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Los precios no incluyen IVA, Tipo de cambio 💵 Dolar Venta Billete BNA, Los precios no incluyen gastos de envios."
            },
        },
    },
    # region Calador automático
    "calador_automatico_ch200": {
        "type": "text",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Puedes contratar línea móvil, internet o TV. ¿Cuál te interesa? Responde con el nombre."
            },
        },
    },
    "contacto_humano": {
        "type": "text",
        "payload": lambda user_id: {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "¡Entendido! Un agente de ventas se pondrá en contacto contigo lo antes posible. Gracias por tu paciencia."
            },
            "notify_agent": True,
            "user_id": user_id,
        },
    },
}
