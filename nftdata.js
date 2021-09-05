/* NFT DATA TRACKER POWERED BY SOLANALYSIS.COM */
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
        
        
        data = await (await fetch('https://solanalysis-dot-feliz-finance.uc.r.appspot.com/projects/get_all_project_stats')).json();
        
        if(message.content.toLowerCase().includes("apeshit")){i = 0;}
        if(message.content.toLowerCase().includes("aurory")){i = 1;}
        if(message.content.toLowerCase().includes("badgers")){i = 2;}
        if(message.content.toLowerCase().includes("degenape")){i = 3;}
        if(message.content.toLowerCase().includes("frakt")){i = 4;}
        if(message.content.toLowerCase().includes("kaiju")){i = 5;}
        if(message.content.toLowerCase().includes("pixel dudes")){i = 6;}
        if(message.content.toLowerCase().includes("smb")){i = 7;}
        if(message.content.toLowerCase().includes("solanimals")){i = 8;}
        if(message.content.toLowerCase().includes("solbears")){i = 9;}
        if(message.content.toLowerCase().includes("sollamas")){i = 10;}
        if(message.content.toLowerCase().includes("tuco")){i = 11;}
        if(message.content.toLowerCase().includes("solpunks")){i = 12;}
        if(message.content.toLowerCase().includes("ssb")){i = 13;}

        const NftE = new MessageEmbed()
            .setColor('#0099ff')
	        .setTitle('Stats for ' + data.Projects[i].DisplayName)
	        .setThumbnail(data.Projects[i].ImageUrl)
	        .addFields(
            
		    { name: 'Average Price', value: "" + data.Projects[i].AveragePrice, inline: true },
		    { name: 'Daily average price change', value: data.Projects[i].AveragePrice_1D_CHG + "%", inline: true },
            { name: '\u200B', value: '\u200B' , inline: true},

            { name: 'Weekly Volume', value: ""+ data.Projects[i].Volume_7D, inline: true },
		    { name: 'Daily Volume Change', value: data.Projects[i].Volume_1D_CHG + "%", inline: true },
            { name: '\u200B', value: '\u200B', inline: true },
            
            { name: 'Market Cap', value: "" + data.Projects[i].MarketCap, inline: true },
		    { name: 'Max Sell', value: "" + data.Projects[i].MaxPrice, inline: true },
            { name: '\u200B', value: '\u200B' , inline: true},
            
	             )
	        .setTimestamp()
	        .setFooter('Made by @ongacell#3853 powered by solanalysis made for COPE | GANG', 'https://i.ibb.co/WyBHK9n/cope-logo.jpg');

        
        await message.channel.send({ embeds: [NftE] });
            }
    }
);


client.login(""); /* bot token */

