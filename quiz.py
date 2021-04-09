import random


quizmaster = { 
 1 : "How many days does it take for the Earth to orbit the Sun?", 
 2 : "Until 1923, what was the Turkish city of Istanbul called?", 
 3 : "What’s the capital of Canada?",
 4 : "Name the longest river in the world",
 5 : "Where was the first modern Olympic Games held?",
 6 : "Which football team is known as ‘The Red Devils’?",
 7 : "What was the most-watched series on Netflix in 2019?",
 8 : "What is the capital of Norway?",
 9 : "What was the downloaded app in 2020?",
 10 : "What is the largest country in the world?",
 11 : "Which nationality was the polar explorer Roald Amundsen?",
 12 : "In bowling, what is the term given for three consecutive strikes?",
 13 : "Who was Donald Trump's vice president?",
 14 : "What was Britney Spears’ first single called?",
 15 : "What is David Bowie’s real name?"
 }

bot1 = {1 : "Thats got to be 365 days, unless it's a leap year ;)",
        2 : "Ankara!",
        3 : "In Canada? This is hard.. Im guessing Vancouver!",
        4 : "Glomma ofcourse!",
        5 : "First olympic games? Qatar!",
        6 : "Soccer? Boooring! Red Devils probably has red shirts, Im guessing Brann from Bergen",
        7 : "Peaky Blinders! You what mate?",
        8 : "Easy! Bergen!",
        9 : "Tinder? Or maybe covid had some impact on it's popularity? Im guessing Tinder",
        10 : "Mother russia!",
        11 : "Roald Amundsen was norwegian!",
        12 : "Triple strike! Easy :)",
        13 : "Condoleezza Rice, duuh!",
        14 : "Genie in a Bottle! Cause im a geeeenie in a booootle!",
        15 : "Bavid Dowie!"
        }

bot2 = {1 : "365!",
        2 : "Constantinople! Im a big history buff so that was easy",
        3 : "Washington!",
        4 : "Longest river..? Danube? Doesn't it go across most of Europe? Probably danube",
        5 : "Athens! History is easy, bring on some diffcult questions Mr. Quizmaster!",
        6 : "Ouugh, soccer? Really. Who cares? Soccer-Team Red Devils FC is my answer!",
        7 : "Ohhh, I know this! Everybody was talking about the one about the meltdown in the nuclear power-plant! Was it called Chernobyl?",
        8 : "Oslo! Come on Mr. Quizmaster, challenge me. I live in Oslo..",
        9 : "Probably that smittesporing-app!",
        10 : "What do you mean by largest? By population? By area? By average BMI? If you are looking for largest as in area its Russia. You have to be more precise in your wording!",
        11 : "Roald was actually a close friend of my great-great-uncle and both were norwegian!",
        12 : "Wait! I think I know the answer. Its the same as a name of a bird.. I think its called 'a rooster'!",
        13 : "Sarah Palin!",
        14 : "How cares? I don't like pop music! Im guessing Barbie Girl!",
        15 : "What? This is a trick question! His name was David Bowie"
        }

bot3 = {1 : "Hmm, theres 12 months in a year, and around 30 days in a month. 30 divided by 12 is around 2. Its got to be 2 days",
        2 : "Istanbul city probably!",
        3 : "Tricky question! Im guessing Ottawa!",
        4 : "Amazon (the river)!",
        5 : "It was held in Athens",
        6 : "Glory, glory Man United!",
        7 : "I remember that there was a big hype around Stranger Things! That's my guess",
        8 : "Oslo!",
        9 : "Tik tok!",
        10 : "Largest? Australia!",
        11 : "Roald? Probably danish!",
        12 : "Im a bowler! Never acheived a turkey yet tho. Turkey is my answer",
        13 : "Mike Pence!",
        14 : "Leave Britney alone! Ohh, hit me baby one more time!",
        15 : "David Bowie? Legend! His birth name was actually David Jones! "
        }

fasit = {1 : "365", 2 : "Constantinople", 3 : "Ottawa", 4 : "The Nile", 5 : "Athens", 6 : "Manchester United", 7 : "Stranger Things",
         8 : "Oslo", 9 : "Tik Tok", 10: "Canada", 11 : "Norwegian", 12 : "A turkey", 13 : "Mike Pence", 14 : "Baby one more time",
         15 : "David Jones"}


x = random.randint(1,15)
print(quizmaster[x])
print(bot1[x])
print(bot2[x])
print(bot3[x])