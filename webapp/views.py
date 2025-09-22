from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, JsonResponse
from django.utils import timezone
import mimetypes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from webapp.settings import RESUME_DIR

SLACK_BOT_TOKEN = 'test-token' # this token is for a dummy app

def index(request):
    #return HttpResponse('Hello, world. You're at the dictionary index.')
    #context = {'latest_question_list': latest_question_list}
    return render(request, "index.html", )

def resume(request):
    file_path = RESUME_DIR / "Greg-Dorshimer-resume.pdf"
    return FileResponse(open(file_path, 'rb'), as_attachment=False)

class SlackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(f"request received: {request.headers}")
        print(f"data: {request.data}")
        return Response({'challenge': 'GET response!'}, status = status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        client = WebClient(token = SLACK_BOT_TOKEN)
        try:
            print(f"request received: {request.headers}")
            print(f"data: {request.data}")
            payload = json.loads(request.body)
            if payload.get('type') == 'url_verification':
                return JsonResponse({"challenge": payload["challenge"]})
            
            event = payload.get("event", {})
            if payload.get('event') == 'app_home_opened':
                user_id = event.get('user_id')
                im_channel = client.conversations_open(users = [user_id])
                channel_id = im_channel['channel']['id']

                client.chat_postMessage(
                    channel = channel_id,
                    message = 'I got your app_home_opened alert.',
                    blocks = [
                                {
                                    "type": "actions",
                                    "elements": [
                                        {
                                            "type": "button",
                                            "text": {
                                                "type": "plain_text",
                                                "text": "Arctic"
                                            },
                                            "action_id": "button_arctic",
                                            "value": "arctic_clicked"
                                        }
                                    ]
                                }
                    ]
                )

                return JsonResponse({"ok": True})

        except SlackApiError as e:
            return JsonResponse({"error": str(e)}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

        # resp = {}
        # data = request.data
        # if 'event' in data.keys() and 'text' in data['event'].keys():
        #     return Response({'msg_txt_received': f"{data['event']['text']}"},
        #                     status = status.HTTP_200_OK)
        # else:
        #     challenge = data['challenge'] if 'challenge' in data.keys() else 'no challenge and no data'
        #     return Response({'challenge': f"{challenge}"},
        #                     status = status.HTTP_200_OK)
        

"""
class SendSlackIMView(APIView):
    def post(self, request, *args, **kwargs):
        slack_token = "xoxb-your-dummy-token"  # 🔁 Replace with real token
        user_id = request.data.get("user_id")

        if not user_id:
            return Response({"error": "Missing user_id in request."}, status=400)

        # Step 1: Open a direct message channel with the user
        im_open_url = "https://slack.com/api/conversations.open"
        headers = {
            "Authorization": f"Bearer {slack_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "users": user_id
        }

        im_response = requests.post(im_open_url, json=payload, headers=headers)
        im_data = im_response.json()

        if not im_data.get("ok"):
            return Response({"error": "Failed to open IM channel", "details": im_data}, status=500)

        channel_id = im_data["channel"]["id"]

        # Step 2: Post a message with Block Kit buttons
        post_message_url = "https://slack.com/api/chat.postMessage"
        message_payload = {
            "channel": channel_id,
            "text": "Choose an ocean:",  # Fallback text
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Choose an ocean:*"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Arctic",
                                "emoji": True
                            },
                            "value": "arctic_button",
                            "action_id": "arctic_action"
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Pacific",
                                "emoji": True
                            },
                            "value": "pacific_button",
                            "action_id": "pacific_action"
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Atlantic",
                                "emoji": True
                            },
                            "value": "atlantic_button",
                            "action_id": "atlantic_action"
                        }
                    ]
                }
            ]
        }

        post_response = requests.post(post_message_url, json=message_payload, headers=headers)
        post_data = post_response.json()

        if not post_data.get("ok"):
            return Response({"error": "Failed to post message", "details": post_data}, status=500)

        return Response({"message": "Slack message sent successfully"}, status=200)
"""