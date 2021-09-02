# Daily Updates and Documentation

This markdown file contains daily updates on progress that is made during a livestream. The corresponding label relates to the stream that the progress came from. Series title: Day ### of coding Python Bots until I get affiliate

### September 1st, 2021 (Day 22)
- Created a basic socket server protocol to begin sending packet data from server back to client (accounts.json back to discord bot)
- Idea: When the discord bot sends a command (ex: !account), then retrieve information from server and pass it back to the client to display in the discord channel.

---

### August 31th, 2021 (Day 21)
- Created new repository and initialized it with .gitignore, LICENSE, and README.md
- Initialized bot information with the client commands and token (authkey)
- Created on_welcome function and on_message to track user and message being sent using discord.ext
- Created a sample function called !sayhi to say hi to the bot while it is in the server
- Ran the bot using client.run(token)