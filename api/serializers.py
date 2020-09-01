from rest_framework import serializers
from glossary.models import Glossary
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Glossary
        fields = ('word',
                  'frequency',
                  'isShow',
                  'desc',
                  'isNew',
                  'account',
                  'glossary_title')

# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#
#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'title',
#             'subtitle',
#             'content',
#             'created_at',
#         )
#         read_only_fields = ('created_at',)
