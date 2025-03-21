# multiple_modules.py
from admin_privileges import Admin

# Create an Admin instance
admin = Admin("jeremy", "warren", 38, "hendersonville", "software developer")

# Call show_privileges to verify
admin.privileges.show_privileges()
