# インポートするライブラリ
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
import os
import matplotlib.pyplot as plt
from sympy import *
from PIL import Image
# 軽量なウェブアプリケーションフレームワーク:Flask
app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

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
    if text == "グラフ":

        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()

        x = symbols('x')
        y = sympify(data)
        g = plotting.plot(y)
        g.save("static/" + event.source.user_id[:4] +".png")

        url = "https://calculation-sympy.herokuapp.com/static/" + event.source.user_id[:4] + ".png"
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(url, url)
            )

    elif text == "微分":
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()

        x = symbols('x')
        y = sympify(data)
        dy = diff(y)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = sstr(dy),
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="グラフ",text="グラフ")
                            ),
                        QuickReplyButton(
                            action=MessageAction(label="微分",text="微分")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="OK",data="OK")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="help",data="help")
                            ),
                    ])))
                    
    else:
        file = open(event.source.user_id[:4] +".txt","w")
        file.write(text)
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "操作を選んでください",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="グラフ",text="グラフ")
                            ),
                        QuickReplyButton(
                            action=MessageAction(label="微分",text="微分")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="OK",data="OK")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="help",data="help")
                            ),
                    ])))

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'OK':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="解析したい数式を入力して下さい"))
    elif event.postback.data == 'help':
        file = open(event.source.user_id[:4] + ".txt","r")
        data = file.read()
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "※入力の形式が違うと結果が返ってきません。\n※掛け算の記号「*」は省略せずに書いてください。\n \nーー演算記号についてーー\n掛け算: *\n割り算: /\nべき乗: ^　(または**)\n　\nーー使える関数,定数ーー\n三角関数: sin(x),cos(x)\n対数関数: log(x)\n指数関数: exp(x)\n二乗根: sqrt(x)\n円周率: pi\n自然対数の底: E\n虚数単位: I",
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
        event.reply_token, TextSendMessage(text='解析したい数式を入力して下さい'))


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
