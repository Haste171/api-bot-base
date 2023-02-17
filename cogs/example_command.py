import interactions
from interactions import Client, CommandContext
from dotenv import load_dotenv
import sys
import api

sys.path.append('../')
api = api.API()

load_dotenv()


class Example(interactions.Extension):
    def __init__(self, client):
        self.client: Client = client

    @interactions.extension_command()
    @interactions.option(name="variable", description="The first variable in your API request", type=str, required=True) # Makes sure to ask for the variable when using the command
    async def example(self, ctx: CommandContext, variable: str): # Make sure the type of variable is the same 
        """This is an example command""" # Command description that shows on Discord when using the command
        if r == None:
            embed = interactions.Embed(title='Error',description=f'Please set up an API in the code!')
            await ctx.send(embeds=embed)
        else: 
            r = api.api_call(variable)
            embed = interactions.Embed(title='Example',description=f'```js\n{r}```')
            await ctx.send(embeds=embed)



def setup(client):
    Example(client)
