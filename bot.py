import discord
import os
import random
from flask import Flask
from threading import Thread
import requests  # 👈 【修正点１】requests をインポートする

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
        "お前キヴォトスにおいてシャーレと関わり断つのは死と同じやぞ考え直せな？", "🗿🍷ガチイク！", "臨戦ホシノ出番少ないとか言っちゃったから増やしてきた？",
        "まあみんな言ってると思うけどこのファル子普通にエロいんだわ\nウマ娘でちんちんをイライラさせるな",
        "あそうそう海外のモンエナ黒人のチ○ポみたいなサイズのがあって非常に良きだった、pixivとかでよくある黒人に寝盗られる女側の気持ちになれる、日本でも売って欲しい",
        "ウマ娘ゲボつまんねえwwwwこんなんに天井したのマジでアホくさすぎるwゆうて星3は4人きててそのうち片方もちゃんと引けてるから悪くはねえけどもっと未所持星3出て欲しかったし、そもそも30連くらいでブライトこいやカス!まあ神名文字枯渇してたから回収したと思えばいいやもう",
        "「ネタバレされたくなければ即見ろ自衛しろはマジで正論なんだけど、人に配慮しようっていう心があれば自分がネタバレって思わないレベルのネタバレでも普通はしないはずなんだよね、楽しみを奪うとかよりも人としての程度の話なんだよね」",
        "もうそれセックスやないかい‼️😁\nオラ‼️夜のお祭りすんぞ‼️😡\nﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝﾊﾟﾝ←花火の音です😃",
        "臨戦ホシノこれからだと正直使う機会あんま無いと思ってる", "俺も予言者だから予言するわ\nオナニー雲があるから今日俺はオナニーをする",
        "心がドビュDビュすんるんじゃあ", "人生初ピンサロ行ってきました\n普通にイキました\nえぐい",
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
        "ことねパネルあるやんキスさせろキス", "お前ルフィ舐めてんの？","魔法少女スズミ可愛すぎる",
    ],
    "ひか": [
        "彼女とカラケ彼女抜き", "俺も股間に種子貯蔵庫あるよ！！", "仮装舞踏会にコユハラ冷笑してるヤツいたから引っこ抜け",
        "ブルアカ辞めたんでミュートブロ解お好きにどうぞ",
        "僕から君へ贈る 愛の証明\n100%早瀬ユウカ 絆100\nhttps://pbs.twimg.com/media/GkXd5qPaoAAqmoH?format=jpg&name=large",
        "人生で初めてtiktok撮ったわ", "まだ飲めないにょ！！\n酒に飲まれる人1人しか思い浮かばんなーw", "𓏸𓏸てwの乱用きた",
        "先生かなーやっぱりww\n自分は思わないんだけど周りにシャーレの先生に似てるってよく言われるwww\nこないだヘルメット団に絡まれた時も気が付いたら意識無くて周りに人が血だらけで倒れてたしなwww\nちなみに彼女もユウカに似てる(聞いてないw)",
        "管理不足\nASMRではいつも〇〇管理されてるのにね笑",
    ],
    "どげろん": [
        "感情的になってDMで吐き出してしまった 情けないな俺は", "「︎︎”ゲーム性”とは」", "え？俺はバカすぎだって？\nガハハ 確かにな！",
        "お前マジで調子のんなよ\n冗談にしてもしょうもない弄りしてんじゃねえよバカがよ\nお前次顔合わせた時覚えておけよマジで\nあの時はガチギレしようかなとは思ったけど 空気悪くするのもアレやから我慢したけどな\n舐めてんのか俺の事冗談をするにしても引き際考えろカス",
        "俺は自分の結果がすごくないって言ってしまうと\n本気でぶつかってトマト突破出来なかった人に対して失礼だと思うので\nだから俺は自分が成し遂げたことは凄いと胸を張りたいと思います\nだからルナやったやつらも狂喜乱舞して喜んでください おめでとうございます",
        "まともなやつは孤独になりやすい\nそれは何故か 信念があるからだと思う\nよく孤立するやつはそれはそいつが悪者だからじゃない 信念を持ち\n自分が自分を恥じないために独りになる",
        "くらふとん 俺にもいいねしてくれ", "あの日から俺のちんぽは宇宙を目指したんだ", "これが〝大人〟の顔だよココナちゃん",
        # 👇 【修正点２】最後の文字列に " (引用符) を追加しました
        "@ftgo225 は~^キチってんな~^\nまぁ腹の底が分からない人間って警戒されるからな 何考えてるかよりもこうやって形に残した方がいいんじゃね？",
    ],
    ("あも", "熊ジェット", "垂狼", "Aモ", "アモ"): [
        "ろりおっぱいのみっぱい",
        "サークル通話楽しかったー\n自分はゆる〜い感じでやって行きたいから今後も今のサークルに居続けると思う😇\n順位も大事だと思うけど、交流とか一緒に何かを頑張ることを大事にしたい💪",
        "【ご報告】\n元いたサークルに戻ります。\n正直めちゃくちゃのハチャメチャに楽しみ‼️‼️‼️\nうおおおおおおおお",
        "あも先あも先言われるけど実はえーもなんすよね", "てかひかがきのイラスト完全に忘れてた",
        "通話してる人全員に言われるけどTwitterと通話してる時の自分が別人すぎるらしい\nTwitterのが本心だからディスコのイメージだとかなり悪いやろなw",
        "加入から脱退まで一生楽しかったです‼️\nこれからのあまねくの活躍にも超絶期待してます✨\nただひたすらに感謝🙏🙏🙏\n体調管理に関しては許してください😭",
        "あまねくVRC禁止みたいなの聞いてたけど俺もするべ",
        "深夜だから……\nあまねくに入れたお陰ですごい大きいコミュニティに属せたのは嬉しいな😇\nあまねくだけでも大きいのに分岐点もあるから繋がりに困る事が無いのが本当にすごいw",
        "あまねく通話の雰囲気が好きすぎてやべ", "あまねく通話たのしぃなぁ",
        "めちゃくちゃ夜中ですが本日より…\n「あまねく愛の終着点」様に加入させていただきました(*´˘`*)\n初日からめちゃくちゃ楽しくて最高でした\nあと初日からサークル長の寝言に立ち会えて感動です😭",
        "あまねくラウンジの雰囲気楽しかったな\n時間あればROM専じゃなくて参加したかった😭",
        "@Rateart1227\nおつありです!!\nまっちゃんさんもお疲れ様〜(*´˘`*)",
        "@chomasa0110\nフレさんが替えくれたから何とかなりそう！\nただゴズ爆発TAは擁護しようもなくゴミや…",
        "全56しゅるい、好きな並びでつなげて飾ったり遊んだりしてみてください！",
        "新宿！\nたくさんの生徒さんががたんごとんとしてますので、お近くに立ち寄りの際はぜひー！\nhttps://pbs.twimg.com/media/GpCCpqBa0AAyQbX?format=jpg&name=large",
        "株式会社Yostarに入社しました\nhttps://note.com/kumajet/n/n763fa4043827",
        "株式会社Cygamesを退職しました\nhttps://note.com/kumajet/n/n32182c2f99fc","https://x.com/StellaSoraJP/status/1871843329295716846?t=rZSqMjNdN5LwYE1pMLkjlg&s=19",
    ],
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
    activity = discord.CustomActivity(name="🗿🍷ガチイク！")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id not in TARGET_CHANNEL_IDS:
        return
    
    content = message.content.lower()
    
    for keywords, response_list in RESPONSE_MAP.items():
        triggered = False
        if isinstance(keywords, tuple):
            if any(k.lower() in content for k in keywords):
                triggered = True
        else:
            if keywords.lower() in content:
                triggered = True
        
        if triggered:
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

# ブルアカデータ取得機能
@tree.command(name="chara_data", description="SchaleDBから生徒の情報を検索します。")
@discord.app_commands.describe(name="生徒の名前（一部でも可）")
async def chara_data_command(interaction: discord.Interaction, name: str):
    await interaction.response.defer()

    try:
        search_url = f"https://schaledb.com/api/v1/students/search?query={name}"
        search_response = requests.get(search_url)

        if search_response.status_code != 200:
            await interaction.followup.send("APIエラーが発生しました。SchaleDBがダウンしているかもしれません。")
            return

        search_data = search_response.json()
        if not search_data:
            await interaction.followup.send(f"「{name}」という名前の生徒は見つかりませんでした。")
            return

        student_id = search_data[0]['Id']
        data_url = f"https://schaledb.com/api/v1/students/{student_id}"
        data_response = requests.get(data_url)
        
        if data_response.status_code != 200:
            await interaction.followup.send("生徒の詳細データの取得に失敗しました。")
            return
            
        student = data_response.json()

        embed = discord.Embed(
            title=f"{student['Name']} ({student['NameJp']})",
            description=student['Profile'],
            color=discord.Color.blue()
        )
        
        embed.set_thumbnail(url=f"https://schaledb.com/images/student/icon/{student['Id']}.webp")
        
        embed.add_field(name="学校", value=student['School'], inline=True)
        embed.add_field(name="部活", value=student['Club'], inline=True)
        embed.add_field(name="学年", value=student['SchoolYear'], inline=True)
        
        embed.add_field(name="役割 (Role)", value=student['Role'], inline=True)
        embed.add_field(name="武器", value=student['WeaponType'], inline=True)
        embed.add_field(name="誕生日", value=student['Birthday'], inline=True)
        
        embed.add_field(name="攻撃タイプ", value=student['AttackType'], inline=True)
        embed.add_field(name="防御タイプ", value=student['DefenseType'], inline=True)
        embed.add_field(name="遮蔽", value="使う" if student['Cover'] else "使わない", inline=True)

        embed.set_footer(text="Data from SchaleDB")

        await interaction.followup.send(embed=embed)

    except requests.exceptions.RequestException as e:
        print(f"APIリクエストエラー: {e}")
        await interaction.followup.send("リクエスト中にネットワークエラーが発生しました。")
    except Exception as e:
        print(f"予期せぬエラー: {e}")
        await interaction.followup.send(f"情報の取得中に不明なエラーが発生しました: {e}")

# BOTの実行
try:
    keep_alive()
    print("Webサーバーを起動しました。")
    TOKEN = os.environ['DISCORD_BOT_TOKEN']
    client.run(TOKEN)
except KeyError:
    print("エラー: 環境変数 'DISCORD_BOT_TOKEN' が設定されていません。")
