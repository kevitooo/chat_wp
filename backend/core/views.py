import json
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                messages = value.get("messages", [])
                for msg in messages:
                    if msg.get("type") == "interactive":
                        interactive = msg.get("interactive", {})
                        if interactive.get("type") == "list_reply":
                            reply_id = interactive["list_reply"]["id"]
                            user_id = msg["from"]
                            
                            response = process_user_choice(reply_id, user_id)
                            send_whatsapp_message(response, user_id)

        return HttpResponse(status=200)
    elif request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode and token == "mi_token_secreto_2025":
            return HttpResponse(challenge)
        return HttpResponse(status=403)


def process_user_choice(reply_id, user_id):
    if reply_id == "caladores_de_mano":
        return {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Óptimas opciones de facturación, planes y trámites. ¿Qué necesitas? Responde 1 para facturación, 2 para planes."
            },
        }
    elif reply_id == "caladores_hidraulicos":
        return {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Puedes contratar línea móvil, internet o TV. ¿Cuál te interesa? Responde con el nombre."
            },
        }
    else:
        return {
            "messaging_product": "whatsapp",
            "to": user_id,
            "type": "text",
            "text": {
                "body": "Opción no reconocida. Por favor, selecciona una opción válida."
            },
        }


def send_whatsapp_message(payload, to):
    if to.startswith("549"):
        to = "54" + to[3:].replace("9", "0", 1)

    url = "https://graph.facebook.com/v22.0/860336800492074/messages"
    headers = {
        "Authorization": "Bearer EAAhdWZCYLDwIBPmV9HZApws1Ij3Umq1ZCn9IKzHZB2ZA66lvGN7ZCvDMUrZAkzReXoSD31fyblNFbvvoJJvBe1nOzczAtRDqSPDi1sRqxSWXcXTiSB1fZBHHaP5bZCWdsM5CEGzngbWLHGFXZCEUW0RPJQcdE2dwfMvpa3TDZAT18ONK5yf5ix66reJlYF1cR6b73ZAV8ZCYHyAZAFlLxpvAtbabzlXBBukYZA6C3kCZAYSOkVDrk4QZD",
        "Content-Type": "application/json",
    }
    payload["to"] = to

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
