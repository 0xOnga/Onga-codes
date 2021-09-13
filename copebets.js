const Discord = require("discord.js")
const client = new Discord.Client({ intents: [32767] });

const { MessageEmbed } = require('discord.js');
const fetch = require('node-fetch');

client.on('ready', () => {
    
    console.log("Ready");
    
});



client.on("messageCreate", async (message) => {
      
    if (message.author.bot) return;
    /* if(message.author.roles.cache.has(825046599788658728)) CHECK FOR ROLE ID (SO ONLY VERIFIED USER CAN USE IT) this id is the Cyrii role in COPE DISCORD
            if(message.channel)
    */
    
    if (message.content.toLowerCase().includes("?bet")){
        
        /* TRIM OUT ARGS FROM THE COMMAND*/
        prefix = "?bet"
        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        
        /* supposed command example ?bet [arg1: coin name] [arg2: expect price] [arg3: timeframe] 
        current formula to calculate time only accepts minutes as input value, code to accept every timeframe soon
        */

        price1 = await (await fetch('https://api.coingecko.com/api/v3/simple/price?ids='+ args[0] + '&vs_currencies=usd')).json();
        price1 = parseFloat(price1[''+args[0]]['usd'])
        time = args[2]
        
        /* check if call is supposed to be for the upside or downside
        */
        callPrice = parseFloat(args[2])
        if(price1 < callPrice){
            var long = true;
            console.log("we are long")
        }
        else{
            var long = false;
            console.log("we are short")
        }
        console.log(args)
        

        
        /* SHOW BET STATS*/
        
        const betE = new MessageEmbed()
            .setColor('#0099ff')
	        .setTitle('Will ' + args[0] + ' reach ' + args[1] +' in ' + args[2] + 'minutes')
	        .addFields(
            
		    { name: 'Coin', value: "" + args[0], inline: true },
		    { name: 'Expected price', value: "" + args[1], inline: true },
            { name: 'In', value: "" +args[2] + 'minutes', inline: true},
            { name: 'Current price ', value: "" + price1, inline: false },
            { name: 'VOTE ', value: "?yes + cope ammount or ?no ", inline: false },
	             )
	        .setTimestamp()
	        .setFooter('#COPEBETS', 'https://i.ibb.co/WyBHK9n/cope-logo.jpg');

        
        await message.channel.send({ embeds: [betE] });
        time = time * 60000

        /* enable chat in this channel by every user or enable the use of ?yes / ?no commands to vote
          start timer for the end of the bet
        */

        setTimeout(async function(){ 
            
            await message.channel.send("Time over")
            
            price2 = await (await fetch('https://api.coingecko.com/api/v3/simple/price?ids='+ args[0] + '&vs_currencies=usd')).json();
            console.log(price2)
            price2 = parseFloat(price2[''+args[0]]['usd'])
            
            
            console.log(long)

            if(long === true){
                    if(price2 < callPrice ){
                        await message.channel.send("?no wins")
                        /*send cope to ?no */ 
                    }
                    else{
                        await message.channel.send("?yes wins")
                        /*send cope to ?yes */ 
                    }
            }
            /*if we are short */
            else{
                if(price2 < callPrice ){
                    await message.channel.send("?yes wins")
                    /*send cope to ?yes */ 
                }
                else{
                    await message.channel.send("?yes wins")
                    /*send cope to ?yes */ 
                }
            }
            
        }, time);

        

            
            }
    }
);






client.login("");

