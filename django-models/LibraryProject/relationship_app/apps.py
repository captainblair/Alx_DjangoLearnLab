from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):  # ✅ Can be named anything
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'  # ✅ MUST match the folder name
