from django.core.management import execute_from_command_line
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ExpenseTracker.settings")
execute_from_command_line()