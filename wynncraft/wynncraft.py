import re

import wynncraft.utils.data as data
from wynncraft.utils.constants import (
    REGEX_CHECK,
    URL_V1,
    URL_V2,
    URL_V3,
    URL_WYNNTILS,
    INGREDIENT_QUERIES,
    SKILLS,
    SPRITES,
    IDENTIFICATIONS,
    ITEM_ONLY_IDS,
    CONSUMABLE_ONLY_IDS,
    ITEM_CATEGORIES,
    RECIPE_CATEGORIES,
    RECIPE_QUERIES,
    RECIPE_MIN_MAX,
)


class Guild:
    # https://docs.wynncraft.com/Guild-API/

    url = URL_V1 + "guild"
    
    @staticmethod
    def list():
        url = Guild.url + "List"
        return data.get(url)
    
    @staticmethod
    def stats(guild_name):
        url = Guild.url + f"Stats&command={guild_name}"
        return data.get(url)


class Ingredient:
    # https://docs.wynncraft.com/Ingredient-API/

    url = URL_V2 + "ingredient/"

    @staticmethod
    def get(name):
        url = Ingredient.url + f"get/{name}"
        return data.get(url)

    @staticmethod
    def list():
        url = Ingredient.url + "list/"
        return data.get(url)
    
    @staticmethod
    def search(query, arg):
        url = Ingredient.url + "search/"

        if REGEX_CHECK:
            raise_error = False
            
            if query == "name":
                pass

            elif query == "tier":
                if not (0 <= int(arg) <= 3):
                    raise_error = True

            elif query == "level":
                if int(arg) < 0:
                    raise_error = True

            elif query == "skills":
                re.IGNORECASE = True
                regex = re.compile(f"^[&^]({'|'.join(SKILLS)})(,({'|'.join(SKILLS)}))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True

            elif query == "sprite":
                re.IGNORECASE = False
                regex = re.compile(f"^[&^](({'|'.join(SPRITES)})<\d+>)(,(({'|'.join(SPRITES)})<\d+>))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True

            elif query == "identifications":
                re.IGNORECASE = True
                regex = re.compile(f"^[&^](({'|'.join(IDENTIFICATIONS)})<\d*;\d*>)(,(({'|'.join(IDENTIFICATIONS)})<\d*;\d*>))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True

            elif query == "itemOnlyIDs":
                re.IGNORECASE = False
                regex = re.compile(f"^[&^](({'|'.join(ITEM_ONLY_IDS)})<\d+>)(,(({'|'.join(ITEM_ONLY_IDS)})<\d+>))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True

            elif query == "consumableOnlyIDs":
                re.IGNORECASE = False
                regex = re.compile(f"^[&^](({'|'.join(CONSUMABLE_ONLY_IDS)})<\d+>)(,(({'|'.join(CONSUMABLE_ONLY_IDS)})<\d+>))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True

            else:
                raise ValueError(f"Ingredient.search() invaild query: '{query}'")
        
            if raise_error:
                raise ValueError(f"Ingredient.search() invaild argument for {query} query: {arg}")

        url += f"{query}/{arg}"
        return data.get(url)
    
    @staticmethod
    def search_name(arg):
        return Ingredient.search("name", arg)

    @staticmethod
    def search_tier(arg):
        return Ingredient.search("tier", arg)

    @staticmethod
    def search_level(arg):
        return Ingredient.search("level", arg)

    @staticmethod
    def search_skills(arg):
        return Ingredient.search("skills", arg)

    @staticmethod
    def search_sprite(arg):
        return Ingredient.search("sprite", arg)

    @staticmethod
    def search_identifications(arg):
        return Ingredient.search("identifications", arg)

    @staticmethod
    def search_item_only_ids(arg):
        return Ingredient.search("itemOnlyIDs", arg)

    @staticmethod
    def search_consumable_only_ids(arg):
        return Ingredient.search("consumableOnlyIDs", arg)

class Item:
    # https://docs.wynncraft.com/Item-API/

    url = URL_V1 + "item"
    
    @staticmethod
    def database_category(category):
        if category not in ITEM_CATEGORIES:
            raise ValueError(f"Item.database_category() invaild category: {category}")

        url = Item.url + f"DB&category={category}"
        return data.get(url)
    
    @staticmethod
    def database_search(name):
        url = Item.url + f"DB&search={name}"
        return data.get(url)


class Leaderboard:
    # https://docs.wynncraft.com/Leaderboard-API

    url = URL_V1 + "statsLeaderboard"

    @staticmethod
    def guild(timeframe):
        url = Leaderboard.url + f"&type=guild&timeframe={timeframe}"
        return data.get(url)
    
    @staticmethod
    def player(timeframe):
        url = Leaderboard.url + f"&type=player&timeframe={timeframe}"
        return data.get(url)

    @staticmethod
    def pvp(timeframe):
        url = Leaderboard.url + f"&type=pvp&timeframe={timeframe}"
        return data.get(url)


class Network:
    # https://docs.wynncraft.com/Network-API/

    url = URL_V1 + "onlinePlayers"

    @staticmethod
    def server_list():
        url = Network.url
        return data.get(url)

    @staticmethod
    def player_sum():
        url = Network.url + "Sum"
        return data.get(url)


class Player:
    # https://docs.wynncraft.com/Player-API/

    url = URL_V2 + "player/"

    @staticmethod
    def stats(player):
        url = Player.url + f"{player}/stats"
        return data.get(url)

    @staticmethod
    def uuid(username):
        url = Player.url + f"{username}/uuid"
        return data.get(url)


class Recipe:
    # https://docs.wynncraft.com/Recipe-API/

    url = URL_V2 + "recipe/"
    
    @staticmethod
    def get(name):
        re.IGNORECASE = False
        regex = re.compile(f"^({'|'.join(cat.capitalize() for cat in RECIPE_CATEGORIES)})-\d+-\d+$")
        if not re.fullmatch(regex, name):
            raise ValueError(f"Recipe.get() invaild name: {name}")

        url = Recipe.url + f"get/{name}"
        return data.get(url)
    
    @staticmethod
    def list():
        url = Recipe.url + "list"
        return data.get(url)

    @staticmethod
    def search(query, arg):
        url = Recipe.url + "search/"

        if REGEX_CHECK:
            raise_error = False

            if query == "type":
                pass

            elif query == "skill":
                re.IGNORECASE = True
                regex = re.compile(f"({'|'.join(SKILLS)})")
                if not re.fullmatch(regex, arg):
                    raise_error = True
            
            elif query in ["level", "durability", "healthOrDamage", "duration", "basicDuration"]:
                re.IGNORECASE = False
                regex = re.compile(f"^[&^](({'|'.join(RECIPE_MIN_MAX)})<\d+>)(,(({'|'.join(RECIPE_MIN_MAX)})<\d+>))*$")
                if not re.fullmatch(regex, arg):
                    raise_error = True
            
            else:
                raise ValueError(f"Recipe.search() invaild query: '{query}'")

            if raise_error:
                raise ValueError(f"Recipe.search() invaild argument for {query} query: {arg}")

        url += f"{query}/{arg}"
        return data.get(url)

    @staticmethod
    def search_type(arg):
        return Recipe.search("type", arg)

    @staticmethod
    def search_skill(arg):
        return Recipe.search("skill", arg)

    @staticmethod
    def search_level(arg):
        return Recipe.search("level", arg)
    
    @staticmethod
    def search_durability(arg):
        return Recipe.search("durability", arg)

    @staticmethod
    def search_health_or_damage(arg):
        return Recipe.search("healthOrDamage", arg)

    @staticmethod
    def search_duration(arg):
        return Recipe.search("duration", arg)

    @staticmethod
    def search_basic_duration(arg):
        return Recipe.search("basicDuration", arg)


class Search:
    # https://docs.wynncraft.com/Search-API/

    url = URL_V1 + "statsSearch"

    @staticmethod
    def name(name):
        url = Search.url + f"&search={name}"
        return data.get(url)


class Territory:
    # https://docs.wynncraft.com/Territory-API/

    url = URL_V1 + "territoryList"

    @staticmethod
    def list():
        url = Territory.url
        return data.get(url)


class Extra:
    """
    A few Wynncraft v3 API endpoints.
    After official documentation, these will be moved to the appropriate classes.
    Undocumented, subject to name change or removal.
    IMPORTANT: These return lists not dicts.
    """

    @staticmethod
    def latest_news():
        url = URL_V3 + "latest-news"
        return data.get(url)

    @staticmethod
    def latest_tweets():
        url = URL_V3 + "latest-tweets"
        return data.get(url)
    

    """
    Wynntils API endpoints (not official).
    Undocumented, subject to name change or removal.
    """

    @staticmethod
    def gathering_spots():
        url = URL_WYNNTILS + "gatheringSpots"
        return data.get(url)

    @staticmethod
    def server_list():
        url = URL_WYNNTILS + "serverList"
        return data.get(url)
