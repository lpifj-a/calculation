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
    try:
        file = open(event.source.user_id[:4] + "range.txt", "r")
        trange = file.read()
        file.close()
        range = trange.split(",")
        min = float(range[0])
        max = float(range[1])
    except:
        min = -10
        max = 10

    if text == "グラフ":
        file = open(event.source.user_id[:4] +"mode.txt","w")
        file.write("グラフ")
        file.close()
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()

        x = symbols('x')

        try :
            y = sympify(data)
            g = plot(y,(x,min,max),ylim=(min,max),axis_center=(0,0),legend=true,aspect_ratio=(1.0,1.0),show=false)
            g.save("static/" + event.source.user_id[:4] +".png")
            url = "https://calculation-sympy.herokuapp.com/static/" + event.source.user_id[:4] + ".png"

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    url,url,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="軸の範囲指定",data="軸の範囲指定")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="グラフを追加",data="グラフ2")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = "数式を読み取れませんでした",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),

                        ])))
    elif "[2]" in text :
        data2 = text.split("]")[1]
        file = open(event.source.user_id[:4] +"2.txt","w")
        file.write(data2)
        file.close()
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()

        x = symbols('x')

        try :
            y = sympify(data)
            y2 = sympify(data2)
            g = plot(y,y2,(x,min,max),ylim=(min,max),axis_center=(0,0),legend=true,aspect_ratio=(1.0,1.0),show=false)
            g[1].line_color = "green"
            g.save("static/" + event.source.user_id[:4] +".png")
            url = "https://calculation-sympy.herokuapp.com/static/" + event.source.user_id[:4] + ".png"

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    url,url,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="グラフを追加",data="グラフ3")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = "数式を読み取れませんでした",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="グラフを追加",data="グラフ2")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),

                        ])))
    elif "[3]" in text :
        data3 = text.split("]")[1]
        file = open(event.source.user_id[:4] +"3.txt","w")
        file.write(data3)
        file.close()
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()
        file = open(event.source.user_id[:4] + "2.txt", "r")
        data2 = file.read()
        file.close()

        x = symbols('x')

        try :
            y = sympify(data)
            y2 = sympify(data2)
            y3 = sympify(data3)
            g = plot(y,y2,y3,(x,min,max),ylim=(min,max),axis_center=(0,0),legend=true,aspect_ratio=(1.0,1.0),show=false)
            g[1].line_color = "green"
            g[2].line_color = "red"
            g.save("static/" + event.source.user_id[:4] +".png")
            url = "https://calculation-sympy.herokuapp.com/static/" + event.source.user_id[:4] + ".png"

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    url,url,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = "数式を読み取れませんでした",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="グラフを追加",data="グラフ3")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),

                        ])))
    elif "," in text:
        try:
            file = open(event.source.user_id[:4] + "mode.txt", "r")
            mode = file.read()
            file.close()
        except:
            mode ="媒介変数"

        if mode == "定積分":
            integ = text.split(",")
            a = float(integ[0])
            b = float(integ[1])
            file = open(event.source.user_id[:4] + ".txt", "r")
            data = file.read()
            file.close()
            try:
                x = symbols('x')
                y = sympify(data)
                Y = integrate(y,(x,a,b))
                text = sstr(Y)
            except:
                text = "数式を読み取れませんでした"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = text,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))
        elif mode == "グラフ":
            file = open(event.source.user_id[:4] +"range.txt","w")
            file.write(text)
            file.close()
            range = text.split(",")
            min = float(range[0])
            max = float(range[1])

            file = open(event.source.user_id[:4] + ".txt", "r")
            data = file.read()
            file.close()

            x = symbols('x')
            y = sympify(data)
            g = plot(y,(x,min,max),ylim=(min,max),axis_center=(0,0),legend=true,aspect_ratio=(1.0,1.0),show=false)
            g.save("static/" + event.source.user_id[:4] +".png")
            url = "https://calculation-sympy.herokuapp.com/static/" + event.source.user_id[:4] + ".png"

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    url,url,
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="軸の範囲指定",data="軸の範囲指定")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="グラフを追加",data="グラフ2")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))
        elif mode == "媒介変数":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text = "準備中です",
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(
                                action=PostbackAction(label="ok",data="ok")
                                ),
                            QuickReplyButton(
                                action=PostbackAction(label="help",data="help")
                                ),
                        ])))

    elif text == "微分":
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()
        try:
            x = symbols('x')
            y = sympify(data)
            dy = diff(y)
            text = sstr(dy)
        except:
            text = "数式を読み取れませんでした"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = text,
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="ok",data="ok")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="help",data="help")
                            ),
                    ])))
    elif text == "積分":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "選んでください",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="不定積分",data="不定積分")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="定積分",data="定積分")
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
                            action=MessageAction(label="積分",text="積分")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="ok",data="ok")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="help",data="help")
                            ),
                    ])))
@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'ok':
        file = open(event.source.user_id[:4] +"mode.txt","w")
        file.write("媒介変数")
        file.close()
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="解析したい数式を入力して下さい"))
    elif event.postback.data == 'help':
        file = open(event.source.user_id[:4] + ".txt","r")
        data = file.read()
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = "※掛け算の記号「*」は省略せずに書いてください。\n"\
                       "※微分積分は基本的に変数xについて行います。\n"\
                       "※予期しない入力に対して返答がおかしくなることがあります。\n\n"\
                        "ーー演算記号についてーー\n"\
                        "掛け算: *\n"\
                        "割り算: /\n"\
                        "べき乗: ^　(または**)\n\n"\
                        "ーー使える関数,定数ーー\n"\
                        "三角関数: sin(x),cos(x)\n"\
                        "対数関数: log(x)\n"\
                        "指数関数: exp(x)\n"\
                        "二乗根: sqrt(x)\n"\
                        "円周率: pi\n"\
                        "自然対数の底: E\n"\
                        "虚数単位: I",
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="ok",data="ok")
                        ),
                    ])))
    elif event.postback.data == 'グラフ2':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "追加するグラフの数式を[2]を先頭に書いて入力して下さい\n"\
                                   "例：[2]3*x^2"
                           ))
    elif event.postback.data == 'グラフ3':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "追加するグラフの数式を[3]を先頭に書いて入力して下さい\n"\
                                   "例：[3]x^2*log(x)"
                           ))
    elif event.postback.data == '軸の範囲指定':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "軸の範囲を\n"\
                                   "\"最小値,最大値\"\n"\
                                   "の形式で入力して下さい"
                                   "例：-5,5"
                           ))
    elif event.postback.data == '不定積分':
        file = open(event.source.user_id[:4] + ".txt", "r")
        data = file.read()
        file.close()
        try:
            x = symbols('x')
            y = sympify(data)
            Y = integrate(y)
            text = sstr(Y)
        except:
            text = "数式を読み取れませんでした"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text = text,
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="ok",data="ok")
                            ),
                        QuickReplyButton(
                            action=PostbackAction(label="help",data="help")
                            ),
                    ])))
    elif event.postback.data == '定積分':
        file = open(event.source.user_id[:4] +"mode.txt","w")
        file.write("定積分")
        file.close()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "積分区間を \"下端,上端\" の形式で入力して下さい\n"\
                                   "例：0,10"
                           ))
@handler.add(FollowEvent)
def handle_follow(event):
    app.logger.info("Got Follow event:" + event.source.user_id)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="グラフ描画、微分積分などの計算ができます。\n"\
                                                "解析したい数式を入力して下さい。\n"\
                                                "※掛け算の記号「*」は省略せずに書いてください。\n"\
                                                "※微分積分は基本的に変数xについて行います\n\n"\
                                                "ーー演算記号についてーー\n"\
                                                "掛け算: *\n"\
                                                "割り算: /\n"\
                                                "べき乗: ^　(または**)\n\n"\
                                                "ーー使える関数,定数ーー\n"\
                                                "三角関数: sin(x),cos(x)\n"\
                                                "対数関数: log(x)\n"\
                                                "指数関数: exp(x)\n"\
                                                "二乗根: sqrt(x)\n"\
                                                "円周率: pi\n"\
                                                "自然対数の底: E\n"\
                                                "虚数単位: I"
                                           ))

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
