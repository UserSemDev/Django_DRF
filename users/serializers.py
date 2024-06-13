from rest_framework import serializers
from users.models import User, Payments, Subscription


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
