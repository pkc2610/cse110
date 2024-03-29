choice1= str("\n You’re walking in the woods with your brother, who thinks the teapot on his head makes him look like an elephant. He’s going over different options for his frog’s name when you think you see a sign. Do you want to walk to the SIGN or SUGGEST a frog name?")
sign= str("\n The sign says “Pottsfield, 1 Mile” Your stomach rumbles at the thought of a proper meal in some good old fashioned civilization. You’re about ready to start floating at even the thought of pumpkin pie, but your brother stops you—“I think there’s a bluebird over there!” Do you head for PIE or the BLUEBIRD?")
pie=str(" \n You grab your brother by the hand and start walking toward town, and meander through a mile’s worth of fall-worn woods. As you pass over the crest of a hill, you see the road wind its way down to a quaint little town, just as picturesque as you could ever hope for it to be, packed in on every side by pumpkin patches. The thought crosses your mind—you could probably comfortably roast a pumpkin and eat it, should you just take one now? Or should you go into town for a meal? Do you want to take a PUMPKIN or go into town for a MEAL?")
pumpkin=str(" \n You grab the closest pumpkin to you and twist it until the dried-up vine cracks and releases it. The plant it came from emanates a shudder, which spreads outward from where you stand through every pumpkin plant in sight, making the whole valley shake. You shudder, and take the pumpkin back into the woods. After making a fire, you crack the pumpkin open on a rock and roast the strips piece by piece. You’ll camp here for the night and keep traveling in the morning.")
meal=str(" \n As the buildings get closer, the eerier everything seems. There’s not a single soul in any of the buildings, the entire town is dead silent. Suddenly, you hear music coming from the barn. As you walk in, you realize that everyone inside is wearing pumpkins. Odd, but you walk up to one of the people carving apples. You mention that you’re just hoping to pass through, and a tremor runs through everyone in the barn. Everyone turns to face you, the looks on their faces becoming much more grim. You’re not going to make it out, are you?")
bluebird=str(" \n You follow your brother as he darts through the thick undergrowth and practically trips into a bush that has a bluebird entangled in its branches. As your brother frees the bluebird, she, much to your surprise, starts talking. After the shock wears off, you realize she’s introducing herself—her name is Beatrice—and is offering to take you to a woman named Adelaide who can take you home. You can’t help but think Adelaide can wait until after you’ve gotten pie in the town only a mile away. Do you decide to head toward ADELAIDE or TOWN?")
adelaide=str(" \n The three of you take the right fork in the road, rather than the left one towards Pottsfield. After an hour or so, you see a river up ahead, with a dock leading to a ferry. The passengers of the ferry, oddly enough, are all frogs dressed in some sort of fancy manner. You board the boat, and end up having a lovely ride. When you get to Adelaide’s house, it’s empty. You call for her, but she’s nowhere to be seen. Beatrice looks relieved. Your brother finds a map, and you’re able to use it to lead you home. ")
town=str(" \n The three of you meander through a mile’s worth of fall-worn woods. As you pass over the crest of a hill, you see the road wind its way down to a quaint little town, just as picturesque as you could ever hope for it to be, packed in on every side by pumpkin patches. As the buildings get closer, the eerier everything seems. There’s not a single soul in any of the buildings—the one time you open someone’s door, a turkey is sitting at the table. You decide to keep walking, and pass through the town.")
suggest= str(" \n Your brother doesn’t consider your offhanded offers of “Gandalf” and “Benjamin Franklin Pierce” and insists you take a break and think of a good, proper name for this frog when all of a sudden—you hear someone moving through the forest. They might be a deranged lunatic with an ax, or they could give you directions. Do you ask for DIRECTIONS or keep talking about the FROG?")
directions=str(" \n You start walking towards where you heard the noise coming from, and stumble into a clearing. The woodsman on the other side of the clearing turns, and you feel like a deer caught in headlights as he swings his lantern so the beam of light falls on you. You start to stutter that you’re lost, to which the woodsman insists on getting you somewhere safe, away from the Beast. You don’t know if you trust him fully. Do you FOLLOW the woodsman or RUN?")
frog=str(" \n Your brother sits cross-legged in the middle of the path, and insists you do so as well. He starts counting off all of the “wonderful traits” this frog possesses while you look at your surroundings. As you scan the tops of the trees, you spot a thin path between a break in the trunks. Do you take a break for the TREES or stand up and keep walking on the PATH?")
follow=str(" \n The woodsman leads you down some thin, barely-there paths, winding around until you reach an old grain mill. He unlocks the door and tells you that you should be safe while he works grinding oil from sap-laden trees. He leaves and locks the door behind him. You decide to get some rest and stay the night, and resume your journey in the morning.")
run=str("  \n You grab your brother’s hand and bolt back for the path, the light from the woodsman’s lantern dimming the further you get. At first he runs after you, then stops abruptly. You look back to see why, when you ram into a seemingly hollow figure. You fall back, and look up. The last thing you hear is a deep melodic laugh, and the last things you see are a pair of antlers and those beautiful, hypnotic eyes.")
trees=str(" \n You let your little brother lead as you usher him up this winding path. At the top of a hill, you break through the trees to find an absolutely gorgeous, sprawling mansion as far as the eye can see. Maybe you could ask here for directions. You ring the bell, and, surprisingly, the gates open. The owner of the house bursts open, and, while a little unusual, insists on finding you a carriage to send you on your way. A bit odd, but you make it home.")
path=str(" \n You insist that you keep walking, but it feels like you’re walking in circles. Hours and hours pass, but everything looks the same. It starts to snow. Your little brother’s voice starts grating on you, but you’re so tired. And so cold. So, so, cold. When a deep, melodic voice starts beckoning you, you follow it until you sleep. Your eyes close and you fade away.")


print("As you go through your adventure, your options will appear in all caps. Type which option you want to persue, then hit enter.")

input()

if input(choice1).lower()=="sign":
    if input(sign).lower()=="pie":
        if input(pie).lower()=="pumpkin":
            print(pumpkin)
        else:
            print(meal)
    else:
        if input(bluebird).lower()=="adelaide":
            print(adelaide)
        else:
            print(town)
else:
    if input(suggest).lower()=="directions":
        if input(directions).lower()=="follow":
            print(follow)
        else:
            print(run)
    else:
        if input(frog).lower()=="trees":
            print(trees)
        else:
            print(path)