import discord
import os
import random
from flask import Flask
from threading import Thread

# ----------------------------------------------------
# Webサーバー機能 (Renderのスリープ防止用)
# ----------------------------------------------------
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------------------------


# BOTが応答するチャンネルIDのリスト
TARGET_CHANNEL_IDS = [
    1372899565920845996,
    1422043344938471485,
]

# 応答リスト（辞書）の定義
RESPONSE_MAP = {
    "ちょまさ": [
        "ルナやぞ", "ちょまさ降臨", "自分のことを○○だと思ってる一般人だよ", "イチャラブーの煮付け", "○○てｗ",
        "12万バズのちょまさ様やぞ", "ちなみにちょまさバフ最強やったで", "万仙陣様やぞ", "もうルナやぞって言えない",
        "総力戦最高難易度のLunaticやぞ", "俺は星3でいい正月ハルカいなかったけどルナやったぞ", "まっちゃんめっちゃ童顔やぞ",
        "お前キヴォトスにおいてシャーレと関わり断つのは死と同じやぞ考え直せな？", "ガチイク！", "臨戦ホシノ出番少ないとか言っちゃったから増やしてきた？",
        "まあみんな言ってると思うけどこのファル子普通にエロいんだわ\nウマ娘でちんちんをイライラさせるな",
        "あそうそう海外のモンエナ黒人のチ○ポみたいなサイズのがあって非常に良きだった、pixivとかでよくある黒人に寝盗られる女側の気持ちになれる、日本でも売って欲しい",
        "ウマ娘ゲボつまんねえwwwwこんなんに天井したのマジでアホくさすぎるwゆうて星3は4人きててそのうち片方もちゃんと引けてるから悪くはねえけどもっと未所持星3出て欲しかったし、そもそも30連くらいでブライトこいやカス!まあ神名文字枯渇してたから回収したと思えばいいやもう",
        "「ネタバレされたくなければ即見ろ自衛しろはマジで正論なんだけど、人に配慮しようっていう心があれば自分がネタバレって思わないレベルのネタバレでも普通はしないはずなんだよね、楽しみを奪うとかよりも人としての程度の話なんだよね」",
        "もうそれセックスやないかい‼️😁\nオラ‼️夜のお祭りすんぞ‼️😡\nﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝ←花火の音です😃",
        "臨戦ホシノこれからだと正直使う機会あんま無いと思ってる", "俺も予言者だから予言するわ\nオナニー雲があるから今日俺はオナニーをする",
        "心がドビュドビュすんるんじゃあ", "人生初ピンサロ行ってきました\n普通にイキました\nえぐい",
        "ライフライン ブスってTwitterで検索したらホライゾンがADHDでワットソンが自閉症なの初めて知ったわ\n\nAPEX始めたてライフライン勧められたから使ってたけど俺が雑魚なだけなのにこのブス弱いって言いまくってた\n\nまあライフラインは普通に良い奴だからなぁ",
        "ドルマリース、ルー", "まーたバズちゃったな😅\nユウカは可愛いからね🥰🥰🥰",
        "何気ライフラインが初の2000ハンマーなんだよな\nブスだからとかじゃなくて普通にキャラとして使いたくない\nジブ(ゲイ)ラハ(ノンバイナリー)ヴァルキリー(レズ)しか使わん",
        "確かにホドってインベイドピラーとかいう棒状のブツで侵食してきたり、\n触手あったりでエロいよな\nタコはエロいってヒナも言ってたしな",
    ],
    "ゆずみつ": [
        "いいぞ\n羽持ってる子が卵産む概念もっと流行れ\n先生に食べてもらってゾクゾクしてると尚良い",
        "人の味覚をどうこう言うつもりはないですがこう言う事らしいので僕は歯磨き粉派です😎",
        "かんなづきさん僕の事好きならそう言ってくれれば良いのに…", "あ、どこ触って…んっ♡///\nそこ敏感だからっ///らめっ♡///",
        "RJ01361216\nオホ声/淫語ありなので苦手な人は居るかも\n僕は好きですね\n<https://www.dlsite.com/maniax/work/=/product_id/RJ01361216.html>\n",
        "キヴォ↑トスでは淫夢ご↑っこは恥ずかしいんだよー！"
    ],
    "かんなづき": [
        "よわよわゆずみつ先生甘々マゾマゾえっちすぎるカフェタッチすごいたのしいブルアカ愛イチャラブーカリカリほむほむASMR",
        "チョコミント美味しいですよね？", "関係は無いんですけど、卵って美味しいですよね🥚", "エロいとえっちは別だと思ってて、えっち派閥に属してます",
    ],
    ":sa:": [
        "本日", "あーおけ笑", "やめてね", "ユウカあるある 可愛い", "NTRって何⁉️クソすぎ⁉️🤩", "一捨九入ぐらいしてるだろこれ",
        "メカニックキンタマおもろい\nキンタマパカパカでワロタ~W", "コユキかわいい", "ウミカかわいい、ウミカわいい",
        "ちょうど死にたかったので助かります！w",
        "しこってねなさい\n\n俺はしごでき人間だから言われる前にもう終わってますよ。\n\nってそれしこでき人間やないか～い‼️W\n\n寝ます。",
        "おれは最初からスミレのかわいさに気づいてた、おまえらはなんなんだ？", "せやで\n今のとこ自分からアクション起こしてないけどなW",
        "えりーと身共可愛いね❤️ྀི🧡ྀི🩷ྀི💚ྀི💙ྀི🩵ྀི💜ྀི🤍ྀི🤎ྀི",
        "ヒマリと結婚して体が不自由で子供が作れなくて影で泣いてるヒマリを偶然見つけて全力で慰めたい",
        "深夜だから許されると思うんですがぶっちゃけブルアカで一番エロいのはノアだと思っている", "유우카 사랑해",
        "まじでよくねー\n俺の意思どうにかならんかな、石だけに‼️\nガハハ‼️笑えよおい笑えよ", "ガーン", "鍵垢の名前大募集‼️",
        "ことねパネルあるやんキスさせろキス",
        "お前ルフィ舐めてんの？",
    ],
    # 👇 【修正点１】カンマを追加しました
    "ひか": [
        "彼女とカラオケ彼女抜き",
        "俺も股間に種子貯蔵庫あるよ！！",
        "仮装舞踏会にコユハラ冷笑してるヤツいたから引っこ抜け",
        "ブルアカ辞めたんでミュートブロ解お好きにどうぞ"
        "僕から君へ贈る  愛の証明\n100%早瀬ユウカ 絆100",
        "人生で初めてtiktok撮ったわ",
        "まだ飲めないにょ！！\n酒に飲まれる人1人しか思い浮かばんなーw",
        "𓏸𓏸てwの乱用きた",
        "先生かなーやっぱりww\n自分は思わないんだけど周りにシャーレの先生に似てるってよく言われるwww\nこないだヘルメット団に絡まれた時も気が付いたら意識無くて周りに人が血だらけで倒れてたしなwww\nちなみに彼女もユウカに似てる(聞いてないw)
    ]
}

# chomasaコマンドで紹介するポストのURLリスト
CHOMASA_POST_LINKS = [
    "https://x.com/chomasa0110/status/1851157072349708583", "https://x.com/chomasa0110/status/1870836874354532648",
    "https://x.com/chomasa0110/status/1851153967247667363",
    "https://x.com/chomasa0110/status/1955618377944514874?s=46&t=YRNFhWuUfWmcyhVVy1uCRQ",
]

# Discordボットの準備
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await tree.sync()
    print("スラッシュコマンドを同期しました。")
    
    activity = discord.CustomActivity(name="ルナやぞ")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id not in TARGET_CHANNEL_IDS:
        return
    content = message.content.lower()
    for keyword, response_list in RESPONSE_MAP.items():
        if keyword.lower() in content:
            chosen_response = random.choice(response_list)
            if chosen_response:
                await message.channel.send(chosen_response)
            return

@tree.command(name="chomasa", description="ちょまささんのバズを1つ紹介します。")
async def chomasa_command(interaction: discord.Interaction):
    if not CHOMASA_POST_LINKS:
        await interaction.response.send_message("紹介できるポストがまだ登録されていません。", ephemeral=True)
        return
    random_post_link = random.choice(CHOMASA_POST_LINKS)
    await interaction.response.send_message(random_post_link)

# ----------------------------------------------------
# 👇 【修正点２】ボットを起動するコードを、ファイルの一番最後に正しく配置しました
# ----------------------------------------------------
try:
    keep_alive()
    print("Webサーバーを起動しました。")
    
    TOKEN = os.environ['DISCORD_BOT_TOKEN']
    client.run(TOKEN)
except KeyError:
    print("エラー: 環境変数 'DISCORD_BOT_TOKEN' が設定されていません。")

