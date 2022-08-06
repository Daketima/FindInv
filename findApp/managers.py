from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom user manager that sets email as the unique identifier for authentication"""
    
    use_in_migration = True
    
    def _create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    # def create_user(self, email: str, password: str, **extra_fields) -> object:
    #     """Creates a user and saves with the given email and password.

    #     Args:
    #         email (str): email address given by the user
    #         password (str): password given by the user

    #     Raises:
    #         ValueError: Raise error when email is not entered

    #     Returns:
    #         object: user
    #     """
    #     if not email:
    #         raise ValueError(_("The email must be set"))
    #     email = self.normalize_email(email=email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save()
        
    #     return user
        
    def create_superuser(self, email, password: str, **extra_fields) -> object:
        """Creates a superuser with the given email and password.
        
        Args:
            email (str): email address given by the user
            password (str): password given by the user

        Raises:
            ValueError: Raises an error when is_staff is not true.
            ValueError: Raises an error when is_superuser is not true.

        Returns:
            object: 
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self._create_user(email, password, **extra_fields)
