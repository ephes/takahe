from activities.models.post import Post
from users.views.settings.settings_page import SettingsPage


class InterfacePage(SettingsPage):

    section = "interface"

    options = {
        "toot_mode": {
            "title": "I Will Toot As I Please",
            "help_text": "Changes all 'Post' buttons to 'Toot!'",
        },
        "default_post_visibility": {
            "title": "Default Post Visibility",
            "help_text": "Visibility to use as default for new posts.",
            "choices": Post.Visibilities.choices,
        },
        "visible_reaction_counts": {
            "title": "Show Boost and Like Counts",
            "help_text": "Disable to hide the number of Likes and Boosts on a 'Post'",
        },
    }

    layout = {
        "Posting": ["toot_mode", "default_post_visibility"],
        "Wellness": ["visible_reaction_counts"],
    }
