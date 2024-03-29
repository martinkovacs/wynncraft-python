# wynncraft-python
A simple wrapper for the Wynncraft API, with caching.

# Install
Requires at least python 3.6
```bash
pip install wynncraft
```

# Information
- **All information returned in JSON format.**
- **For incorrect inputs `ValueError` is raised.**
- **To disable caching, set `CACHE_TIME` to `0`**

# Constants
| Constant        | Type    | Descrpition                                      | Default Value |
| --------------- | ------- | ------------------------------------------------ | ------------- |
| `API_KEY`       | String  | Your API key. (Not required, but recommended)    | `""`          |
| `CACHE_TIME`    | Nubmer  | How long does a cached response is usable.       | `300`         |
| `RATE_LIMITER`  | Boolean | Enables the rate limiter.                        | `True`        |
| `REGEX_CHECK`   | Boolean | Checks the syntax of the argument.               | `True`        |
| `TIMEOUT`       | Number  | Specifies a timeout in seconds for http request. | `10`          |

<br>

# Functions
### Guild
- [list](https://docs.wynncraft.com/Guild-API/#list)
```python
wynncraft.Guild.list()
```

- [stats](https://docs.wynncraft.com/Guild-API/#statistics)
```python
wynncraft.Guild.stats("Wynncraft")
```

### Ingredient
- [get](https://docs.wynncraft.com/Ingredient-API/#get)
```python
wynncraft.Ingredient.get("apple")
```

- [list](https://docs.wynncraft.com/Ingredient-API/#list)
```python
wynncraft.Ingredient.list()
```

- [search](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Valid queries: name, tier, level, skills, sprite, identifications, itemOnlyIDs, consumableOnlyIDs
wynncraft.Ingredient.search(query, arg)
```

- [search_name](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("name", arg)
wynncraft.Ingredient.search_name(arg)
```

- [search_tier](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("tier", arg)
wynncraft.Ingredient.search_tier(arg)
```

- [search_level](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("level", arg)
wynncraft.Ingredient.search_level(arg)
```

- [search_skills](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("skills", arg)
wynncraft.Ingredient.search_skills(arg)
```

- [search_sprite](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("sprite", arg)
wynncraft.Ingredient.search_sprite(arg)
```

- [search_identifications](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("identifications", arg)
wynncraft.Ingredient.search_identifications(arg)
```

- [search_item_only_ids](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("itemOnlyIDs", arg)
wynncraft.Ingredient.search_item_only_ids(arg)
```

- [search_consumable_only_ids](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("consumableOnlyIDs", arg)
wynncraft.Ingredient.search_consumable_only_ids(arg)
```

### Item
- [database_category](https://docs.wynncraft.com/Item-API/#database)
```python
# Valid categories: all, boots, bow, bracelet, chestplate, dagger, helmet, leggings, necklace, ring, spear, wand
wynncraft.Item.database_category(all)
```

- [database_search](https://docs.wynncraft.com/Item-API/#database)
```python
wynncraft.Item.database_search("Idol")
```

### Leaderboard
- [guild](https://docs.wynncraft.com/Leaderboard-API/#guild)
```python
wynncraft.Leaderboard.guild(timeframe)
```

- [player](https://docs.wynncraft.com/Leaderboard-API/#player)
```python
wynncraft.Leaderboard.player(timeframe)
```

- [pvp](https://docs.wynncraft.com/Leaderboard-API/#pvp)
```python
wynncraft.Leaderboard.pvp(timeframe)
```

### Network
- [server_list](https://docs.wynncraft.com/Network-API/#server-list)
```python
wynncraft.Network.server_list()
```

- [player_sum](https://docs.wynncraft.com/Network-API/#player-sum)
```python
wynncraft.Network.player_sum()
```

### Player
- [stats](https://docs.wynncraft.com/Player-API/#statistics)
```python
wynncraft.Player.stats("Salted")
```

- [uuid](https://docs.wynncraft.com/Player-API/#uuid)
```python
wynncraft.Player.uuid("Salted")
```

### Recipe
- [get](https://docs.wynncraft.com/Recipe-API/#get)
```python
wynncraft.Recipe.get("Boots-1-3")
```

- [list](https://docs.wynncraft.com/Recipe-API/#list)
```python
wynncraft.Recipe.list()
```

- [search](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Valid queries: type, skill, level, durability, healthOrDamage, duration, basicDuration
wynncraft.Recipe.search(query, arg)
```

- [search_type](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("type", arg)
wynncraft.Recipe.search_type(arg)
```

- [search_skill](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("skill", arg)
wynncraft.Recipe.search_skill(arg)
```

- [search_level](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("level", arg)
wynncraft.Recipe.search_level(arg)
```

- [search_durability](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("durability", arg)
wynncraft.Recipe.search_durability(arg)
```

- [search_health_or_damage](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("healthOrDamage", arg)
wynncraft.Recipe.search_health_or_damage(arg)
```

- [search_duration](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("duration", arg)
wynncraft.Recipe.search_duration(arg)
```

- [search_basic_duration](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("basicDuration", arg)
wynncraft.Recipe.search_basic_duration(arg)
```

### Search
- [name](https://docs.wynncraft.com/Search-API/#name)
```python
wynncraft.Search.name("Salted")
```

### Territory
- [list](https://docs.wynncraft.com/Territory-API/#list)
```python
wynncraft.Territory.list()
```

### Extra
#### Wynncraft v3 API endpoints
After official documentation, these will be moved to the appropriate classes. Undocumented, subject to name change or removal. **These return lists not dicts.**

- [latest_news](https://web-api.wynncraft.com/api/v3/latest-news)
```python
wynncraft.Extra.latest_news()
```

- [latest_tweets](https://web-api.wynncraft.com/api/v3/latest-tweets)
```python
wynncraft.Extra.latest_tweets()
```

#### Wynntils API endpoints (not official)
Undocumented, subject to name change or removal.

- [gathering_spots](https://athena.wynntils.com/cache/get/gatheringSpots)
```python
wynncraft.Extra.gathering_spots()
```

- [server_list](https://athena.wynntils.com/cache/get/serverList)
```python
wynncraft.Extra.server_list()
```

## **For more documentation see the [Wynncraft API documentation](https://docs.wynncraft.com/).**
