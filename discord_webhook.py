from discord_webhooks import DiscordWebhooks

WEBHOOK_URL = 'https://discordapvhfevbuvwhrb (webhook here


def send_msg(username, follower_change, followers, unfollowers,
             followers_count, unfollowers_count, time, webhook_url):

    WEBHOOK_URL = webhook_url

    if followers == [] and unfollowers == []:
        print("No change in followers, so not sending message to discord")
        return

    if followers == []:
        followers = 'None'

    if unfollowers == []:
        unfollowers = 'None'

    webhook = DiscordWebhooks(WEBHOOK_URL)

    webhook.set_content(title='Report for %s' % (time),
                        description="Here's your report with :heart:")

   
    webhook.set_footer(text='-- Navaneethan')


    webhook.add_field(name='Username', value=username)
    webhook.add_field(name='Total follower change', value=follower_change)

    if unfollowers != 'None':
        webhook.add_field(name='People who unfollowed you (%d)' %
                          (unfollowers_count),
                          value=', '.join(unfollowers))
    else:
        webhook.add_field(name='People who unfollowed you (%d)' %
                          (unfollowers_count),
                          value=unfollowers)

    if followers != 'None':
        webhook.add_field(name='People who followed you (%d)' %
                          (followers_count),
                          value=', '.join(followers))
    else:
        webhook.add_field(name='People who followed you (%d)' %
                          (followers_count),
                          value=followers)

    webhook.send()

    print("Sent message to discord")
