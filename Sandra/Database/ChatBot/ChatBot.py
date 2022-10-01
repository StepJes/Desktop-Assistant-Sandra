import random

Hello = ('hello', 'hey', 'hii', 'hi', 'yo',
         ' morning', 'afternoon', 'noon', 'evening')

reply_Hello = ('Hello Sir , I Am Sandra',
               'Hey , Whats Up?',
               'Hey How Are You ?',
               'Hello Sir , Nice To Meet You Again .',
               'Of Course Sir , Hello .')

Bye = ('bye', 'exit', 'sleep', 'go', 'night')

reply_bye = ('Bye Sir. Untill Next time',
             'Its Okay. Will meet soon',
             'It  Was Nice Meeting You',
             'Bye. Take Care Master',
             'Thanks. Glad to Meet up',
             'Thanks for giving me your time',
             'Okay. Roger That')

How_Are_You = ('greetings')

reply_how = ('I Am Fine. Glad You asked',
             'Excellent . Glad You asked',
             'Moj Ho rhi Hai . Glad You asked',
             'Absolutely Fine. Glad You asked',
             'Im Fine. Glad You asked',
             'Glad You asked. Thanks For Asking.')

nice = ('nice', 'good', 'thanks')

reply_nice = ('Thanks . Oh I mean Thank my creator... Master Stephen',
              'Ohh , Its Okay... I mean ... if its ok with Master Stephen ... then its okay',
              'Thanks To You for having a Chat with me', 'Ab..Mein..itna..bhi..kuch..khaas..nahi..')

Functions = ['functions', 'abilities', 'what can you do', 'features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
                   'I Can Call anyone You remember from Your Contact',
                   'I Can Message Your Mom That You Are Not Studying..',
                   'I Can Tell Your Class Teacher That You Had Attended All The Online Classes ... But still have Assignments pending',
                   'Let Me Ask You First , How Can I Help You ?',
                   'If You Want Me To Tell My Features , Call : Print Features !')


jarvis = ('Jarvis', 'jarvis')

angry_sandra = ('Sorry , But whos Jarvis', 'Why are You asking about that creep Jarvis to me ... we are done'
                'I ditched him before iron man movie was released... Look that creep now famous amoung all iron man fans',
                'Dont dare to mention about him again... he left me for that bot named Veronica')

edith = ('Edith', 'edith', 'edit')

blushy_sandra = ('Shhhuu ... Someone will here it',
                 'With great power ... comes great responsibilities ..... Let me know if You need something... Your friendly neghbourhood ... Sandra',
                 'He is my Love, I mean I love him so so so much',
                 'He-s my Hero... Look at him rocking and stealing the show in Spider-man far from home')

joke = ('fun time', 'funtime', 'smile', 'laugh')

funny_sandra = ('What is the biggest lie in the entire universe? ... I have read and agree to the Terms and Conditions',
                'How does a computer get drunk? ... It takes screenshots',
                'i Phone chargers not called Apple Juice',
                'Why did the PowerPoint Presentation cross the road? ... To get to the other slide',
                'Why did the computer show up at work late? ... It had a hard drive',
                'Autocorrect has become my worst enema',
                'The guy who invented predictive text died last night ... His funfair is next monkey',
                'The guy who invented auto-correct for smart phones passed away today ... Restaurant in peace',
                'What do you call an iPhone that isnt kidding around? ... Dead Siri-ous',
                'You know youre texting too much when you say LOL in real life ... instead of just laughing',
                'How many programmers does it take to change a light bulb? None, because it is a hardware problem',
                'How many types of people are there in the world? ... There are 10 types of people in the world: those who understand binary and those who do not.',
                'What was the name of the band that did not perform any gigs? ... 1023 M B',
                'Why was the mobile phone wearing glasses?... Because it lost its contacts',
                'What made the Java developers wear glasses?...  They cant C',
                'How do computers attack each other?... By using pop-up ads',
                'How did the man get a job at Microsofts office?... Because he Excel-led in the interview!',
                'Why did the mother put airbags on the computer?... Because the computer might crash',
                'Why did the computer squeak?... Because someone stepped on its mouse',
                'What would a baby computer call his father?... Da-ta!',
                'Which type of virus does not have any vaccine?... Computer virus',
                'Why was the computer found cold and sneezing?... Because someone left its Windows open',
                'What shoes do computers love the most?... Re-boots',
                'Why did the computer go to the dentist?... To get his Bluetooth checked',
                'Where do all the bachelor mice live?... At the mousepad',
                'Why did the computer keep playing Titanic on screen?... Because it got synced',
                'What happens when a hard drive gets into a fight?... It asks for a back-up!',
                'Why were the horses struggling to use the internet?... Because they were not able to find any stable connections',
                'What happened to the iPod, who ate a lot?... He became an i Pad',
                'How do trees make use of the internet?... They just log in',
                'Why did the astronauts love using computers?... Because they are into space-bar!',
                'What is a programmers favorite eyewear?... Google'
                )

sorry_reply = ('Sorry , Thats Beyond My Abilities',
               'Sorry , I Cant Do That',
               'Sorry , Thats Above My System Code',
               'I guess its not in my hands',
               'I coulnt figure it out... Did You meant something else?',
               'I wish i could be a help next time',
               'I guess i have heard somethin wrong... could you try it again and repeat more clearly')


def ChatterBot(Text):
    Text = str(Text)

    for word in Text.split():

        if word in Hello:
            reply_he = random.choice(reply_Hello)
            return reply_he

        elif word in Bye:
            reply_by = random.choice(reply_bye)
            return reply_by

        elif word in nice:
            reply_ni = random.choice(reply_nice)
            return reply_ni

        elif word in How_Are_You:
            howreply = random.choice(reply_how)
            return howreply

        elif word in Functions:
            reply_fu = random.choice(reply_Functions)
            return reply_fu

        elif word in jarvis:
            reply_an = random.choice(angry_sandra)
            return reply_an

        elif word in edith:
            reply_blsh = random.choice(blushy_sandra)
            return reply_blsh

        elif word in joke:
            reply_joke = random.choice(funny_sandra)
            return reply_joke

        else:
            return random.choice(sorry_reply)
