import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!복제'):
        if message.author.guild_permissions.manage_messages:
            new = await message.channel.clone()
            nposition = message.channel.position
            await new.edit(position=nposition)
            embed = discord.Embed(title='채널 복제 완료', color=0x2f3136)
            embed.add_field(name='**채널 복제 명령어 사용자**',value=message.author.mention, inline=False)
            embed.add_field(name='**채널 이름**',value=new.name,inline=False)
            await new.send(embed=embed)
            await new.send(message.author.mention)

    if message.content.startswith('!재생성'):
        if message.author.guild_permissions.manage_messages:
            new = await message.channel.clone()
            nposition = message.channel.position
            await new.edit(position=nposition)
            await message.channel.delete()
            embed = discord.Embed(title='채널 재생성 완료', color=0x2f3136)
            embed.add_field(name='**채널 재생성 명령어 사용자**',value=message.author.mention, inline=False)
            embed.add_field(name='**채널 이름**',value=new.name,inline=False)
            await new.send(embed=embed)
            await new.send(message.author.mention)

client.run('token')
