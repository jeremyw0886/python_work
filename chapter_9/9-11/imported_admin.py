# imported_admin.py
from user_admin import Admin

# Create an Admin instance
admin = Admin("jeremy", "warren", 38, "hendersonville", "software developer")

# Call show_privileges to verify the import
admin.privileges.show_privileges()
