class ExtraFieldsSerializerMixin:
    extra_fields = []

    """
    This custom model serializer mixin is defined to specify a extra_fileds maeta attribute,
    so that extra_fields can be added without affecting '__all__' fields value.
    """

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, "extra_fields", None):
            return list(expanded_fields) + list(self.Meta.extra_fields)
        else:
            return expanded_fields
