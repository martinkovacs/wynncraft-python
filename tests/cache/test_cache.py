import json
import time
import unittest

import wynncraft.cache
import wynncraft.wynncraft

"""
Some compare tests occasionally could fail.
Run 'python -m unittest tests.cahce.test_cache.<Failed test class>' to test it again.
If it repeatedly fails, then please open am issue on github.
"""


def compare(d1, d2):
    if "request" in d1:
        diff = abs(d1["request"]["timestamp"] - d2["request"]["timestamp"])
    else:
        diff = abs(d1["timestamp"] - d2["timestamp"])
    
    return list(d1.keys()) == list(d2.keys()) and diff < 1000


def run_test(function, *args):
    timer = Timer()

    for i in range(10):
        exec(f"{function}{args}")
    
    elapsed_seconds = timer.end()
    return elapsed_seconds <= 1.0


class Timer:
    def __init__(self):
        self.start_seconds = time.time()

    def end(self):
        return time.time() - self.start_seconds


class TestGuild(unittest.TestCase):
    def test_list(self):
        self.assertTrue(compare(wynncraft.wynncraft.Guild.list(), wynncraft.cache.Guild.list()))
        self.assertTrue(run_test("wynncraft.cache.Guild.list"))

    def test_stats(self):
        self.assertTrue(compare(wynncraft.wynncraft.Guild.stats("Wynncraft"), wynncraft.cache.Guild.stats("Wynncraft")))
        self.assertTrue(run_test("wynncraft.cache.Guild.stats", "Wynncraft"))


class TestIngredient(unittest.TestCase):
    def test_get(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.get("apple"), wynncraft.cache.Ingredient.get("apple")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.get", "apple"))
        
    def test_list(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.list(), wynncraft.cache.Ingredient.list()))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.list"))

    def test_search_name(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_name("apple"), wynncraft.cache.Ingredient.search_name("apple")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_name", "apple"))

    def test_search_tier(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_tier("3"), wynncraft.cache.Ingredient.search_tier("3")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_tier", "3"))
        
    def test_search_level(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_level("100"), wynncraft.cache.Ingredient.search_level("100")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_level", "100"))
        
    def test_search_skills(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_skills("^cooking,armouring"), wynncraft.cache.Ingredient.search_skills("^cooking,armouring")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_skills", "^cooking,armouring"))
        
    def test_search_sprite(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_sprite("^id<100>,damage<100>"), wynncraft.cache.Ingredient.search_sprite("^id<100>,damage<100>")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_sprite", "^id<100>,damage<100>"))
        
    def test_search_identifications(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_identifications("^speed<;>,poison<;>"), wynncraft.cache.Ingredient.search_identifications("^speed<;>,poison<;>")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_identifications", "^speed<;>,poison<;>"))
        
    def test_search_item_only_ids(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_item_only_ids("^strength<100>,defence<100>"), wynncraft.cache.Ingredient.search_item_only_ids("^strength<100>,defence<100>")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_item_only_ids", "^strength<100>,defence<100>"))
        
    def test_search_consumable_only_ids(self):
        self.assertTrue(compare(wynncraft.wynncraft.Ingredient.search_consumable_only_ids("^duration<100>,charges<100>"), wynncraft.cache.Ingredient.search_consumable_only_ids("^duration<100>,charges<100>")))
        self.assertTrue(run_test("wynncraft.cache.Ingredient.search_consumable_only_ids", "^duration<100>,charges<100>"))


class TestItem(unittest.TestCase):
    def test_database_category(self):
        self.assertTrue(compare(wynncraft.wynncraft.Item.database_category("all"), wynncraft.cache.Item.database_category("all")))
        self.assertTrue(run_test("wynncraft.cache.Item.database_category", "all"))
        
    def test_database_search(self):
        self.assertTrue(compare(wynncraft.wynncraft.Item.database_search("Idol"), wynncraft.cache.Item.database_search("Idol")))
        self.assertTrue(run_test("wynncraft.cache.Item.database_search", "Idol"))


class TestLeaderboard(unittest.TestCase):
    def test_guild(self):
        self.assertTrue(compare(wynncraft.wynncraft.Leaderboard.guild("alltime"), wynncraft.cache.Leaderboard.guild("alltime")))
        self.assertTrue(run_test("wynncraft.cache.Leaderboard.guild", "alltime"))
        
    def test_player(self):
        self.assertTrue(compare(wynncraft.wynncraft.Leaderboard.player("alltime"), wynncraft.cache.Leaderboard.player("alltime")))
        self.assertTrue(run_test("wynncraft.cache.Leaderboard.player", "alltime"))

    def test_pvp(self):
        self.assertTrue(compare(wynncraft.wynncraft.Leaderboard.pvp("alltime"), wynncraft.cache.Leaderboard.pvp("alltime")))
        self.assertTrue(run_test("wynncraft.cache.Leaderboard.pvp", "alltime"))


class TestNetwork(unittest.TestCase):
    def test_server_list(self):
        self.assertTrue(compare(wynncraft.wynncraft.Network.server_list(), wynncraft.cache.Network.server_list()))
        self.assertTrue(run_test("wynncraft.cache.Network.server_list"))
    
    def test_player_sum(self):
        self.assertTrue(compare(wynncraft.wynncraft.Network.player_sum(), wynncraft.cache.Network.player_sum()))
        self.assertTrue(run_test("wynncraft.cache.Network.player_sum"))


class TestRecipe(unittest.TestCase):
    def test_get(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.get("Boots-1-3"), wynncraft.cache.Recipe.get("Boots-1-3")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.get", "Boots-1-3"))
    
    def test_list(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.list(), wynncraft.cache.Recipe.list()))
        self.assertTrue(run_test("wynncraft.cache.Recipe.list"))

    def test_search_type(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_type("boots"), wynncraft.cache.Recipe.search_type("boots")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_type", "boots"))

    def test_search_skill(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_skill("cooking"), wynncraft.cache.Recipe.search_skill("cooking")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_skill", "cooking"))

    def test_search_level(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_level("^min<0>,max<100>"), wynncraft.cache.Recipe.search_level("^min<0>,max<100>")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_level", "^min<0>,max<100>"))

    def test_search_durability(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_durability("^min<0>,max<100>"), wynncraft.cache.Recipe.search_durability("^min<0>,max<100>")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_durability", "^min<0>,max<100>"))

    def test_search_healthOrDamage(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_health_or_damage("^min<0>,max<100>"), wynncraft.cache.Recipe.search_health_or_damage("^min<0>,max<100>")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_health_or_damage", "^min<0>,max<100>"))

    def test_search_duration(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_duration("^min<0>,max<100>"), wynncraft.cache.Recipe.search_duration("^min<0>,max<100>")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_duration", "^min<0>,max<100>"))

    def test_search_basicDuration(self):
        self.assertTrue(compare(wynncraft.wynncraft.Recipe.search_basic_duration("^min<0>,max<100>"), wynncraft.cache.Recipe.search_basic_duration("^min<0>,max<100>")))
        self.assertTrue(run_test("wynncraft.cache.Recipe.search_basic_duration", "^min<0>,max<100>"))


class TestPlayer(unittest.TestCase):
    def test_stats(self):
        self.assertTrue(compare(wynncraft.wynncraft.Player.stats("Salted"), wynncraft.cache.Player.stats("Salted")))
        self.assertTrue(run_test("wynncraft.cache.Player.stats", "Salted"))

    def test_uuid(self):
        self.assertTrue(compare(wynncraft.wynncraft.Player.uuid("Salted"), wynncraft.cache.Player.uuid("Salted")))
        self.assertTrue(run_test("wynncraft.cache.Player.uuid", "Salted"))


class TestSearch(unittest.TestCase):
    def test_name(self):
        self.assertTrue(compare(wynncraft.wynncraft.Search.name("Salted"), wynncraft.cache.Search.name("Salted")))
        self.assertTrue(run_test("wynncraft.cache.Search.name", "Salted"))


class TestTerritory(unittest.TestCase):
    def test_list(self):
        self.assertTrue(compare(wynncraft.wynncraft.Territory.list(), wynncraft.cache.Territory.list()))
        self.assertTrue(run_test("wynncraft.cache.Territory.list"))
