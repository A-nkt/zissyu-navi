# zissyu-navi
このリポジトリは、個人開発によるwebサービスとして開発・公開したものの、現在はクローズしたリポジトリになります。
- 開発期間：2021/1 ~ 2021/2

## 使用した技術
- 言語：HTML, CSS, JavaScript, Python
- FW：bootstrap, JQuery, Django
- その他：Git, GitHub, Slack, Adobe XD, GA

## 本番環境（※現在は、クローズ済みです）
- クラウド : Degital Ocean, GCP
- OS : Ubuntu
- Webサーバー：Nginx
- DB：MySQL
- メール配信システム：SendGrid

## 本プロジェクトに関する概要
### 開発の背景
開発の背景としてあったものは、医療系を専攻する知人との会話がきっかけです。<br>
医療系を専攻する学生は、在学中に実習を経験します。<br>
この実習を通じて、学生は様々なスキルを身に着ける重要な場になっています。<br>
この実習を、病院の立場から見てみると、（学校側から多少の礼金はあるらしいですが）現場における負担になります。<br>
そのため、「卒業・就職のために実習に来ている立場の弱い学生」と「現場の負担になる病院側」で軋轢が生まれます。<br>
この軋轢や管理体制の不十分をきっかけとして、**病院側のパワハラによって学生が自殺する事件**が起きました。<br>
（参考記事：https://www.asahi.com/articles/ASM4854K2M48PTIL011.html）
<br><br>
また、学校側は病院に実習をお願いしている立場であるため、「**学校側で実習先の病院について事前に知る機会は提供されていない**」そうです。（知人談）<br>
そこで、**この情報をpublicに共有・公開し、学生の知る機会を提供することはできないか**と思い、開発しました。
## 実装した機能
- クチコミの閲覧機能・登録機能
CRUDの実装
- 自由コメント機能
- アカウント登録機能<br>
mailアドレスを使用したアカウントの登録・削除・更新機能を作成しました。
- お気に入り登録機能 <br>
アカウントを持つユーザーのみ、お気に入り病院を登録でき、新規のクチコミがあった際は、通知する機能を作成しました。
- ブログ機能
- メール配信機能
## 工夫した点
## 苦労した点
