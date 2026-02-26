import discord
import os
import random
from flask import Flask
from threading import Thread
import requests
import datetime 

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive."

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------------------------

TARGET_CHANNEL_IDS = [
    1372899565920845996,
    1422043344938471485,
]

NOTIFICATION_CHANNEL_ID = 1437221242355585074

# 応答リスト（辞書）の定義
RESPONSE_MAP = {
    "ちょまさ": [
        "ルナやぞ", "ちょまさ降臨", "自分のことを○○だと思ってる一般人だよ", "イチャラブーの煮付け", "○○てｗ",
        "12万バズのちょまさ様やぞ", "ちなみにちょまさバフ最強やったで", "万仙陣様やぞ", "もうルナやぞって言えない",
        "総力戦最高難易度のLunaticやぞ", "俺は星3でいい正月ハルカいなかったけどルナやったぞ", "まっちゃんめっちゃ童顔やぞ",
        "お前キヴォトスにおいてシャーレと関わり断つのは死と同じやぞ考え直せな？", "🗿🍷ガチイク！", "臨戦ホシノ出番少ないとか言っちゃったから増やしてきた？",
        "まあみんな言ってると思うけどこのファル子普通にエロいんだわ\nウマ娘でちんちんをイラつかせるな",
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
        "ちな俺のサキこれ\n抜く以外では一切触れないようにしたい",
        "サテライトの「さ」さんとぽっちパイのhikaと飯！！\n#サテライト甘党部\n#めしてろぽっちパイ\nhttps://pbs.twimg.com/media/GyY1wrRaQAEUmmi?format=jpg&name=large\nhttps://pbs.twimg.com/media/GyY1wrUagAAL28S?format=jpg&name=large",
#飯仙陣
    ],
    "ゆずみつ": [
        "いいぞ\n羽持ってる子が卵産む概念もっと流行れ\n先生に食べてもらってゾクゾクしてると尚良い",
        "人の味覚をどうこう言うつもりはないですがこう言う事らしいので僕は歯磨き粉派です😎",
        "かんなづきさん僕の事好きならそう言ってくれれば良いのに…", "あ、どこ触って…んっ♡///\nそこ敏感だからっ///らめっ♡///",
        "RJ01361216\nオホ声/淫語ありなので苦手な人は居るかも\n僕は好きですね\n<https://www.dlsite.com/maniax/work/=/product_id/RJ01361216.html>\n",
        "キヴォ↑トスでは淫夢ご↑っこは恥ずかしいんだよー！",
        "あまりにも早い射精",
    ],
    "かんなづき": [
        "よわよわゆずみつ先生甘々マゾマゾえっちすぎるカフェタッチすごいたのしいブルアカ愛イチャラブーカリカリほむほむASMR",
        "チョコミント美味しいですよね？", "関係は無いんですけど、卵って美味しいですよね🥚", "エロいとえっちは別だと思ってて、えっち派閥に属してます",
    ],
    "さ": [
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
        "サテライト様を脱退させていただきました\nモチベ低下が主な理由です\n本当に最高の環境でした\n半年間ありがとうございました！！",
        "ノアのやつ匂いが爽やかだからちょっとスパイシーなフルーツって感じで考えたらギリいけなくもないかも\n口の中からめっちゃいい匂いしてウケる\nあとこれ飯の前にやるもんじゃないわどう考えても",
        "失礼しました、萌えアニメが出てしまいました",
    ],
    "ひか": [
        "彼女とカラケ彼女抜き", "俺も股間に種子貯蔵庫あるよ！！", "仮装舞踏会にコユハラ冷笑してるヤツいたから引っこ抜け",
        "ブルアカ辞めたんでミュートブロ解お好きにどうぞ",
        "僕から君へ贈る 愛の証明\n100%早瀬ユウカ 絆100\nhttps://pbs.twimg.com/media/GkXd5qPaoAAqmoH?format=jpg&name=large",
        "人生で初めてtiktok撮ったわ", "まだ飲めないにょ！！\n酒に飲まれる人1人しか思い浮かばんなーw", "𓏸𓏸てwの乱用きた",
        "先生かなーやっぱりww\n自分は思わないんだけど周りにシャーレの先生に似てるってよく言われるwww\nこないだヘルメット団に絡まれた時も気が付いたら意識無くて周りに人が血だらけで倒れてたしなwww\nちなみに彼女もユウカに似てる(聞いてないw)",
        "管理不足\nASMRではいつも〇〇管理されてるのにね笑",
        "昔から伝えられてる言葉があるじゃろ\n女と機械は叩けば治るってな‼️\nガハハ😂",
    ],
    "どげろん": [
        "感情的になってDMで吐き出してしまった 情けないな俺は", "「︎︎”ゲーム性”とは」", "え？俺はバカすぎだって？\nガハハ 確かにな！",
        "お前マジで調子のんなよ\n冗談にしてもしょうもない弄りしてんじゃねえよバカがよ\nお前次顔合わせた時覚えておけよマジで\nあの時はガチギレしようかなとは思ったけど 空気悪くするのもアレやから我慢したけどな\n舐めてんのか俺の事冗談をするにしても引き際考えろカス",
        "俺は自分の結果がすごくないって言ってしまうと\n本気でぶつかってトマト突破出来なかった人に対して失礼だと思うので\nだから俺は自分が成し遂げたことは凄いと胸を張りたいと思います\nだからルナやったやつらも狂喜乱舞して喜んでください おめでとうございます",
        "まともなやつは孤独になりやすい\nそれは何故か 信念があるからだと思う\nよく孤立するやつはそれはそいつが悪者だからじゃない 信念を持ち\n自分が自分を恥じないために独りになる",
        "くらふとん 俺にもいいねしてくれ", "あの日から俺のちんぽは宇宙を目指したんだ", "これが〝大人〟の顔だよココナちゃん",
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
        "深夜だから……\nあまねくに入れたお陰ですごい大きいコミュニティに属せたのは嬉しいな😇\nあまねくだけでも大きいのに分岐点もあるから繋りに困る事が無いのが本当にすごいw",
        "あまねく通話の雰囲気が好きすぎてやべ", "あまねく通話たのしぃなぁ",
        "めちゃくちゃ夜中ですが本日より…\n「あまねく愛の終着点」様に加入させていただきました(*´˘`*)\n初日からめちゃくちゃ楽しくて最高でした\nあと初日からサークル長の寝言に立ち会えて感動です😭",
        "あまねくラウンジの雰囲気楽しかったな\n時間あればROM専じゃなくて参加したかった😭",
        "@Rateart1227\nおつありです!!\nまっちゃんさんもお疲れ様〜(*´˘`*)",
        "@chomasa0110\nフレさんが替えくれたから何とかなりそう！\nただゴズ爆発TAは擁護しようもなくゴミや…",
        "テスト",
        "全56しゅるい、好きな並びでつなげて飾ったり遊んだりしてみてください！",
        "新宿！\nたくさんの生徒さんががたんごとんとしてますので、お近くに立ち寄りの際はぜひー！\nhttps://pbs.twimg.com/media/GpCCpqBa0AAyQbX?format=jpg&name=large",
        "株式会社Yostarに入社しました\nhttps://note.com/kumajet/n/n763fa4043827",
        "株式会社Cygamesを退職しました\nhttps://note.com/kumajet/n/n32182c2f99fc","https://x.com/StellaSoraJP/status/1871843329295716846?t=rZSqMjNdN5LwYE1pMLkjlg&s=19",
    ],
        "ゆばも": [
        "https://pbs.twimg.com/media/G9ukWP8acAAnYoo?format=jpg&name=large",
        "俺と会った印象「女殴ってそう」って言われるんすけど殴ってそうですか！？！",
        "この世の中、喋ること=話すだと思ってる人多すぎる\n\n喋る:聞くの割合が5:5になって初めてみ 「話す」だよ", "サークルスペースの前で30分何も買わずマシンガントークされたよ",
        "https://pbs.twimg.com/media/G9jODtjaMAQodHR?format=jpg&name=small",
        "明けましておめでとうございます。\n皆さん今年もよろしくお願いしますブルーアーカイブ",
        "ちょまさ会いたい、寂しいよ","冬コミに参加した三善タカネ\nhttps://pbs.twimg.com/media/G9gS2TdagAEaEvT?format=jpg&name=4096x4096",
        "タカネ「私をこんな目に合わせるなんて屈辱ですわ」\n関西弁のおっさん「私をこんな目に合わせるなんて屈辱ですわ」",
        "金が足りません。金を買いますか\n#ブルアカ #アロナ\nhttps://pbs.twimg.com/media/Gy3TlJzacAAg9hj?format=jpg&name=large"
    ],
}

CHOMASA_POST_LINKS = [
    "https://x.com/chomasa0110/status/1851157072349708583", "https://x.com/chomasa0110/status/1870836874354532648",
    "https://x.com/chomasa0110/status/1851153967247667363",
    "https://x.com/chomasa0110/status/1955618377944514874?s=46&t=YRNFhWuUfWmcyhVVy1uCRQ",
]

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

    try:
        channel = client.get_channel(NOTIFICATION_CHANNEL_ID)
        
        if channel:
            jst = datetime.timezone(datetime.timedelta(hours=9))
            now = datetime.datetime.now(jst)
            
            embed = discord.Embed(
                title="✅ BOT起動完了",
                description="BOTが再起動しました。応答内容が更新されています。",
                color=discord.Color.green(),
                timestamp=now  # Embedのフッターにタイムスタンプを表示
            )
            embed.set_footer(text=f"起動時刻 (JST)")
            
            # メッセージを送信
            await channel.send(embed=embed)
            print(f"チャンネル (ID: {NOTIFICATION_CHANNEL_ID}) に起動通知を送信しました。")
            
        else:
            print(f"エラー: 通知用チャンネル (ID: {NOTIFICATION_CHANNEL_ID}) が見つかりません。")
            print("指定したチャンネルIDが正しいか、BOTにそのチャンネルの「メッセージを送信」権限があるか確認してください。")

    except Exception as e:
        print(f"通知の送信中にエラーが発生しました: {e}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id not in TARGET_CHANNEL_IDS:
        return
    
    content = message.content.strip().lower()
    
    for keywords, response_list in RESPONSE_MAP.items():
        triggered = False
        
        if isinstance(keywords, tuple):
            if any(content == k.lower() for k in keywords):
                triggered = True
        else:
            if content == keywords.lower():
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

@tree.context_menu(name="文字をシャッフル")
async def shuffle_message(interaction: discord.Interaction, message: discord.Message):

    text = message.content
    
    if not text:
        await interaction.response.send_message("シャッフルできる文字が見つかりませんでした。", ephemeral=True)
        return

    char_list = list(text)
    random.shuffle(char_list)
    shuffled_text = "".join(char_list)
    
    await interaction.response.send_message(shuffled_text)



@tree.command(name="シャッフル", description="入力した文字をバラバラに並べ替えます。")
@discord.app_commands.describe(text="シャッフルしたい文字列")
async def shuffle_command(interaction: discord.Interaction, text: str):

    char_list = list(text)
    random.shuffle(char_list)
    
    shuffled_text = "".join(char_list)
    
    await interaction.response.send_message(shuffled_text)

# メッセージを右クリック > アプリ > X動画を埋め込み表示 から実行
@tree.context_menu(name="X動画を埋め込み表示")
async def fix_x_video(interaction: discord.Interaction, message: discord.Message):
    content = message.content
    
    # リンクが含まれているか確認
    if "x.com" in content or "twitter.com" in content:
        # ドメインを vxtwitter.com に置換
        # これにより、Discord上でMP4として再生・保存可能なプレイヤーが表示されます
        fixed_url = content.replace("x.com", "vxtwitter.com").replace("twitter.com", "vxtwitter.com")
        
        await interaction.response.send_message(f"動画を見やすくしたよ！\n{fixed_url}")
    else:
        await interaction.response.send_message("メッセージの中にX（Twitter）のリンクが見つかりませんでした。", ephemeral=True)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await tree.sync()
    print("スラッシュコマンドを同期しました。")
    activity = discord.CustomActivity(name="🗿🍷ガチイク！")
    await client.change_presence(activity=activity)

    try:
        # 通知先のチャンネルオブジェクトを取得
        channel = client.get_channel(NOTIFICATION_CHANNEL_ID)
        
        if channel:
            # タイムゾーンをJST (UTC+9) に設定
            jst = datetime.timezone(datetime.timedelta(hours=9))
            now = datetime.datetime.now(jst)

            commit_hash = os.environ.get("RENDER_GIT_COMMIT")
            branch_name = os.environ.get("RENDER_GIT_BRANCH")


            embed = discord.Embed(
                title="✅ BOT起動完了",
                description="BOTが再起動しました。応答内容が更新されています。",
                color=discord.Color.green(),
                timestamp=now  # Embedのフッターにタイムスタンプを表示
            )
            

            if branch_name:
                embed.add_field(name="ブランチ", value=branch_name, inline=True)
                
            if commit_hash:
                # コミットハッシュが長い場合は、先頭7文字だけ表示する
                short_hash = commit_hash[:7]
                embed.add_field(name="コミット", value=f"`{short_hash}`", inline=True)

                
            embed.set_footer(text=f"起動時刻 (JST)")

            await channel.send(embed=embed)
            print(f"チャンネル (ID: {NOTIFICATION_CHANNEL_ID}) に起動通知を送信しました。")
            
        else:
            print(f"エラー: 通知用チャンネル (ID: {NOTIFICATION_CHANNEL_ID}) が見つかりません。")

    except Exception as e:
        print(f"通知の送信中にエラーが発生しました: {e}")
try:
    keep_alive()
    print("Webサーバーを起動しました。")
    TOKEN = os.environ['DISCORD_BOT_TOKEN']
    if TOKEN is None:
        raise KeyError("'DISCORD_BOT_TOKEN' が設定されていません。")
    client.run(TOKEN)
except KeyError as e:
    print(f"エラー: 環境変数 {e}")
    print("ホスティングサービス（Render, Fly.ioなど）の環境変数設定を確認してください。")














