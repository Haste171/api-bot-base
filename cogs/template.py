import interactions

"Uncomment if you want to check if a user has permissions"
# from src.permissions import Permissions, has_permission
class TemplateCog(interactions.Extension):
    def __init__(self, client: interactions.Client):
        """Initializes the client instance so we can interact with it"""
        self.client: interactions.Client = client

    @interactions.extension_command(
        name="test", description="test command"
    )
    async def test_cmd(self, ctx: interactions.CommandContext):
        """Register as an extension command"""
        await ctx.send("Test")


def setup(client: interactions.Client):
    """Crucial setup script to register this cog"""
    TemplateCog(client)