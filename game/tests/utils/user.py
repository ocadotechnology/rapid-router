from django.contrib.auth.models import User


def get_superuser():
    """Get a superuser for testing, or create one if there isn't one."""
    try:
        return User.objects.get(username="superuser")
    except User.DoesNotExist:
        return User.objects.create_superuser(
            "superuser", "superuser@codeforlife.education", "password"
        )
