import os
from django.utils.translation import gettext_lazy as _

SITE_TITLE = "Django Boilerplate"
SITE_BRAND = ""
SITE_HEADER = "Django Boilerplate"
COPYRIGHT_TEXT = f"Django Boilerplate"
WELCOME_SIGN = _("Welcome to Django Boilerplate Admin")
BRAND_SLOGAN = "A Sensible Boilerplate for Djangonauts"

#######################################
# Currently available UI tweaks       #
# Use the UI builder to generate this #
#######################################

JAZZMIN_UI_TWEAKS = {
    # Small text on the top navbar
    "navbar_small_text": True,
    # Small text on the footer
    "footer_small_text": True,
    # Small text everywhere
    "body_small_text": True,
    # Small text on the brand/logo
    "brand_small_text": BRAND_SLOGAN,
    # brand/logo background colour
    "brand_colour": False,
    # Link colour
    "accent": "accent-primary",
    # topmenu colour
    "navbar": "navbar-white navbar-light",
    # topmenu border
    "no_navbar_border": True,
    # Make the top navbar sticky, keeping it in view as you scroll
    "navbar_fixed": False,
    # Whether to constrain the page to a box (leaving big margins at the side)
    "layout_boxed": False,
    # Make the footer sticky, keeping it in view all the time
    "footer_fixed": False,
    # Make the sidebar sticky, keeping it in view as you scroll
    "sidebar_fixed": True,
    # sidemenu colour
    "sidebar": "sidebar-light-primary",
    # sidemenu small text
    "sidebar_nav_small_text": True,
    # Disable expanding on hover of collapsed sidebar
    "sidebar_disable_expand": False,
    # Indent child menu items on sidebar
    "sidebar_nav_child_indent": True,
    # Use a compact sidebar
    "sidebar_nav_compact_style": True,
    # Use the AdminLTE2 style sidebar
    "sidebar_nav_legacy_style": False,
    # Use a flat style sidebar
    "sidebar_nav_flat_style": False,
    # Bootstrap theme to use (default, or from bootswatch, see THEMES below)
    "theme": "cosmo",
    # Theme to use instead if the user has opted for dark mode (e.g darkly/cyborg/slate/solar/superhero)
    "dark_mode_theme": None,
    # The classes/styles to use with buttons
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": False,
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": SITE_TITLE,
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": SITE_HEADER,
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": SITE_BRAND,
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "images/site_logo.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "images/login_logo.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logodark": "images/login_logodark.png",
    # CSS classes that are applied to the logo above
    "site_logoclasses": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "images/site_icon.png",
    # Welcome text on the login screen
    "welcome_sign": WELCOME_SIGN,
    # Copyright on the footer
    "copyright": COPYRIGHT_TEXT,
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": [
        "accounts.User",
    ],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "avatar_url",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # {'name': 'Site', 'url': '/', 'permissions': ['auth.view_user']},
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index"},
        {"name": "Swagger", "url": "/api/docs/swagger"},
        {"name": "ReDoc", "url": "/api/docs/redoc"},
        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        # model admin to link to (Permissions checked against model)
        {"model": "accounts.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {'app': 'books'},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        {"model": "settings.Setting"},
        {
            "name": "GitHub",
            "url": "https://github.com/mnamegaurav",
            "new_window": True,
        },
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": False,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [
        "socialaccount",
    ],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [
        # "account.EmailAddress",
        # "authtoken.TokenProxy",
        # "token_blacklist.BlacklistedToken",
        # "token_blacklist.OutstandingToken",
        # 'SocialAccount',
        # 'SocialToken',
        # 'SocialApp',
        # "push_notifications.APNSDevice",
        # "push_notifications.WNSDevice",
        # "push_notifications.WebPushDevice",
    ],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # 'order_with_respect_to': ['auth', 'books', 'books.author', 'books.book'],
    # Custom links to append to app groups, keyed on app name
    # 'custom_links': {
    #     'settings': [{
    #         'name': 'Recent Actions',
    #         'url': '/django_boilerplate-secret-admin/recent-actions/',
    #         'icon': 'fas fa-edit',
    #         # 'permissions': ['books.view_book']
    #     }]
    # },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        # Apps
        "auth": "fas fa-users-cog",
        "accounts": "fas fa-user",
        "core": "far fa-id-badge",
        "settings": "fas fa-tools",
        "sites": "fas fa-sitemap",
        "socialaccount": "fas fa-user-friends",
        # Models
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
        "accounts.User": "fas fa-user",
        "accounts.UserGroup": "fas fa-users-cog",
        "settings.Setting": "fas fa-tools",
        "settings.GeneralInformation": "fas fa-scroll",
        "sites.Site": "fas fa-sitemap",
        "socialaccount.SocialAccount": "fas fa-user-friends",
        "socialaccount.SocialToken": "fas fa-mobile",
        "socialaccount.SocialApp": "fas fa-key",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-satellite-dish",
    "default_icon_children": "fas fa-satellite",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    # "related_modal_active": True,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "jazzmin/custom.css",
    "custom_js": "jazzmin/custom.js",
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {
    #     "settings.Setting": "single",
    # },
    # Add a language dropdown into the admin
    "language_chooser": True,
}
