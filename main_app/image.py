from PIL import Image, ImageDraw, ImageFont
import glob

def image_card(hospital_name):
    text = hospital_name

    img = Image.open('static/img/card-template.jpg')
    imagesize = img.size
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("meiryo.ttc", 128)
    size = font.getsize(text)

    draw.text(((imagesize[0] - size[0])/2, (imagesize[1] - size[1])/3), text, font=font, fill=(0,0,0))

    text = 'の実習クチコミ'
    font = ImageFont.truetype("meiryo.ttc", 96)
    draw.text(((imagesize[0] - size[0])*3/5, (imagesize[1] - size[1])/2), text, font=font, fill=(0,0,0))
    # ファイルを保存
    try: #本番環境用
        img.save('/var/www/mysite/media/media/'+hospital_name+'-card.png', 'PNG', quality=100, optimize=True)
    except FileNotFoundError: # 開発環境
        pass
        #localでtwitter-cardはいらないので省略
        #img.save('media/images/'+hospital_name+'-card.png', 'PNG', quality=100, optimize=True)
