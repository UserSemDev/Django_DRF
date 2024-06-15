from rest_framework import serializers
from users.models import User, Payments, Subscription
from users.services import retrieve_strip_session


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатор пользователя"""

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'is_superuser', 'is_staff', 'is_active']


class UserRegisterSerializer(serializers.ModelSerializer):
    """Класс сериализатор регистрации пользователя"""

    class Meta:
        model = User
        fields = ['email', 'password']


class UserNotOwnerSerializer(serializers.ModelSerializer):
    """Класс сериализатор отображения профиля пользователя"""

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'is_active']


class PaymentsSerializer(serializers.ModelSerializer):
    """Класс сериализатор платежей"""

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsStatusSerializer(serializers.ModelSerializer):
    """Класс сериализатор статуса платежа"""
    payment_status = serializers.SerializerMethodField()
    class Meta:
        model = Payments
        exclude = ['payment_link',]

    def get_payment_status(self, instance):
        return retrieve_strip_session(instance.payment_id)



class UserDetailSerializer(serializers.ModelSerializer):
    """Класс сериализатор информации пользователя с платежами"""
    payments_list = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'city', 'is_superuser', 'is_staff', 'is_active',
                  'payments_list']


class SubscriptionSerializer(serializers.ModelSerializer):
    """Класс сериализатор подписок """

    class Meta:
        model = Subscription
        fields = '__all__'
