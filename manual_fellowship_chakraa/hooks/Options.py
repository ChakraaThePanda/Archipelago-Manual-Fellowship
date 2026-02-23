# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class DungeonsAmount(Range):
    """Select the amount of dungeons each Hero has to complete."""
    display_name = "Dungeons Amount per Hero"
    range_start = 1
    range_end = 10
    default = 2

class LocationsPerDungeon(Range):
    """Select the amount of locations each dungeon has."""
    display_name = "Locations per dungeon"
    range_start = 1
    range_end = 10
    default = 4

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["dungeons_amount"] = DungeonsAmount
    options["locations_per_dungeon"] = LocationsPerDungeon
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    options.type_hints["include_helena"].__doc__ = """When set to true, will include Helena in the pool"""
    options.type_hints["include_helena"].display_name = """Include Helena"""
    options.type_hints["include_meiko"].__doc__ = """When set to true, will include Meiko in the pool"""
    options.type_hints["include_meiko"].display_name = """Include Meiko"""
    options.type_hints["include_rime"].__doc__ = """When set to true, will include Rime in the pool"""
    options.type_hints["include_rime"].display_name = """Include Rime"""
    options.type_hints["include_tariq"].__doc__ = """When set to true, will include Tariq in the pool"""
    options.type_hints["include_tariq"].display_name = """Include Tariq"""
    options.type_hints["include_mara"].__doc__ = """When set to true, will include Mara in the pool"""
    options.type_hints["include_mara"].display_name = """Include Mara"""
    options.type_hints["include_elarion"].__doc__ = """When set to true, will include Elarion in the pool"""
    options.type_hints["include_elarion"].display_name = """Include Elarion"""
    options.type_hints["include_ardeos"].__doc__ = """When set to true, will include Ardeos in the pool"""
    options.type_hints["include_ardeos"].display_name = """Include Ardeos"""
    options.type_hints["include_sylvie"].__doc__ = """When set to true, will include Sylvie in the pool"""
    options.type_hints["include_sylvie"].display_name = """Include Sylvie"""
    options.type_hints["include_vigour"].__doc__ = """When set to true, will include Vigour in the pool"""
    options.type_hints["include_vigour"].display_name = """Include Vigour"""
    options.type_hints["include_aeona"].__doc__ = """When set to true, will include Aeona in the pool"""
    options.type_hints["include_aeona"].display_name = """Include Aeona"""
    options.type_hints["include_xavian"].__doc__ = """When set to true, will include Xavian in the pool"""
    options.type_hints["include_xavian"].display_name = """Include Xavian"""

    return options

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
