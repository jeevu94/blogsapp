from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, PositiveSmallIntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from blogsapp.users.taxonomies import UserRole


class User(AbstractUser):
    """
    Default custom user model for blogsapp.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = PositiveSmallIntegerField(
        choices=UserRole.choices, default=UserRole.customer
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def can_access_admin_panel(self):
        """Check if user can access admin panel."""

        return self.role == UserRole.admin
