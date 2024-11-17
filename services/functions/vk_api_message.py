import vk_api
from celery import shared_task
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config.settings import TOKEN_VK
from services.functions.number_order import get_number_order_list
from services.models import Making
from vk_api.upload import VkUpload
import pathlib
project_path = pathlib.Path(__file__).parent.parent.parent

vk_session = vk_api.VkApi(token=TOKEN_VK)
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)
upload = VkUpload(vk_session)

def send_some_message(user_id, some_text):
    session_api.messages.send(user_id=user_id, message=some_text, random_id=get_random_id())
    # vk_session.method('messages.send', {'user_id': id, 'message': some_text, 'random_id': get_random_id()})

def send_some_image(peer_id, image, user_id):
    with open(pathlib.Path(project_path, f'media/{image}'), 'rb') as img_:
        upload_img = upload.photo_messages(photos=[img_, ], peer_id=peer_id)[0]
        pic = 'photo{}_{}'.format(upload_img['owner_id'], upload_img['id'])
        session_api.messages.send(user_id=user_id, random_id=get_random_id(), attachment=pic, message='Сообщение')

def get_help_message(info_):
    first_name = info_[0]['first_name']
    last_name = info_[0]['last_name']
    return (f'Привет {first_name} {last_name}\n'
            f'- Для получения информации о заказе с сайта http://127.0.0.1:8000/ :\n'
            f'  Отправьте сообщение с полученным номером заказа\n'
            f'- Узнать свой id отправьте "мой id"')

def get_order_message(number):
    making = Making.objects.filter(number=number)
    return (f'Заказ №{number} {making[0]} передан на рассмотрение мастеру.\n'
            f'Ожидайте ответа(ответ придет в этой беседе)')

def get_order_image(number):
    making = Making.objects.filter(number=number)
    return making[0].image_one

@shared_task
def start_vk_bot():
    longpool.listen().close()
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id_ = event.user_id
                info = session_api.users.get(user_id=id_)
                peer_id = event.peer_id
                if msg == 'help':
                    send_some_message(id_, get_help_message(info))
                if msg == 'мой id':
                    send_some_message(id_, f'Ваш vk id: {id_}')
                if msg in get_number_order_list():
                    send_some_message(id_, get_order_message(msg))
                    send_some_image(peer_id, get_order_image(msg), id_)