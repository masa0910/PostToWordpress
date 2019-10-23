from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from datetime import datetime

# wordpressのユーザー名，パスワード，url
user_name = "set user_name"
password = "set password"
url="set url"

wp = Client(url, user_name, password)
#保存した名前
save_name = 'set image file path'
data = {
    'name':'set name',
    'type':'image/png',
}
#save_nameのIDを取得
with open(save_name,'rb') as img:
     data['bits'] = xmlrpc_client.Binary(img.read())
response = wp.call(media.UploadFile(data))
attachment_id = response['id']
print(response)
# 投稿する
post = WordPressPost()
# タイトル
post.title = 'set title'
# 投稿内容
post.content = 'set content'
#アイキャッチ画像の設定
post.thumbnail = attachment_id
# タグの設定
post.terms_names = {
    'post_tag': ['set tag',],
    'category': ['set category']
}

# 投稿URL
#post.slug = '自身のサイトURL'

# 投稿ステータス。
# 投稿する場合は下。
post.post_status = 'publish'
#post.post_status = 'draft'
# 下書き指定の場合は下
# post.post_status = 'draft'

wp.call(NewPost(post))
print('投稿完了')