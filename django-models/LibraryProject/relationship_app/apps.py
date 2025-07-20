from django.apps import AppConfig  # 💥 You were missing this import

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'  # ✅ Must match your folder name

    def ready(self):
        import relationship_app.signals  # ✅ Keep it aligned
