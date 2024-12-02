import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import random


class SendCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response({'error': 'Укажите номер телефона'}, status=status.HTTP_400_BAD_REQUEST)

        auth_code = str(random.randint(1000, 9999))
        request.session['auth_code'] = auth_code
        request.session['auth_code_time'] = time.time()

        time.sleep(2)

        return Response({'message': 'Код отправлен', 'code': auth_code}, status=status.HTTP_200_OK)


class VerifyCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        # Проверка наличия данных
        if not phone_number or not code:
            return Response({'error': 'Укажите номер телефона и код'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка существования кода в сессии
        auth_code = request.session.get('auth_code')
        auth_code_time = request.session.get('auth_code_time')

        if not auth_code:
            return Response({'error': 'Код не найден. Пожалуйста, запросите новый код.'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка времени жизни кода (например, 5 минут)
        if time.time() - auth_code_time > 300:
            return Response({'error': 'Код истек. Запросите новый код.'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка правильности кода
        if code == auth_code:
            user, created = User.objects.get_or_create(phone_number=phone_number)

            if created:
                # Пользователь создан впервые — генерируем инвайт-код
                user.invite_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
                user.save()
                message = 'Новый пользователь создан и авторизован'
            else:
                message = 'Пользователь успешно авторизован'

            # Очистка кода из сессии
            del request.session['auth_code']
            del request.session['auth_code_time']

            return Response({'message': message, 'user_id': user.id}, status=status.HTTP_200_OK)

        return Response({'error': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get(self, request, user_id):
        try:
            # Получаем текущего пользователя
            user = User.objects.get(id=user_id)

            # Получаем пользователей, которые активировали инвайт-код текущего пользователя
            referrals = User.objects.filter(activated_invite=user)

            # Формируем данные профиля
            profile_data = {
                'phone_number': user.phone_number,
                'invite_code': user.invite_code,
                'activated_invite': user.activated_invite.invite_code if user.activated_invite else None,
                'referrals': [{'id': ref.id, 'phone_number': ref.phone_number} for ref in referrals],
            }

            return Response(profile_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

class ActivateInviteView(APIView):
    def post(self, request, user_id):
        try:
            # Получаем пользователя, который делает запрос
            user = User.objects.get(id=user_id)

            # Проверяем, активировал ли пользователь инвайт ранее
            if user.activated_invite:
                return Response(
                    {'error': f'Вы уже активировали инвайт-код: {user.activated_invite.invite_code}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Получаем инвайт-код из запроса
            invite_code = request.data.get('invite_code')
            if not invite_code:
                return Response({'error': 'Укажите инвайт-код'}, status=status.HTTP_400_BAD_REQUEST)

            # Ищем пользователя, чей инвайт-код был указан
            inviter = User.objects.filter(invite_code=invite_code).first()
            if not inviter:
                return Response({'error': 'Инвайт-код не найден'}, status=status.HTTP_404_NOT_FOUND)

            # Активируем инвайт-код
            user.activated_invite = inviter
            user.save()

            return Response(
                {'message': f'Инвайт-код {invite_code} успешно активирован'},
                status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
