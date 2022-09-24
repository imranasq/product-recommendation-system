from rest_framework.generics import get_object_or_404


class BaseModelService:
    model_class = None

    def get_user(self):
        return self.request.user

    def prepare_data(self, validated_data):
        return validated_data

    def get_model_class(self):
        assert self.model_class is not None, (
                "%s should include model_class attribute or override get_model_class() method"
                % self.__class__.__name__
        )
        return self.model_class

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        model_class = self.get_model_class()
        request = kwargs.get("request")
        user = self.get_user(request)
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        instance = model_class.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        user = self.get_user(request)
        validated_data['updated_by'] = user

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get(self, **kwargs):
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, **kwargs)
        return instance

    def update_status(self, instance, validated_data, **kwargs):
        instance.is_active = validated_data["is_active"]
        request = kwargs.get("request")
        user = self.get_user(request)
        validated_data['updated_by'] = user
        instance.save()
        return instance

    def all(self, **kwargs):
        model_class = self.get_model_class()
        instances = model_class.objects.filter(**kwargs)
        return instances