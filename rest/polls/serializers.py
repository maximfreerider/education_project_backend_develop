from rest_framework import serializers
from polls.models import User, Package, Mode_Of_Study





class ModeOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode_Of_Study
        fields = ('name_of_mos', 'description', 'image_for_presentation', 'text_for_read')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'number_of_credir_card','email', 'date_of_birth')


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('users', 'name_of_package', 'price', 'lenght_discription', 'short_discription')