from .islands.adnmb import AdnmbPage
from .islands.nimingban import NiMingBanPage
from .islands.kukuku import KukukuPage


island_class_map = {
    'adnmb': AdnmbPage,
    'nimingban': NiMingBanPage,
    'kukuku': KukukuPage,
}

class IslandSwitcher:
    available_island = island_class_map.keys()

    def __init__(self, island=None):
        self.island = island

    def detect_by_url(self, url):
        for island in self.available_island:
            if island in url:
                self.island = island
                return
        raise ValueError('Unknown url: {}'.format(url))

    @property
    def island_page_model(self):
        return island_class_map[self.island]

    def sanitize_url(self, url):
        return self.island_page_model.sanitize_url(url)


island_switcher = IslandSwitcher()