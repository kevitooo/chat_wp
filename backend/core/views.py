import json
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from .responses import RESPONSE_CONFIG

WHATSAPP_API_URL = "https://graph.facebook.com/v22.0/860336800492074/messages"
WHATSAPP_API_TOKEN = "Bearer EAAhdWZCYLDwIBPsCe0WPg573EDb3HEBgRwF9gOiMjZBTuuJm6KvYQN6SSVJAOiHL4jp4JasiYrfOSQz6FeAHOwZCZAGmMt7EiwwhGoEgVZBxy0ia4nZAOfgNJJKuArK0TlXS4zUm5BeeOAhopxSpLxk0aS2ywRKdOE7amGwFZBJfpqJVmO0cHbNgFkE5LLj0N1r6dHIjlXbWgm9XLFt6msGLC0FZBtnZA1bMlVOZCm3lzLLwZDZD"
VERIFY_TOKEN = "mi_token_secreto_2025"
HUMAN_AGENT_NUMBER = ""


@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            for entry in data.get("entry", []):
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    messages = value.get("messages", [])
                    for msg in messages:
                        if msg.get("type") == "interactive":
                            interactive = msg.get("interactive", {})
                            reply_id = None

                            if interactive.get("type") == "list_reply":
                                reply_id = interactive["list_reply"]["id"]
                            elif interactive.get("type") == "button_reply":
                                reply_id = interactive["button_reply"]["id"]

                            if reply_id:
                                user_id = msg["from"]
                                response = process_user_choice(reply_id, user_id)
                                if response:
                                    send_whatsapp_message(response, user_id)
            return HttpResponse(status=200)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

    elif request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)
        return HttpResponse(status=403)


def process_user_choice(reply_id, user_id):
    config = RESPONSE_CONFIG.get(reply_id)

    if config:
        return config["payload"](user_id)
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

    headers = {
        "Authorization": WHATSAPP_API_TOKEN,
        "Content-Type": "application/json",
    }
    payload["to"] = to

    try:
        response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Message sent successfully to {to}: {response.status_code}")

        if payload.get("notify_agent"):
            notify_human_agent(payload["user_id"])

    except requests.RequestException as e:
        print(f"Failed to send message to {to}: {e}")


def notify_human_agent(user_id):
    notification_payload = {
        "messaging_product": "whatsapp",
        "to": HUMAN_AGENT_NUMBER,
        "type": "text",
        "text": {
            "body": f"Un usuario ({user_id}) ha solicitado hablar con un agente humano. Por favor, contáctalo."
        },
    }

    headers = {
        "Authorization": WHATSAPP_API_TOKEN,
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            WHATSAPP_API_URL, json=notification_payload, headers=headers
        )
        response.raise_for_status()
        print(f"Human agent notified succesfully: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to notify human agent: {e}")
