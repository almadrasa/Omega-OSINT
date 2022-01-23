###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
import asyncio
from .Resources import console, coloring
from .Nodes import *
###################################################
class run:
    
    def __init__(self, command):
        options = {
            "help": run.help,
            "twitter": run.twitter,
            "instagram": run.instagram,
            "exit": console.quit,
            "clear": console.clear,
            "cls": console.clear,
            "ascii": console.ascii
        }
        if command in options:
            options[command]()
        else: 
            return

    def social(media):
        def wrapper():
            query = media(input(f"\n  -> Enter {media.__name__} Query: "))
            # Add \n to results
            return query
        return wrapper

    def help():
        print(f"""
  {coloring.WHITE}-------------------------------------------------- 
  [{coloring.WARNING}!{coloring.WHITE}] Commands: {coloring.BLUE}[command name]{coloring.WHITE}
  {coloring.BLUE}Name:          {coloring.BLUE}Description:
        
  {coloring.WARNING}help        {coloring.WHITE}Creates specified number of GCs with tokens.
  {coloring.WARNING}clear       {coloring.WHITE}Clears terminal of all print. Alias cls.
  {coloring.WARNING}ascii       {coloring.WHITE}Prints terminal art.
  {coloring.WARNING}exit        {coloring.WHITE}Terminates script.
  {coloring.WARNING}twitter     {coloring.WHITE}Searches Twitter for keyword.
  {coloring.WARNING}instagram   {coloring.WHITE}Searches Instagram for keyword.
  --------------------------------------------------
        """)

    @social
    def twitter(query):
        asyncio.run(Twitter().search(query))

    @social
    def instagram(query): 
        asyncio.run(Instagram().search(query))
###################################################
# seriously well done very swag
# Me > you? cry about it ok go work on facebook osint
# no u skid :rage: