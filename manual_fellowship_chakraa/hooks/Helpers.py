from typing import Optional, Any
from BaseClasses import MultiWorld
import re

# "Complete 3 dungeons with Helena - Item 04" -> dungeons completed (3), item number (4)
DUNGEON_LOCATION = re.compile(r"^Complete (\d+) dungeons? with .+ - Item (\d+)$")


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    """Drops dungeon checks past the player's dungeons_amount / locations_per_dungeon options,
    so they are never created. Everything else falls back to the default (hero toggles)."""
    from ..Helpers import get_option_value  # imported here, ..Helpers imports this file

    m = DUNGEON_LOCATION.match(location.get("name", ""))
    if m and (int(m.group(1)) > get_option_value(multiworld, player, "dungeons_amount")
              or int(m.group(2)) > get_option_value(multiworld, player, "locations_per_dungeon")):
        return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
