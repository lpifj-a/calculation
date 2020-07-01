from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

import matplotlib.pyplot as plt
from sympy import *
# 軽量なウェブアプリケーションフレームワーク:Flask
app = Flask(__name__)


#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    if text == "？":
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=data+"(https://dictionary.goo.ne.jp/word/"+data+")"))

    elif text == "なんでやねん！":
        file = open(event.source.user_id[:4] +".txt","r")
        data = file.read()
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "すみません、「"+data+"」と間違えました",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="詳しく",data="詳しく")
                        ),
                        QuickReplyButton(
                            action=PostbackAction(label="OK",data="OK")
                        ),
                    ])))
    else :
        q1 = text
        q3 = 0
        count = 0
        while(q3==0):
            q2 = change(q1)
            q3 = scrape(q2)
            count += 1
            if(count > 10):
                if(scrape(q1)):
                    q3 = scrape(q1)
                else:
                    q3 = "わかりません"
                q2 = q1
                break
        file = open(event.source.user_id[:4] +".txt","w")
        file.write(q2)
        file.close()
        if q3 == "わかりません":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = q3,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="OK",data="OK")
                            ),
                        ])))
        else :
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = q3,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=MessageAction(label="なんでやねん！",text="なんでやねん！")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="詳しく",data="詳しく")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="OK",data="OK")
                                ),
                        ])))

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'OK':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="数式を入力して下さい"))
    elif event.postback.data == 'グラフ':
        file = open(event.source.user_id[:4] + ".txt","r")
        data = file.read()
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = data+"(https://dictionary.goo.ne.jp/word/"+data+")",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="OK",data="OK")
                        ),
                    ])))

@handler.add(FollowEvent)
def handle_follow(event):
    app.logger.info("Got Follow event:" + event.source.user_id)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="数式を入力して下さい"))



if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
