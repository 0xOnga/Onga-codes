
const Discord = require("discord.js")
const client = new Discord.Client({ intents: [32767] });

const { MessageEmbed } = require('discord.js');
const fetch = require('node-fetch');
const JSON = require('json');
client.on('ready', () => {
    
    console.log("Ready");
    
});



client.on("messageCreate", async (message) => {
    
        
    
    if (message.author.bot) return;
    if (message.content.toLowerCase().includes("?nftdata")){
        prefix = "?nftdata"
        const arg = message.content.slice(prefix.length).trim().split(/ +/g);
        data = await (await fetch('https://jmccmlyu33.medianetwork.cloud/query_volume_per_collection?collection='+arg[0])).json();
        
        const NftE = new MessageEmbed()
            .setColor('#0099ff')
	        .setTitle('Stats for ' + arg)
	        .addFields(
            
		    { name: 'Total Sales', value: "" + data['totalSales'], inline: true },
		    { name: 'Daily average price change', value: ""+data['dailySales'] , inline: true },
            { name: '\u200B', value: '\u200B' , inline: true},

            { name: 'Total Volume', value: "" + data['totalVolume'], inline: true },
		    { name: 'Daily Volume', value: "" +data['dailyVolume'] , inline: true },
            { name: '\u200B', value: '\u200B', inline: true },
            
	             )
	        .setTimestamp()
	        .setFooter('Made by @ongacell#3853 made for COPE | GANG', 'https://i.ibb.co/WyBHK9n/cope-logo.jpg');

        
        await message.channel.send({ embeds: [NftE] });
            }
    }
);


client.login("");







