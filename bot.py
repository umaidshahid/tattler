import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

assigned_channel_id = None

class ChannelSelect(discord.ui.Select):
    def __init__(self, channels):
        options = [
            discord.SelectOption(label=channel.name, value=str(channel.id))
            for channel in channels
        ]
        super().__init__(placeholder="Choose a text channel...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        global assigned_channel_id
        assigned_channel_id = int(self.values[0])
        await interaction.response.send_message(f"✅ Set updates to <#{assigned_channel_id}>", ephemeral=True)

class ChannelSelectView(discord.ui.View):
    def __init__(self, channels):
        super().__init__()
        self.add_item(ChannelSelect(channels))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="setchannel", description="Assign a channel for voice updates.")
async def setchannel(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You must be an admin to use this.", ephemeral=True)
        return

    channels = interaction.guild.text_channels
    view = ChannelSelectView(channels)
    await interaction.response.send_message("Pick a channel for voice join notifications:", view=view, ephemeral=True)

@bot.event
async def on_voice_state_update(member, before, after):
    if assigned_channel_id:
        channel = bot.get_channel(assigned_channel_id)
        if channel and after.channel and before.channel != after.channel:
            await channel.send(f"🔔 **{member.display_name}** joined **{after.channel.name}**")

bot.run("MTM2NDMzODQ1MTY3NTIxNzk3MA.GKcQqn.QqnyFLt7xIic0xtjX-FZ11a4cQL4weMxUOHVMI")
