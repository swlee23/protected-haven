from models import db, Lang, Resource
from app import app

#resets, then creates our basic database
db.drop_all()
db.create_all()

#clears the Lang class database
Lang.query.delete()
# Report.query.delete()

#current language objects in our database
english = Lang(name='English', script='English', form_name='Name', form_email='Email Address', form_phone='Phone Number', form_details='Details of the Incident', form_geoloc="Do not send location")
chinese = Lang(name='Chinese', script='中文', form_name='你的名字', form_email='您的电子邮件地址', form_phone='你的电话号码', form_details='事故详情', form_geoloc="不发送位置")
vietnamese = Lang(name='Vietnamese', script='Tiếng Việt', form_name='Tên của bạn', form_email='Địa chỉ email của bạn', form_phone='Số điện thoại của bạn', form_details='Chi tiết về sự cố', form_geoloc="Không gửi vị trí")
tagalog = Lang(name='Tagalog', script='Tagalog', form_name='Ang pangalan mo', form_email='Ang iyong email address', form_phone='Iyong numero ng telepono', form_details='Mga Detalye ng Insidente', form_geoloc="Huwag magpadala ng lokasyon")


db.session.add_all([english, chinese, vietnamese, tagalog])


db.session.commit()

Resource.query.delete()

eng = Lang.query.get_or_404('English')

test_resource = Resource(text="test", phone='1-800-222-3333', email='test@test.com')

db.session.add(test_resource)
db.session.commit()

resource = Resource.query.get(1)

eng.resources.append(resource)

db.session.commit()

