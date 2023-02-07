from flask_admin import Admin

from backend.admin.views import AdminDashboardView


admin = Admin(name='Crypto Profiles Admin',
              index_view=AdminDashboardView(),
              template_mode='bootstrap3',
              )
