from django.contrib import admin
from Utilisateurs.models import MonModel
from Evernements.models import Evenement
from Articles.models import Article
from Publicites.models import Publicite


admin.site.register( Evenement)
admin.site.register( Article)
admin.site.register( MonModel)
admin.site.register( Publicite)
