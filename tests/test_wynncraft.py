import unittest

import wynncraft

invalid = "asdasdasdasdasd"


class TestConstants(unittest.TestCase):
    def test_apikey(self):
        self.assertEqual(wynncraft.API_KEY, "")
        wynncraft.API_KEY = "test"
        self.assertEqual(wynncraft.API_KEY, "test")

    def test_cache_time(self):
        self.assertEqual(wynncraft.CACHE_TIME, 300)
        wynncraft.CACHE_TIME = 600
        self.assertEqual(wynncraft.CACHE_TIME, 600)

    def test_timeout(self):
        self.assertEqual(wynncraft.TIMEOUT, 10)
        wynncraft.TIMEOUT = 20
        self.assertEqual(wynncraft.TIMEOUT, 20)

    def test_rate_limiter(self):
        self.assertEqual(wynncraft.RATE_LIMITER, True)
        wynncraft.RATE_LIMITER = False
        self.assertEqual(wynncraft.RATE_LIMITER, False)


class TestGuild(unittest.TestCase):
    def test_list(self):
        self.assertEqual(type(wynncraft.Guild.list()["guilds"]), list)

    def test_stats(self):
        self.assertEqual(wynncraft.Guild.stats("Wynncraft")["name"], "Wynncraft")
        self.assertEqual(wynncraft.Guild.stats(invalid), {"error": "Guild not found"})


class TestIngredient(unittest.TestCase):
    def test_get(self):
        self.assertEqual(wynncraft.Ingredient.get("apple")["code"], 200)

    def test_list(self):
        self.assertEqual(wynncraft.Ingredient.list()["code"], 200)

    def test_search(self):
        self.assertRaises(ValueError, wynncraft.Ingredient.search, invalid, "")
    
    def test_search_name(self):
        self.assertEqual(wynncraft.Ingredient.search_name("apple")["code"], 200)

    def test_search_tier(self):
        self.assertEqual(wynncraft.Ingredient.search_tier("3")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_tier, "100")

    def test_search_level(self):
        self.assertEqual(wynncraft.Ingredient.search_level("100")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_level, "-1")

    def test_search_skills(self):
        self.assertEqual(wynncraft.Ingredient.search_skills("&cooking")["code"], 200)
        self.assertEqual(wynncraft.Ingredient.search_skills("^cooking,armouring")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_skills, "cooking")

    def test_search_sprite(self):
        self.assertEqual(wynncraft.Ingredient.search_sprite("&id<100>")["code"], 200)
        self.assertEqual(wynncraft.Ingredient.search_sprite("^id<100>,damage<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_sprite, "id<100>,damage<100>")

    def test_search_identifications(self):
        self.assertEqual(wynncraft.Ingredient.search_identifications("&speed<0;100>")["code"], 200)
        self.assertEqual(wynncraft.Ingredient.search_identifications("^speed<;>,poison<;>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_identifications, "id<100>,damage<100>")

    def test_search_item_only_ids(self):
        self.assertEqual(wynncraft.Ingredient.search_item_only_ids("&strength<100>")["code"], 200)
        self.assertEqual(wynncraft.Ingredient.search_item_only_ids("^strength<100>,defence<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_item_only_ids, "strength<100>,defence<100>")

    def test_search_consumable_only_ids(self):
        self.assertEqual(wynncraft.Ingredient.search_consumable_only_ids("&duration<100>")["code"], 200)
        self.assertEqual(wynncraft.Ingredient.search_consumable_only_ids("^duration<100>,charges<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Ingredient.search_consumable_only_ids, "duration<100>,charges<100>")


class TestItem(unittest.TestCase):
    def test_database_category(self):
        self.assertEqual(type(wynncraft.Item.database_category("all")["items"]), list)
        self.assertRaises(ValueError, wynncraft.Item.database_category, invalid)
        

    def test_database_search(self):
        self.assertEqual(type(wynncraft.Item.database_search("Idol")["items"]), list)


class TestLeaderboard(unittest.TestCase):
    def test_guild(self):
        self.assertEqual(type(wynncraft.Leaderboard.guild("alltime")["data"]), list)

    def test_player(self):
        self.assertEqual(type(wynncraft.Leaderboard.player("alltime")["data"]), list)

    def test_pvp(self):
        self.assertEqual(type(wynncraft.Leaderboard.pvp("alltime")["data"]), list)


class TestNetwork(unittest.TestCase):
    def test_server_list(self):
        self.assertEqual(len(wynncraft.Network.server_list().keys()) >= 2, True)
    
    def test_player_sum(self):
        self.assertEqual(type(wynncraft.Network.player_sum()["players_online"]), int)


class TestPlayer(unittest.TestCase):
    def test_stats(self):
        self.assertEqual(wynncraft.Player.stats("Salted")["code"], 200)

    def test_uuid(self):
        self.assertEqual(wynncraft.Player.uuid("Salted")["code"], 200)


class TestRecipe(unittest.TestCase):
    def test_get(self):
        self.assertEqual(wynncraft.Recipe.get("Boots-1-3")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.get, invalid)
    
    def test_list(self):
        self.assertEqual(wynncraft.Recipe.list()["code"], 200)

    def test_search(self):
        self.assertRaises(ValueError, wynncraft.Recipe.search, invalid, "")

    def test_search_type(self):
        self.assertEqual(wynncraft.Recipe.search_type("boots")["code"], 200)

    def test_search_skill(self):
        self.assertEqual(wynncraft.Recipe.search_skill("cooking")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_skill, invalid)

    def test_search_level(self):
        self.assertEqual(wynncraft.Recipe.search_level("&min<0>")["code"], 200)
        self.assertEqual(wynncraft.Recipe.search_level("^min<0>,max<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_level, invalid)

    def test_search_durability(self):
        self.assertEqual(wynncraft.Recipe.search_durability("&min<0>")["code"], 200)
        self.assertEqual(wynncraft.Recipe.search_durability("^min<0>,max<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_durability, invalid)

    def test_search_healthOrDamage(self):
        self.assertEqual(wynncraft.Recipe.search_health_or_damage("&min<0>")["code"], 200)
        self.assertEqual(wynncraft.Recipe.search_health_or_damage("^min<0>,max<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_health_or_damage, invalid)

    def test_search_duration(self):
        self.assertEqual(wynncraft.Recipe.search_duration("&min<0>")["code"], 200)
        self.assertEqual(wynncraft.Recipe.search_duration("^min<0>,max<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_duration, invalid)

    def test_search_basicDuration(self):
        self.assertEqual(wynncraft.Recipe.search_basic_duration("&min<0>")["code"], 200)
        self.assertEqual(wynncraft.Recipe.search_basic_duration("^min<0>,max<100>")["code"], 200)
        self.assertRaises(ValueError, wynncraft.Recipe.search_basic_duration, invalid)


class TestSearch(unittest.TestCase):
    def test_name(self):
        self.assertEqual(wynncraft.Search.name("Salted")["search"], "salted")


class TestTerritory(unittest.TestCase):
    def test_list(self):
        self.assertEqual(type(wynncraft.Territory.list()), dict)
