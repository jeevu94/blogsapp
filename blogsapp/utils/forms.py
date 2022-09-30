from django.forms import Form, ModelForm
from django.forms.forms import BaseForm


class AppBaseForm(BaseForm):
    """
    Base class for the ModelForm and the Form class. This implements some
    common and useful fields and methods. and of course makes things DRY.

    Why is this here?
        1. Without overriding you cannot access the request/view, so helps in validations.
        2. You don't need to do self.cleaned_data['key'], if in case you need to boost performance this is a mess.
    """

    class Meta:
        pass

    def __init__(self, *args, **kwargs):
        """Overridden to get other context data from the view."""

        self.context = kwargs.pop("context", {})
        super().__init__(*args, **kwargs)

    def get_cleaned_data(self, key="__all__", default=None):
        """
        Returns the value from the cleaned data dict based on the given key.
        If in case some other things are to be added, it can be added here.
        This acts as a single point of contact.
        """

        if key == "__all__":
            return self.cleaned_data

        if hasattr(self, "cleaned_data"):
            return self.cleaned_data.get(key, default)

        return self.data.get(key, default)

    def get_user(self):
        """Returns the currently logged in user."""

        request = self.get_request()
        if request:
            return request.user

        return None

    def get_request(self):
        """
        Used as a single point of contact. Just in case the request
        would come from some other ways.
        """

        return self.context.get("request", None)


class AppForm(AppBaseForm, Form):
    """
    The applications normal form. Implements common methods and stuff.

    Consider you are inheriting a form and that form has defined 10 error messages,
    but you want to modify only one error message. You might have to copy all the 10 and
    paste it in the child class.

    This class will reduce this headache. (By default implemented in the ModelForm)

    Note that anything that is defined in the Meta will be higher precedence.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if hasattr(self, "error_messages"):
            # defined in parent class, overridden in child class
            self.error_messages.update(getattr(self.Meta, "custom_error_messages", {}))

    class Meta(AppBaseForm.Meta):
        custom_error_messages = {}


class AppModelForm(AppBaseForm, ModelForm):
    """The applications model form. Implements common methods and stuff."""

    class Meta(AppBaseForm.Meta):
        fields = []
        model = None
        extra_kwargs = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, config in self.Meta.extra_kwargs.items():
            for key, value in config.items():
                setattr(self.fields[field_name], key, value)

    def save(self, commit=True):
        """Set necessary hidden fields on save, like created_by."""

        instance = super().save(commit=commit)

        # setting the anonymous fields
        if hasattr(instance, "created_by") and not instance.created_by:
            instance.created_by = self.get_user()
            instance.save()

        return instance


def get_app_model_form(
    given_model, given_fields="__all__", exclude_fields=["created_by"]  # noqa
):
    """
    This function is used to dynamically generate an AppModelForm. Given the set of inputs.
    This is used to dynamically generate forms for the meta tables.
    """

    class _ModelForm(AppModelForm):
        """The dynamic form that is being generated. This is returned as an output."""

        class Meta(AppModelForm.Meta):
            model = given_model
            fields = given_fields
            exclude = exclude_fields

    return _ModelForm
