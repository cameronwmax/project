class GameStats:
    """Track stats for Chicken Cross"""

    def __init__(self, cc_game):
        """Initialize stats"""
        self.settings = cc_game.settings
        self.reset_stats()
        self.highest_level = 1

    def reset_stats(self):
        """Initialize stats that can change during game"""
        self.chickens_left = self.settings.chickens_limit
        self.level = 1
        