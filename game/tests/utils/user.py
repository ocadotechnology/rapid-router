from django.contrib.auth import get_user_model

User = get_user_model()

def get_superuser():
    """Get a superuser for testing, or create one if there isn't one."""
    try:
        return User.objects.get(username="superuser")
    except User.DoesNotExist:
        return User.objects.create_superuser(
            "superuser", "superuser@codeforlife.education", "password"
        )
