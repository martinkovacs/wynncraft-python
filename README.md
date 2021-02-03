# wynncraft-python
A wrapper for the Wynncraft API, with local caching.

# Install
Requires at least python 3.6
```bash
pip install wynncraft
```

# Information
- **All information returned in JSON format.**<br/><br/>
- **Constants**<br/>
  This wrapper has some variables you can change
  - `CACHE_TIME`: If the data in cache is older than CACHE_TIME seconds, then a new request will be made.
  - `DEFAULT_TIMEOUT`: Specifies a timeout in seconds for http request.<br/><br/>
- **How does caching works?**<br/>
  The default funcions don't use cache at all (`wynncraft.Guild.list()`).<br/>You need to use the cache variants (`wynncraft.cache.Guild.list()`). All functions available with this functionality.<br/>
  It will make a request if:
  - **response hasn't been cached**
  - **data in the cache is older than CACHE_TIME**

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

- [search_itemOnlyIDs](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("itemOnlyIDs", arg)
wynncraft.Ingredient.search_itemOnlyIDs(arg)
```

- [search_consumableOnlyIDs](https://docs.wynncraft.com/Ingredient-API/#search)
```python
# Same as Ingredient.search("consumableOnlyIDs", arg)
wynncraft.Ingredient.search_consumableOnlyIDs(arg)
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

- [search_healthOrDamage](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("healthOrDamage", arg)
wynncraft.Recipe.search_healthOrDamage(arg)
```

- [search_duration](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("duration", arg)
wynncraft.Recipe.search_duration(arg)
```

- [search_basicDuration](https://docs.wynncraft.com/Recipe-API/#search)
```python
# Same as Recipe.search("basicDuration", arg)
wynncraft.Recipe.search_basicDuration(arg)
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

**For more documentation see the [Wynncraft API documentation](https://docs.wynncraft.com/).**
