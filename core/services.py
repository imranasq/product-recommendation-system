from rest_framework.generics import get_object_or_404


class BaseModelService:
    model_class = None

    def get_user(self, request):
        return request.user

    def get_model_class(self):
        assert self.model_class is not None, (
                "%s should include model_class attribute or override get_model_class() method"
                % self.__class__.__name__
        )
        return self.model_class

    def create(self, request, validated_data, **kwargs):
        model_class = self.get_model_class()
        user = self.get_user(request)
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        if user.user_type == "Vendor":
            validated_data['vendor'] = user

        instance = model_class.objects.create(**validated_data)
        return instance

    def update(self, request, instance, validated_data, **kwargs):
        user = self.get_user(request)
        validated_data['updated_by'] = user

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    def delete(self, **kwargs):
        instance = self.get()
        instance.delete()

    def get(self, **kwargs):
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, **kwargs)
        return instance

    def update_status(self, request, instance, validated_data):
        instance.is_active = validated_data["is_active"]
        user = self.get_user(request)
        validated_data['updated_by'] = user
        instance.save()
        return instance

    def all(self, **kwargs):
        model_class = self.get_model_class()
        instances = model_class.objects.filter(**kwargs)
        return instances
    
    def admin_user(self, *args, **kwargs):
        return self.request.user.user_type == "Admin" and self.request.user.is_superuser
    
    def vendor_user(self, *args, **kwargs):
        return self.request.user.user_type == "Vendor" and not self.request.user.is_superuser

    def customer_user(self, *args, **kwargs):
        return self.request.user.user_type == "Customer" and not self.request.user.is_superuser