import xbmcaddon

ADDON = xbmcaddon.Addon()
META_LANG = 'fr'

DICT = {
    'username_error': {
        'fr': "Nom d'utilisateur non défini",
        'en': 'No username provided'
    },
    'password_error': {
        'fr': 'Mot de passe non défini',
        'en': 'No password provided'
    },
    'login_error': {
        'fr': 'Impossible de se connecter',
        'en': 'Unable to login'
    }
}


def get_text(id: str, lang=META_LANG) -> str:
    if id not in DICT:
        return ''
    if META_LANG not in DICT[id]:
        return ''
    return DICT[id][META_LANG]
