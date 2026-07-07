"""Generate yt_reddit_stories.csv with 25 sub-5-min creepy horror stories
in the voice of popular Reddit horror subreddits (r/nosleep, r/LetsNotMeet,
r/shortscarystories, r/Paranormal, r/TrueScaryStories, r/Glitch_in_the_Matrix).

Modified Script targets 450-550 words for ~3-4 minute narration (under 5 min
at ~150 wpm). Stories are AI-composed originals in those subs' voices.
"""

import csv
from pathlib import Path

stories = [
    # 1
    {
        "title": "The Apartment Has One Extra Room That Wasn't There Yesterday",
        "description": "I've lived here six months. The hallway is one door longer than it used to be. And the neighbor knew. #nosleep #scarystories #horror #creepy #redditstories",
        "content": (
            "I moved into this apartment in November. One bedroom, one bath, kitchen, living room, and a short hallway with a closet "
            "at the end. I've walked that hallway maybe a thousand times. Last Tuesday I came home from work and there was a door at "
            "the end of the hallway. Not the closet. A new door. White, heavy, brass handle. The closet is gone. My lease floor plan "
            "shows a five foot hallway. I measured. It's eleven feet now. I asked the neighbor, who has lived here twenty years, if "
            "her apartment ever changed. She looked at me for a long time. Said, 'you found the door.' Then she shut hers. I hear "
            "breathing on the other side of mine at night. Not knocking. Breathing."
        ),
        "script": (
            "What would you do if your apartment was one room bigger than it used to be? OP is living that exact problem right now.\n\n"
            "She moved into a small one bedroom in November. Nothing special. Kitchen, bath, bedroom, living room, and a short hallway "
            "with a closet at the end. She has walked that hallway, by her own count, more than a thousand times. She knows every "
            "floorboard creak.\n\n"
            "Last Tuesday she comes home from work. Same as always. Drops her bag by the door. Kicks her shoes off. Walks down the "
            "hallway to put her coat in the closet. Except the closet is gone. In its place is a door. A heavy white paneled door "
            "with a brass handle. It looks like it has been there since the building was built. The wood matches the rest of the "
            "apartment perfectly.\n\n"
            "She stands there for fifteen minutes. Just staring. She walks back to the front door. Walks forward again. Same door. "
            "She pulls up the floor plan in her lease. The hallway should be five feet long. She gets a tape measure. It is now "
            "eleven feet long. Six extra feet of apartment that were not there yesterday.\n\n"
            "She tries the handle. Locked. She checks her keychain. There are four keys. Front door. Mailbox. Laundry. And a fourth "
            "key. Smaller. Older. Brass like the handle. She has no memory of the landlord ever giving her this key.\n\n"
            "She calls the landlord. No answer. She calls the building manager. Voicemail. She knocks on her neighbor's door. The "
            "woman next door has lived in the building for twenty years. OP asks her, has your apartment ever, you know, grown? The "
            "neighbor stares at her for a long time. And then says, quote, you found the door. She closes her door without another "
            "word.\n\n"
            "OP went back to her apartment. Put a chair in front of the door. Pushed her dresser against the chair. Slept on the "
            "couch. She says she hears something on the other side of the door at night. Not knocking. Breathing. Slow. Patient. "
            "Like whatever is in there has all the time in the world.\n\n"
            "She posted last night asking for advice. Some commenters said burn the key. Some said try the key. One person, claiming "
            "to live in the same building, replied in all caps, do not open it. They never replied again.\n\n"
            "OP says she's going to wait until morning to decide. Some of us in the comments don't think she has until morning. We'll "
            "know when she updates. If she updates. Subscribe so you don't miss part two."
        ),
    },
    # 2
    {
        "title": "I Babysat For A New Family — The Security Camera In The Living Room Wasn't Theirs",
        "description": "The parents told me to ignore it. Then it turned and followed me. #nosleep #truecrime #creepy #scary #redditstories",
        "content": (
            "I picked up a one off babysitting gig from a parents' Facebook group. New family. Two girls, four and six. The mom "
            "showed me around quickly and pointed to a black security camera in the corner of the living room. 'That's our security "
            "cam, ignore it.' They left. Two hours after the girls were asleep, I noticed the camera had turned. It was pointed "
            "directly at me. The back office door, the one she told me to keep the girls out of, was locked from the outside. I "
            "pressed my ear against it. Slow, even breathing. I got the girls out, called 911 from down the street. Police found a "
            "man inside. He had been living in their walls for months. The parents had no idea."
        ),
        "script": (
            "You would never expect a babysitting job to end with a man being arrested inside a house's walls. But this is one of "
            "the most shared stories on the entire subreddit, and it deserves the audience.\n\n"
            "OP is a college student who picks up babysitting gigs through a local parents' Facebook group. She gets a message from "
            "a new family in the neighborhood. They have two girls, four and six. They need someone for a Friday night. Pay is good. "
            "They give her the address.\n\n"
            "She shows up. The parents are warm. The mom does a quick tour. Kitchen here. Bathroom there. Bedtime is eight thirty. "
            "One rule. Do not let the girls into the back office. The door is locked anyway. Just easier if they don't try.\n\n"
            "On her way out the mom points to a black security camera mounted in the corner of the living room. She says, that's our "
            "security cam, ignore it. It's just pointed at the front door. They leave.\n\n"
            "Two hours pass. Normal night. The girls eat dinner. They watch a movie. They go to bed. OP is on the couch reading. "
            "Around ten thirty she goes into the kitchen for water. She glances back into the living room and stops.\n\n"
            "The camera has moved. It is no longer pointed at the front door. It is now pointed directly at the couch where she had "
            "been sitting.\n\n"
            "She thinks, maybe it's motion tracking. She walks back to the couch. The camera follows her. She walks to the kitchen. "
            "It follows her again. She waves. The camera tilts. Like it is nodding.\n\n"
            "Now her heart is racing. She walks to the back office door. The one the mom said was locked. She tests the handle. "
            "Locked. But here is the thing. It is locked from the outside. There is a deadbolt with the key cylinder on the hallway "
            "side. As if someone inside was being kept in.\n\n"
            "She presses her ear against the door. She hears breathing. Slow. Even. A grown adult's breathing.\n\n"
            "She quietly gets the girls. Bundles them into the car. Drives down the street. Calls 911 from there. Tells them what "
            "she saw. Calls the parents. They don't answer at first. When they call back, panic.\n\n"
            "Police arrive. They open the back office. There is a man inside. He has a sleeping bag, jugs of water, and a laptop with "
            "a live feed of every camera in the house. He had been living in a hidden crawl space behind the office for months. The "
            "family had no idea. He knew their schedule. He knew which child slept which side of the bed. He had been waiting.\n\n"
            "Nobody was physically hurt. The family moved out two weeks later. OP doesn't babysit anymore. Subscribe for the "
            "genuinely scary ones."
        ),
    },
    # 3
    {
        "title": "The Hitchhiker On A Dark Road Kept Whispering My Name",
        "description": "He had no way of knowing it. I had never met him before. #letsnotmeet #nosleep #creepy #scary #redditstories",
        "content": (
            "Two AM. Highway 9. The only car for miles. A man stood on the shoulder in a long coat. I don't pick up hitchhikers but "
            "the weather was awful. I slowed down. He smiled and got in. I asked where he was going. He said, 'wherever you are, "
            "Daniel.' I have never met him. My name is on nothing in my car. After a mile he repeated my name. Then again. Then "
            "again. He never blinked. I pulled over near a gas station, ran inside, asked the clerk to call the cops. When I came "
            "out, the passenger door was open and he was gone. The clerk pulled the security footage. The seat was empty the entire "
            "drive. I had been alone the whole time."
        ),
        "script": (
            "Have you ever picked up a hitchhiker and regretted it? Some people regret it because of who they picked up. OP regrets "
            "it because of what he picked up.\n\n"
            "It is two in the morning. Highway 9. OP is driving home from a late shift. Rain is coming down sideways. He has not "
            "seen another car for fifteen minutes. And then, on the shoulder, standing in the rain with no umbrella, no bag, no "
            "flashlight, is a man in a long coat. He is not waving. He is just standing there. Watching the road.\n\n"
            "OP does not pick up hitchhikers. He never has. But the weather is so bad that he slows down anyway. He stops. He rolls "
            "the passenger window down. He says, where are you headed? The man smiles and gets in.\n\n"
            "OP asks again. Where are you going? The man turns to him. And says, very softly, wherever you are, Daniel.\n\n"
            "OP has never met this man. There is nothing in the car with his name on it. No registration visible. No mail. No badge. "
            "He had been Daniel for thirty four years. This stranger knew it.\n\n"
            "OP says, calmly, how do you know my name. The man does not answer. He just smiles. They drive for a mile in silence. "
            "Then the man says, Daniel. Just the name. Then again. Daniel. Then again. Daniel. He never blinks. His hands stay folded "
            "in his lap. He says the name every fifteen seconds, for two miles.\n\n"
            "OP sees a gas station ahead. He pulls in. He tells the man, I need to grab something. The man smiles. OP gets out, runs "
            "inside, locks the door behind him with his elbow, and asks the night clerk to please call 911. The clerk asks why. OP "
            "tells him.\n\n"
            "They look out the window. The passenger door of OP's car is wide open. The hitchhiker is gone.\n\n"
            "The clerk pulls up the security camera. The footage is clear. Two angles. OP pulling in. Getting out alone. Running "
            "inside. There was never a passenger. The passenger door does open by itself, in the footage, about thirty seconds after "
            "OP runs into the store. But there is nobody in the seat. There never was.\n\n"
            "OP says he sat in the gas station until sunrise. The clerk let him. When OP finally drove home, his car smelled like wet "
            "wool. Just for the first mile. Then it was gone.\n\n"
            "He says he doesn't drive Highway 9 at night anymore. None of us would.\n\n"
            "If you've ever heard a stranger say your name, drop the comment. Subscribe for more from the road."
        ),
    },
    # 4
    {
        "title": "My Neighbor Was Watching Me Sleep Through My Bedroom Window",
        "description": "For three weeks. From a place he shouldn't have been able to stand. #letsnotmeet #creepy #scary #redditstories",
        "content": (
            "Second floor apartment. My bedroom window faces a brick wall about six feet away. There is no balcony. No fire escape. "
            "Nothing to stand on. For three weeks I'd been waking up feeling watched. I thought I was being paranoid. Then I set up "
            "a webcam. Pointed it at the window. The next morning I watched the footage. At 3:14 AM, a face appeared in the window. "
            "Pressed against the glass. My upstairs neighbor. He stayed there for forty minutes. I called police. They asked how he "
            "got there. There is nothing under the window. They eventually found a system of climbing hooks he had installed into "
            "the brick over the previous month. He'd been training to climb up. From the alley."
        ),
        "script": (
            "Some stalkers are loud. Some are patient. OP's neighbor was the patient kind.\n\n"
            "OP lives on the second floor of a brick apartment building. Her bedroom window faces the side alley. The wall of the "
            "next building is about six feet away. There is no balcony. No fire escape. Nothing under her window. The window is too "
            "high to reach from the ground and there is nothing for a person to stand on. This is, in her words, why she always "
            "felt safe leaving the blinds open.\n\n"
            "For three weeks she had been waking up around three a.m. with the feeling of being watched. She would sit up in bed, "
            "see nothing, lay back down, and write it off as a nightmare. She started keeping the blinds half closed just in case.\n\n"
            "Finally she sets up a cheap webcam on her dresser. Points it at the window. Hits record before bed.\n\n"
            "Next morning she scrubs through the footage at her kitchen table. Most of it is nothing. Then at 3:14 a.m. she sees it. "
            "A face appears in the window. Pressed against the glass. Eyes open. Just watching her sleep.\n\n"
            "She recognizes him immediately. It is the man from the apartment directly above hers. They have nodded at each other in "
            "the hallway. He had once helped her carry groceries up the stairs. Polite. Quiet. Mid forties.\n\n"
            "He stays at the window for forty minutes. He does not move. He does not blink for what looks like impossible stretches. "
            "Then he disappears. He does not climb down. He does not fall. He just is not in the frame anymore.\n\n"
            "She calls the police. The officers come out. Their first question is, how did he get there? There is no balcony. There "
            "is nothing under the window. The wall is just smooth brick.\n\n"
            "It takes them two days to find it. He had been installing climbing hooks into the brick of the alley wall over the "
            "previous month. Small ones. Painted to match the brick. Spaced just right for hand and foot holds. He had been training "
            "himself to scale the wall from the alley to her window. Quietly. Methodically. So he could stand outside it for forty "
            "minutes at a time, in the middle of the night, watching her sleep.\n\n"
            "Police searched his apartment. They found a notebook. Pages of her schedule. What time she got home. What time she went "
            "to bed. What time she usually woke up. Photos of her through the window. Drawings.\n\n"
            "He was arrested. He took a plea deal. He's in for years. OP moved that week. She does not leave her blinds open anymore. "
            "Subscribe and please check your windows tonight."
        ),
    },
    # 5
    {
        "title": "I Bought An Old Doll At A Yard Sale — That Night She Started Speaking",
        "description": "The seller said it didn't talk. The voice was not a recording. #nosleep #paranormal #haunted #creepy #redditstories",
        "content": (
            "Yard sale on a Saturday. Old woman selling off her late mother's things. I saw a porcelain doll in a wooden chair. "
            "Beautiful. Vintage. Five dollars. I asked if it talked. The old woman looked uncomfortable and said, no, it does not. "
            "I bought it. Set it on a shelf at home. That night, around 2 AM, I heard a child's voice in my hallway. Whispering. "
            "I sat up. The doll was on the floor outside my bedroom door. I had locked the door. The voice said, 'put me back where "
            "she put me.' I took her back to the yard sale address the next morning. Empty house. For sale sign. The woman didn't "
            "live there. The realtor said the house had been empty for two years."
        ),
        "script": (
            "Have you ever bought something at a yard sale and felt like you took something else home with it? OP did.\n\n"
            "Saturday morning. OP is wandering through a neighborhood yard sale. There is an old woman running it. She says she is "
            "selling off her late mother's things. Mostly normal. Plates. Books. Lamps. And then, on a small wooden chair in the "
            "shade, a porcelain doll. Beautiful. Vintage. Long dress. Glass eyes. Five dollars.\n\n"
            "OP picks her up. He asks the old woman, does she talk, like one of those antique pull string dolls? The old woman looks "
            "uncomfortable. She says, no, she does not talk. Then, after a pause, she says, please don't put her near a door at "
            "night.\n\n"
            "OP laughs. Pays the five dollars. Takes the doll home. Puts her on a shelf in his living room. He completely forgets "
            "about the warning.\n\n"
            "That night, around two a.m., he wakes up. He hears a voice in his hallway. A child's voice. Whispering. He can't make "
            "out the words. He sits up. His bedroom door is closed. He had locked it before bed, which he never does, because the "
            "doll had been making him a little uneasy when he turned off the lights.\n\n"
            "The whispering stops. Then it says, very clearly, put me back where she put me.\n\n"
            "OP turns on his phone flashlight. He gets up. He approaches the door. He opens it.\n\n"
            "The doll is sitting on the floor of the hallway. Directly outside his bedroom door. Facing his door. She had been on a "
            "shelf in the living room two rooms away.\n\n"
            "OP did not sleep again. The next morning he put the doll in the passenger seat of his car. Drove back to the yard sale "
            "address.\n\n"
            "There was no yard sale. There was no old woman. The house was empty. The grass had not been cut in months. There was a "
            "for sale sign in the front yard. OP knocked. No answer.\n\n"
            "He called the realtor on the sign. The realtor told him the house had been vacant for two years. The previous owner, "
            "an elderly woman, had passed away there. Her daughter had cleared out the house and sold off her possessions before "
            "listing the property.\n\n"
            "OP described the woman who had been running the yard sale the day before. The realtor went quiet for a moment. Then he "
            "said, that sounds like the previous owner.\n\n"
            "OP buried the doll in the backyard of the empty house. He says the whispering stopped. He never went back. He never "
            "drove past it again. He still won't sleep with his bedroom door open.\n\n"
            "Some things are five dollars for a reason. Subscribe if you check your shelves after dark."
        ),
    },
    # 6
    {
        "title": "There's An Old Mirror In My Attic — It Shows A Different Room",
        "description": "Same dimensions. Different room. And something is moving in it. #nosleep #haunted #creepy #scary #redditstories",
        "content": (
            "Inherited my grandparents' farmhouse. Cleaning out the attic I found a tall mirror covered in a sheet. Beautiful old "
            "frame. When I uncovered it, the mirror didn't show the attic. It showed a different room. Same dimensions. But "
            "different walls. Different floor. A single chair facing the mirror, with a man sitting in it. Watching me. He was not "
            "moving. I waved. He did not move. I stepped to the side. He turned his head and tracked me. I covered the mirror back "
            "up and ran. That night I checked the attic. The sheet was on the floor. The chair in the mirror was empty. The man "
            "was now standing. And he was closer."
        ),
        "script": (
            "If you've ever inherited an old house, you know there is always one room you should leave alone. OP found his attic.\n\n"
            "OP inherits his grandparents' farmhouse after they pass within months of each other. It is a beautiful old place. He "
            "spends a weekend up there cleaning it out before he decides whether to live in it or sell it.\n\n"
            "He saves the attic for last. He climbs the ladder. He is expecting cobwebs and old furniture, and that is mostly what "
            "he finds. Boxes. A rocking chair. Old quilts. And, propped against the back wall, a tall mirror with a heavy carved "
            "wooden frame. Covered in a sheet.\n\n"
            "He pulls the sheet off. He turns to look at the mirror. And he stops.\n\n"
            "The mirror is not showing the attic.\n\n"
            "It is showing a room. The same dimensions as the attic. The same angle, the same shape. But the walls are different. "
            "Wood paneling instead of bare wood. The floor is darker. There is a single wooden chair in the middle of the room. "
            "Facing the mirror. And a man is sitting in the chair, watching him.\n\n"
            "He is not someone OP recognizes. He is older. Dressed plainly. Not moving. Not blinking. Just watching.\n\n"
            "OP waves. The man does not move. OP says, hello, out loud, into the attic. The man does not move. OP takes a step to "
            "the side, to see if he's a painting or a hologram or some trick of the light. The man's eyes follow him. He turns his "
            "head, slowly, tracking OP across the room.\n\n"
            "OP throws the sheet back over the mirror. He climbs down the ladder. He locks the attic door. He drives back to his "
            "apartment in town and pretends it didn't happen.\n\n"
            "That night, around three a.m., he can't sleep. He drives back to the farmhouse. He tells himself he just imagined it. "
            "He climbs the ladder. He opens the attic.\n\n"
            "The sheet is on the floor.\n\n"
            "He had thrown it over the mirror and walked away. He had not touched it again. He had locked the attic door behind him. "
            "Yet the sheet was lying on the floor next to the mirror.\n\n"
            "He looks at the mirror. The room is still there. The chair is still there. But the chair is empty. The man is no longer "
            "sitting in it.\n\n"
            "He is standing. Closer to the mirror than the chair was. And his face is just out of view, like he is leaning down to "
            "look through.\n\n"
            "OP didn't cover the mirror again. He left. He listed the farmhouse for sale that week. Whoever buys it inherits "
            "everything in it. Subscribe if you've ever been afraid of a mirror."
        ),
    },
    # 7
    {
        "title": "I Got A Voicemail From My Grandmother Three Years After She Died",
        "description": "Her old number had been reassigned. The voicemail was her. And she knew what was happening in my life. #paranormal #nosleep #creepy #redditstories",
        "content": (
            "My grandmother died in 2022. Her phone was cancelled. The number was reassigned to someone else within a year. Last "
            "month I got a voicemail at 2:14 AM. From her old number. It was her voice. Unmistakable. She said, 'I am so sorry "
            "about the baby, sweetheart. I am here when you are ready.' My wife had a miscarriage two weeks earlier. We had told "
            "no one. The current owner of the number is a man in his forties. He said he never makes calls after midnight and his "
            "phone showed no record of having called me. I saved the voicemail. Played it for my mom. She started crying. She had "
            "lost a baby in 1978. She had never told anyone."
        ),
        "script": (
            "Have you ever gotten a phone call you can't explain? OP's grandmother died three years ago. Last month she called him "
            "anyway.\n\n"
            "OP's grandmother passed in 2022. After the funeral, the family cancelled her phone. Standard. The carrier eventually "
            "reassigned her old number to a new customer about ten months later. OP had her number saved in his phone with a heart "
            "next to her name because he hadn't been able to delete it. The number now belonged to a stranger.\n\n"
            "Last month, around two fifteen a.m., his phone rang. He didn't pick up. He was asleep. In the morning he saw a "
            "voicemail notification from, quote, Grandma heart emoji. He stared at it for ten minutes before he pressed play.\n\n"
            "The voice was hers. Unmistakable. He recognized her cadence, the slight rasp she had after a lifetime of dry winters, "
            "the way she always said his name with a long e at the end.\n\n"
            "The message was short. She said, I am so sorry about the baby, sweetheart. I am here when you are ready. I love you.\n\n"
            "That was it.\n\n"
            "Here is the part that broke him. Two weeks earlier, his wife had had a miscarriage. They had only just learned she was "
            "pregnant. They had told no one. Not their parents. Not their siblings. Not their friends. They had been waiting for "
            "the twelve week mark to announce. The pregnancy had ended at nine weeks. They were still grieving in private.\n\n"
            "OP called the number back. A man answered. Mid forties. Confused. OP asked if he had called him at two fifteen a.m. "
            "the night before. The man checked his recent calls in front of him. He said no. He said his phone had been on do not "
            "disturb. He said he never makes calls after midnight. He sounded annoyed, and then a little uneasy, because OP would "
            "not let it go.\n\n"
            "OP eventually drove to a phone repair shop and had them pull the call data. The voicemail file was real. The metadata "
            "showed it had been received at his phone at 2:14 a.m. The originating number was his grandmother's old number. The "
            "carrier's records, on the other end, showed no outgoing call at that time from that number.\n\n"
            "OP saved the voicemail. Played it for his mother that weekend. She started crying before he had even told her what "
            "she was about to hear. She told him a story she had never told anyone in her life. In 1978, she had lost a baby too. "
            "OP's grandmother was the only person who ever knew.\n\n"
            "The voicemail is still in his phone. He plays it on the days he needs it. Subscribe if you've ever gotten a call you "
            "can't explain."
        ),
    },
    # 8
    {
        "title": "I Hiked A Trail That Wasn't On Any Map — Something Followed Me Back",
        "description": "I saw the trailhead from the road. The forest service says it doesn't exist. #nosleep #creepy #scary #hiking #redditstories",
        "content": (
            "I was driving through the national forest. Saw a small wooden trail sign at a pull off. 'Whitehorse Ridge — 2.4 mi.' "
            "I had time. I parked and hiked it. The trail was beautiful and completely empty. I made the ridge. Took photos. Hiked "
            "back. When I got home I checked the forest service map. There is no Whitehorse Ridge trail. The pull off doesn't exist. "
            "I drove back the next weekend to show my brother. The trail sign was gone. So was the pull off. We parked on the "
            "shoulder and walked into the woods anyway. We made it about a mile in. We heard footsteps behind us. We turned around. "
            "Our own footprints in the dirt were doubled."
        ),
        "script": (
            "If you hike, you probably have a favorite trail. OP's favorite trail does not exist.\n\n"
            "OP was driving through a large national forest on a Sunday. Two lane road. Forty miles between towns. He passed a small "
            "gravel pull off with a wooden trail sign at the edge. He pulled over and walked up to it. The sign was simple. Hand "
            "carved. It said, Whitehorse Ridge, two point four miles.\n\n"
            "He had time. He had hiking boots. He had water. He locked the car and started up the trail.\n\n"
            "The trail was beautiful. Clear path. Worn smooth. Old growth trees. He didn't pass a single other hiker. He made the "
            "ridge in about an hour. Took photos. Sat for a few minutes. Hiked back. Back at the car by sundown. Drove home.\n\n"
            "That night, scrolling through his photos, he wanted to look up the trail to plan a longer hike. He pulled out the "
            "forest service map. He looked at the section of road where he had pulled off. There was no trailhead. There was no "
            "trail. There was no Whitehorse Ridge.\n\n"
            "He called the local ranger station the next morning. The ranger said, with absolute confidence, there is no Whitehorse "
            "Ridge trail in this forest. There is no pull off at that mile marker. Maybe you have the wrong forest.\n\n"
            "OP had the photos. He had the GPS tags on the photos. The coordinates were inside the national forest. He had been "
            "there.\n\n"
            "The next weekend he drove back. He brought his brother. He wanted a witness.\n\n"
            "He pulled up to where the pull off had been. There was no pull off. The shoulder of the road there was the same "
            "shoulder for miles in either direction. The wooden sign was gone. No post in the ground. No disturbed dirt.\n\n"
            "They parked on the shoulder. They walked into the woods at the spot where the trail had been. There was no trail. They "
            "kept walking anyway. The forest got dense. They pushed through brush for about half a mile and then, suddenly, the "
            "trail was there. Same trail. Same worn path. Same direction.\n\n"
            "They followed it. About a mile in, they both stopped at the same time. They heard footsteps behind them. Not animal. "
            "Boots. Steady. Matching their pace, just delayed.\n\n"
            "They turned around. There was no one on the trail. But their own footprints in the dirt behind them were doubled. As "
            "if someone had been walking in step with them, one set on top of theirs.\n\n"
            "They left. They drove home in silence. OP has not gone back. He hopes you don't either. Subscribe for more from the "
            "woods."
        ),
    },
    # 9
    {
        "title": "The Man In The Gas Station Bathroom Wasn't On Any Camera",
        "description": "I saw him at the sink. He smiled at me in the mirror. The clerk said the bathroom had been empty all night. #letsnotmeet #nosleep #creepy #redditstories",
        "content": (
            "Driving overnight on I-80. Stopped at a 24 hour gas station around 3 AM. Went to use the bathroom. A man was at the "
            "sink. Long coat. Wet hair, dripping, even though it wasn't raining. He smiled at me in the mirror. I nodded, went into "
            "the stall, came out a minute later. He was still at the sink. Still smiling at the mirror. Water still dripping. I "
            "left. Told the clerk there was a creepy guy in the bathroom. Clerk pulled up the camera in the hallway leading to the "
            "bathroom. Nobody had gone in or out for two hours before me. He showed me the bathroom doorway angle. I walked in. The "
            "footage clearly showed me alone. The mirror behind me was empty. I never saw a reflection of him. Only of me."
        ),
        "script": (
            "If you drive overnight, you know the rules. Don't stop at gas stations that don't feel right. OP did not know the rules "
            "yet.\n\n"
            "OP is driving cross country. It's three a.m. He's on a flat stretch of highway in the middle of nowhere. He pulls off "
            "at a small twenty four hour gas station. Two pumps. One clerk inside behind bulletproof glass. He fills up. He goes "
            "inside to use the bathroom.\n\n"
            "The bathroom is small. One sink. Two stalls. As he walks in, there is a man standing at the sink. Long dark coat. The "
            "man's hair is wet. Dripping into the sink. It hadn't been raining. There had been no rain for days. The man is just "
            "looking at himself in the mirror.\n\n"
            "OP nods politely. The man smiles. Not at OP directly. At OP's reflection in the mirror. A big slow smile. OP keeps "
            "walking, goes into the far stall, locks the door, does his business as fast as he possibly can.\n\n"
            "When he comes out about ninety seconds later, the man is still there. Same position. Same smile. Same water still "
            "dripping from his hair into the sink. He has not moved. OP washes his hands at the second sink, gets out, walks fast "
            "back to the front of the store.\n\n"
            "He tells the clerk, there is a really weird guy in the bathroom, you might want to check on him. The clerk frowns. He "
            "says, has there been someone in there with you the whole time? OP says yes. The clerk pulls up his security camera.\n\n"
            "There is a camera in the hallway leading to the bathroom. The clerk scrolls back. Nobody had walked into that bathroom "
            "for two hours before OP did. OP was the first person to enter all night.\n\n"
            "Clerk pulls up another angle. The doorway is visible from a corner camera in the store. OP walks toward the bathroom "
            "in the footage. The bathroom door is shut. He pushes it open. The angle catches just inside the bathroom for half a "
            "second.\n\n"
            "OP is alone. The sink is dry. The mirror is empty.\n\n"
            "They walk to the bathroom together. The clerk opens the door. The sink is dry. No water on the floor. The mirror is "
            "clean. There is no man.\n\n"
            "OP says he stood in the bathroom for a long minute, looking at the mirror. He had never seen a reflection of the man "
            "in it. He had only ever seen his own reflection. He had assumed the man was real because he could see him in the room. "
            "He had not noticed the mirror was empty.\n\n"
            "OP doesn't stop at gas stations alone anymore. Subscribe and please don't stop at three a.m."
        ),
    },
    # 10
    {
        "title": "My Dog Won't Stop Staring At The End Of My Hallway",
        "description": "He's done it every night for three weeks. There's nothing there. Until I filmed it. #nosleep #paranormal #haunted #creepy #redditstories",
        "content": (
            "My golden retriever is six years old. Sweetest dog on earth. Three weeks ago he started sitting in the middle of the "
            "hallway at night and staring at the wall at the end of it. Not the door. The wall. He'd sit there for hours. He won't "
            "respond to his name when he's doing it. Eventually I set up my phone to film overnight. Watched the footage in the "
            "morning. From midnight to 3 AM, my dog stares at the wall. At 3:03 AM, something dark passes through the wall, walks "
            "down the hallway, walks past my dog, who tracks it with his head, and stops at the door of my bedroom. My door opens. "
            "Then the thing walks in. My dog stays sitting in the hallway. He won't come into the bedroom anymore."
        ),
        "script": (
            "Dogs see things we don't. We've all heard that. OP set up a camera to find out exactly what his was seeing. It was a "
            "mistake.\n\n"
            "OP has a six year old golden retriever named Buddy. The sweetest dog on earth, his words. Buddy follows him from room "
            "to room. Sleeps at the foot of the bed every night. Has slept in OP's bedroom every night since he was a puppy.\n\n"
            "Three weeks ago, Buddy stopped doing that.\n\n"
            "Instead, every night, after OP goes to bed, Buddy walks out into the hallway. He sits down in the middle of the "
            "hallway. And he stares at the wall at the very end of it. Not the door to the bathroom. Not the linen closet. The "
            "blank wall.\n\n"
            "He sits there for hours. He doesn't move. He doesn't whine. He doesn't bark. If OP calls his name, Buddy doesn't "
            "respond. If OP comes out and tries to pet him, Buddy is rigid. Eyes locked on the wall.\n\n"
            "OP took him to the vet. Bloodwork. Eyes. Ears. Cognitive tests. Everything normal. Vet said dogs sometimes get like "
            "this and to just let him be.\n\n"
            "OP couldn't let it be. So he set up his phone in the hallway to record overnight. Pointed at Buddy and at the wall.\n\n"
            "He watched the footage in the morning.\n\n"
            "From midnight to three a.m., the footage is exactly what he expected. Buddy sitting in the hallway, staring at the wall. "
            "Tail still. Ears up. Just watching.\n\n"
            "At three oh three a.m., something happens.\n\n"
            "A dark shape comes through the wall. Through the wall. Not from a door. Not from a vent. From the wall itself. It is "
            "tall. Roughly the shape of a person but indistinct, like the camera couldn't focus on it. It walks down the hallway. "
            "It moves past Buddy. Buddy tracks it with his head, calm, like he sees it every night.\n\n"
            "The shape stops at OP's bedroom door. The bedroom door opens. The shape walks in. The door closes behind it.\n\n"
            "OP was in the bed. Asleep. He had no memory of anything entering the room. He has no idea what happens next.\n\n"
            "The shape comes back out about forty minutes later. Walks down the hallway. Passes Buddy again. Walks back through the "
            "wall.\n\n"
            "Buddy stays sitting in the hallway until sunrise.\n\n"
            "OP says Buddy will not come into the bedroom anymore. Not even during the day. He waits at the doorway. Every night, at "
            "midnight, he goes to his spot in the hallway. OP has tried sleeping on the couch. The shape still comes. Buddy still "
            "watches.\n\n"
            "He is moving next month. He doesn't know if it matters. Subscribe and please pay attention to your pets."
        ),
    },
    # 11
    {
        "title": "The Radio In My Car Plays A Broadcast At 3:33 AM That Doesn't Exist",
        "description": "It is the same broadcast every night. And every night, more of it is about me. #nosleep #paranormal #creepy #scary #redditstories",
        "content": (
            "Drove a graveyard shift. Around 3:33 AM every night, my car radio would switch to a station that wasn't programmed. "
            "Crackly old broadcast voice. Reading what sounded like a news bulletin from another era. The first week it was just "
            "weather and crop reports. Then it started reading addresses. Then my home address. Then descriptions of my evening. "
            "What I had eaten. What I had said to my wife. Last night it read tomorrow's date and said, 'final broadcast.' I called "
            "the FCC. They confirmed there is no licensed broadcast on that frequency. I bought a new car. The new car's radio "
            "switched to the same station at 3:33 AM tonight. It said, 'we missed you yesterday.'"
        ),
        "script": (
            "If your car radio ever switches to a station that isn't there, please change cars. It will not help. But please.\n\n"
            "OP worked an overnight delivery route for two years. Same route. Same hours. Quiet small town highways. He had his "
            "presets dialed in. Two news stations, three music stations.\n\n"
            "A few months ago he noticed his radio doing something strange. At three thirty three a.m., every night, it would "
            "switch off his preset and tune itself to a frequency that wasn't programmed. He'd hear static for a moment. Then a "
            "broadcast would come through. Crackly. Old microphone sound. A man's voice. Calm. Like a 1940s radio announcer.\n\n"
            "The first week, the broadcasts were boring. Weather. Wheat prices. Football scores from games OP had never heard of, "
            "between teams that didn't exist. He laughed it off. Figured he was picking up a pirate radio guy roleplaying old time "
            "radio.\n\n"
            "Then one Tuesday at three thirty three, the voice started reading addresses. Just a list of street addresses. About a "
            "dozen of them. OP didn't recognize any of them at first. Then, the eighth one in, the voice read his address.\n\n"
            "OP almost wrecked his car. He pulled over. The voice kept reading addresses. Then it went back to wheat prices. Then "
            "it ended. The radio returned to his preset like nothing had happened.\n\n"
            "He told himself it was a coincidence. The next night, three thirty three, the broadcast came back. This time it read "
            "what it called, quote, the evening's events. It read a list of things people had done that night. About thirty entries. "
            "Most were short. One read, quote, the driver had spaghetti with his wife at seven p.m., argued about money, made up "
            "before bed. OP and his wife had eaten spaghetti that night. They had argued about a credit card bill. They had made up "
            "before bed.\n\n"
            "He didn't sleep.\n\n"
            "The next night, the broadcast read what he had done that day. The next night, what he had said to his daughter on the "
            "phone. The voice didn't sound threatening. It sounded patient. It sounded like an archive.\n\n"
            "He called the FCC. They confirmed there is no licensed broadcast on that frequency in his region. They told him "
            "regional pirate broadcasts almost never run nightly at the same time. They asked him to send a recording. The recording "
            "would not save. Every time he played it back in the morning, it was static.\n\n"
            "Last week, the broadcast read tomorrow's date and said, quote, final broadcast.\n\n"
            "OP traded the car in the next morning. Different make. Different model. Different dealer. Two states away.\n\n"
            "He drove the new car last night. At three thirty three a.m., the radio switched stations on its own. The voice came "
            "through clearer than ever. The first thing it said was, quote, we missed you yesterday.\n\n"
            "Subscribe and don't change your stations after midnight."
        ),
    },
    # 12
    {
        "title": "There's A Boy In The Cornfield Behind My House — He's Always Facing My Window",
        "description": "He stands in the same spot every night. Even when the corn is too tall for him to see over. #nosleep #scarystories #creepy #redditstories",
        "content": (
            "Bought a farmhouse in Indiana. Beautiful place. The back of the property borders a neighbor's cornfield. Last summer "
            "I noticed a small boy standing in the cornfield about thirty yards back, facing my bedroom window. Same kid. Same "
            "spot. Every night around 9 PM. I figured it was the neighbor's kid. Asked the neighbor. He has no kids and no one "
            "visits. The corn grew taller over the summer. Past the boy's head. He kept standing in the same spot, facing my window. "
            "I could only see him from the second story now. By August the corn was eight feet tall. He's still there. He hasn't "
            "moved in three months. He hasn't grown. The neighbor cut the field last week. The boy is still there. There is no "
            "corn around him."
        ),
        "script": (
            "If you live next to a cornfield, you know cornfields get weird at night. OP's cornfield is worse.\n\n"
            "OP bought a small farmhouse in rural Indiana last year. Beautiful old place. The back of his property line borders a "
            "neighbor's cornfield. The neighbor is an older farmer who lives a quarter mile away. They've spoken twice.\n\n"
            "Last summer, OP started noticing something out his upstairs bedroom window. Around nine p.m. every night, just as it "
            "was getting dark, a small boy was standing in the cornfield. About thirty yards back from the property line. Facing "
            "OP's bedroom window. Just standing there.\n\n"
            "OP assumed he was the farmer's grandson. He waved. The boy didn't wave back. He went down and walked toward the fence. "
            "The boy didn't move. By the time he reached the fence, it was too dark to see well. He went back inside.\n\n"
            "The next morning he drove over to the neighbor's house and asked, hey, is that your grandson hanging out in the field "
            "at night? The farmer looked at him for a long time. Then said, son, I don't have any grandkids. No kids ever come out "
            "here.\n\n"
            "OP kept watching. The boy was there every night. Same spot. Same time. Same height. He never moved.\n\n"
            "Through June and July, the corn grew. By the end of July, the corn was over the boy's head. OP couldn't see him from "
            "the first floor anymore. From his upstairs bedroom window, he could just make out the top of the boy's head between "
            "the stalks. Still in the exact same spot. Still facing the window.\n\n"
            "By August the corn was eight feet tall. OP could only see the boy when he stood at his upstairs window and the "
            "moonlight hit just right. The boy was still there. Still in the same spot. Still hadn't moved.\n\n"
            "Three months. He had not moved.\n\n"
            "OP called the farmer in October when the corn was getting cut for harvest. He said, look, this is going to sound "
            "insane, but please tell me if you see a kid out there when you cut.\n\n"
            "The farmer cut the field. He called OP that night. He said, I cut around something. I'm not sure what. I don't want "
            "to look at it. You should come look.\n\n"
            "OP went out there at dusk. The field was bare. Stubble for hundreds of yards in every direction. And in the exact "
            "spot the boy had been standing all summer, there was a perfect ring of uncut corn. About three feet wide. The corn "
            "in the ring was the only corn standing in the entire field.\n\n"
            "The boy was standing in the middle of the ring. Same height. Same clothes. Same face. Still facing OP's window.\n\n"
            "OP put the house on the market the next morning. Subscribe. Don't buy farmhouses with views."
        ),
    },
    # 13
    {
        "title": "Our Wedding Photographer Caught A Person In Every Photo Who Wasn't At The Wedding",
        "description": "Same person. Every angle. Every shot. We don't know who he is. #nosleep #paranormal #creepy #scary #redditstories",
        "content": (
            "Got our wedding photos back. Beautiful work. Around the third album page my wife noticed a man. Tall, dark suit, "
            "balding, mid sixties. Standing at the back of the ceremony. We didn't recognize him. Showed our parents. No one knew "
            "him. We checked every photo. He was in every single one. Background of the reception. Edge of the dance floor. Just "
            "outside the cake cutting. Every angle, every shot. Always looking at us. We checked the guest list and the venue's "
            "camera footage. No man like that on camera entering or leaving. No one matching that description signed in. The "
            "photographer doesn't remember photographing him. My wife's grandmother saw the photos and dropped her glass. He was "
            "her father. He died in 1979."
        ),
        "script": (
            "Have you ever looked through your wedding photos and seen someone you didn't invite? OP and his wife noticed an extra "
            "guest. In every. Single. Photo.\n\n"
            "OP and his wife got married last year. Small wedding. Sixty guests. Beautiful outdoor venue. They hired a professional "
            "photographer who delivered the photos about three weeks after the wedding.\n\n"
            "They sat down on the couch to look through the album together. Around the third page, his wife stopped. She pointed at "
            "the back of a wide shot of the ceremony. There was a man standing at the back. Tall. Dark gray suit. Balding. Mid "
            "sixties. He was just inside the rear corner of the seating area. He wasn't looking at the bride or the groom. He was "
            "looking at his wife. Directly at her.\n\n"
            "She said, who is that. OP didn't know. They didn't recognize him.\n\n"
            "They flipped to the next page. He was in the next photo too. Background of the recessional. Standing on the lawn. "
            "Still watching them.\n\n"
            "The next page. Behind the bridal party photos. Just out of focus, but there. Always present. Always watching.\n\n"
            "They went through the entire album. The man was in every photo. Every single one. The background of the cocktail "
            "hour. Edge of the dance floor. Just outside the cake cutting. The first dance had him standing right behind the "
            "father of the bride.\n\n"
            "He was the same man. Same face. Same suit. Same angle of his head. He never spoke. He never appeared to interact with "
            "anyone. No one was looking at him in any photo. No one was acknowledging him.\n\n"
            "They called their parents. Showed them the photos. Nobody knew him. They went through the guest list. Sixty names. "
            "None of them this man. They contacted the venue and asked for the security camera footage from the entrance. The "
            "venue sent over the footage. They watched four hours of guests arriving and leaving. No one matching the man entered "
            "or left the venue. Not once.\n\n"
            "OP called the photographer. The photographer said, this is going to sound weird, but I don't remember photographing "
            "him. I would have. I have a process. I check every frame for crashers and ask them to step out. He's in the photos. "
            "He wasn't there.\n\n"
            "OP's wife brought the album to her grandmother that Sunday. Her grandmother had been too sick to attend the wedding. "
            "She was excited to finally see the photos.\n\n"
            "She flipped to the first page. She saw the man. She dropped her water glass. It broke on the floor. She said his name. "
            "And then she said, that's my father. He died in 1979. I never even got to introduce him to your mother.\n\n"
            "OP says they keep the album in the back of a closet now. They look at it once a year on their anniversary. He is "
            "still in every photo. Subscribe for the wholesome scary ones."
        ),
    },
    # 14
    {
        "title": "I Stayed In An Airbnb With A Hallway The Host Said Was 'Private' — I Should Have Listened",
        "description": "She told me at check in. I forgot. I opened the door at 2 AM. #nosleep #letsnotmeet #creepy #redditstories",
        "content": (
            "Solo trip. Booked a cute Airbnb in a small mountain town. The host met me at check in. Sweet older woman. She showed "
            "me around and pointed to a hallway off the kitchen. 'This hallway is private. Please do not go down it. It is in the "
            "listing.' I checked the listing. It was. I said no problem. Two nights later I woke up at 2 AM hearing scraping coming "
            "from that hallway. I wasn't fully awake. I forgot the rule. I opened the door. There was no hallway. There was a flight "
            "of wooden stairs going down. At the bottom, candles. And a woman in a long dress, sitting on the floor, with her back "
            "to me, slowly turning her head. I shut the door. I left at sunrise. The host messaged me three days later. 'You looked.'"
        ),
        "script": (
            "Some Airbnb hosts ask you to take your shoes off. Some ask you to use the dish soap by the sink. OP's host asked her "
            "not to open a specific hallway. OP, eventually, opened it.\n\n"
            "OP is on a solo writing trip. She rents a small cabin Airbnb in a quiet mountain town. The host meets her at check in. "
            "A sweet older woman in a long sweater. Polite. Warm. Gives her the tour herself.\n\n"
            "At the end of the tour, in the kitchen, the host points to a hallway that branches off behind the pantry. The hallway "
            "has a closed door at its entrance. The host says, this hallway is private. Please do not go down it. It's in the "
            "listing.\n\n"
            "OP pulls up the listing on her phone. It is in the listing. In the house rules, underlined. Quote, the private hallway "
            "is not part of the rental. Guests must not open the door under any circumstances.\n\n"
            "OP says no problem. She wasn't planning to. The host smiles, hands her the keys, and leaves.\n\n"
            "The first night, OP doesn't think about it. The cabin is gorgeous. She writes by the fire. She sleeps well.\n\n"
            "The second night, she starts hearing things. A faint scraping sound from the kitchen area. Like a chair being dragged "
            "slowly across a wood floor. She gets up. There's no chair out of place. The fridge is humming. She goes back to bed.\n\n"
            "The third night, the scraping is louder. It is two a.m. She is groggy. Half asleep. She walks into the kitchen. She "
            "is barely awake. She walks past the pantry and turns toward the sound. Without thinking, she opens the door.\n\n"
            "There is no hallway.\n\n"
            "Behind the door is a flight of wooden stairs going down. Old. Narrow. The air coming up is cold and smells like wet "
            "earth.\n\n"
            "At the bottom of the stairs, she can see candles. A circle of them. Real candles, flickering. And, sitting in the "
            "middle of the circle, facing away from her, is a woman in a long pale dress. Long hair. Bare feet. Sitting cross "
            "legged on the dirt floor.\n\n"
            "As OP stands at the top of the stairs, the woman starts to turn her head. Slowly. Toward her.\n\n"
            "OP slammed the door. She did not look back. She ran to the bedroom, grabbed her bag, sat in her car in the driveway "
            "with the doors locked, and waited for sunrise. She drove out at six a.m.\n\n"
            "Three days later, the host messaged her. Five star review, no mention of any of it. The message was one line. Quote, "
            "you looked.\n\n"
            "OP didn't respond. She doesn't book Airbnbs in mountain towns anymore. Subscribe if you check listing rules carefully."
        ),
    },
    # 15
    {
        "title": "The Voice In My Baby Monitor Wasn't Coming From My Baby",
        "description": "I checked the monitor. The room was empty. The voice kept talking. #nosleep #paranormal #parenting #creepy #redditstories",
        "content": (
            "Three month old. Sleeping through the night for the first time. Around 2 AM I heard a voice through the monitor. Adult. "
            "Soft. Female. Singing the lullaby my late mother used to sing to me as a child. I sat up. Checked the video feed. The "
            "nursery was empty except for my daughter, asleep in her crib. No one was in the room. The voice kept singing. I ran "
            "to the nursery. Empty. The monitor on the dresser was off, unplugged. Yet the audio was still coming through my "
            "speaker. The singing finished. The voice said, very softly, 'she has your eyes, sweetheart.' Then the speaker went "
            "silent. My mother died when I was nineteen. She never met her granddaughter. The lullaby was one she wrote herself."
        ),
        "script": (
            "Have you ever heard a voice you weren't supposed to hear? OP heard her dead mother singing through the baby monitor.\n\n"
            "OP has a three month old daughter. First time mom. Sleep deprived. Hyper alert to every sound from the nursery. She "
            "and her husband had set up a wifi baby monitor with video and audio. Camera on the wall. Speaker on the dresser in the "
            "nursery. Receiver on her bedside table.\n\n"
            "Last week was the first night the baby slept through. OP didn't believe it. She kept checking the monitor every "
            "twenty minutes.\n\n"
            "Around two a.m. she heard a voice through the monitor speaker. Soft. Adult. Female. Singing.\n\n"
            "The melody was familiar. She listened for a few seconds. And then she froze, because she recognized it. It was the "
            "lullaby her mother used to sing to her when she was a little girl. It wasn't a famous lullaby. It wasn't a song. Her "
            "mother had written it herself when OP was a baby. She used to sing it every night.\n\n"
            "Her mother died when OP was nineteen. Cancer. Quick. She never met her granddaughter.\n\n"
            "OP sat up in bed. She turned on the video feed on her phone. The nursery was lit by the night light. The crib was in "
            "view. Her daughter was asleep, peaceful, on her back. The room was empty. No one else was in the room.\n\n"
            "The singing kept going.\n\n"
            "OP ran to the nursery. Pushed the door open. The room was exactly as the camera showed it. Her daughter asleep. No one "
            "else there. She looked at the dresser where the monitor speaker was.\n\n"
            "The monitor was off. The cord had pulled out of the wall sometime in the day. The little green power light was dark. "
            "The speaker was not on.\n\n"
            "She ran back to her bedroom. Her receiver was still playing the lullaby. Clearly. Through speakers that were no longer "
            "connected to anything in the nursery.\n\n"
            "She stood in her bedroom doorway. She listened. The lullaby finished. There was a pause. Then, just as soft as the "
            "singing, the voice said, quote, she has your eyes, sweetheart.\n\n"
            "Then the receiver went silent.\n\n"
            "Her husband had slept through all of it. She woke him up. She made him replay the monitor's audio history on the app. "
            "Most monitors record. There was nothing recorded. The timestamp had a six minute gap. As if those six minutes had not "
            "happened.\n\n"
            "OP says she is not afraid. She says, if anything, she sleeps better now. Her daughter is fine. Her daughter is happy. "
            "Sometimes she swears she sees her daughter looking up at something above her crib and smiling at it.\n\n"
            "Subscribe if you've ever felt a loved one come back."
        ),
    },
    # 16
    {
        "title": "A Dating App Match Knew My Childhood Phone Number — I Had Never Told Anyone",
        "description": "We had never met. Her first message was the number my parents gave up in 1998. #letsnotmeet #creepy #scary #redditstories",
        "content": (
            "Matched with a woman on a dating app last month. Hadn't even exchanged names yet. Her first message was a ten digit "
            "phone number. No context. Just the number. I recognized it immediately. It was the home phone number my parents had "
            "when I was a kid. They gave it up in 1998 when we moved. I asked her what it was. She said, 'I'm sorry, I don't know "
            "why I sent that. My phone just typed it.' I unmatched. The next morning I had a missed call from that exact number. "
            "The number does not exist anymore. The voicemail was forty five seconds of a child humming the song I used to hum to "
            "myself when I was scared at night. I never told anyone I did that."
        ),
        "script": (
            "Some dating app stories are funny. Some are weird. This one is the only story I've ever read that made me delete the "
            "app off my phone.\n\n"
            "OP is in his mid thirties. Recently single. He's on one of the major dating apps. Last month he gets a new match. A "
            "woman. Nice photos. No bio. He doesn't message right away. He's been swiping casually.\n\n"
            "She messages first. The first message is a ten digit phone number. No context. No greeting. Just the number.\n\n"
            "OP reads it. His stomach drops. He recognizes the number immediately. It was his parents' home phone number when he "
            "was a kid. The number they had at the house he grew up in. They moved in 1998. They gave up the number. He hadn't "
            "thought of it in twenty five years. But he saw it and he knew it like it had been his own.\n\n"
            "He responds, what is this? Where did you get this?\n\n"
            "She replies, I'm so sorry, I don't know why I sent that. My phone just typed it. I think my keyboard glitched.\n\n"
            "He asks her if she's ever lived in his hometown. She says she's never been to that state.\n\n"
            "He asks her how old she is. She says twenty seven. She would have been an infant in 1998. There is no way she knows "
            "this number.\n\n"
            "He unmatches her. Closes the app. Tries to forget about it.\n\n"
            "The next morning he has a missed call. From the exact ten digit number she had sent him. A number that has not been "
            "his parents' number in twenty five years. A number that, when he Googles it, shows as disconnected. There is no active "
            "phone associated with that number.\n\n"
            "There is a voicemail. He plays it on speaker. It is forty five seconds long.\n\n"
            "It is a child. Humming. The same simple tune, over and over. No words. Just a child humming softly to themselves.\n\n"
            "It is the song he used to hum to himself when he was scared at night as a kid. He had made it up. He never sang it for "
            "anyone. He never told anyone he did it. It was a private comfort thing. He had completely forgotten about it until he "
            "heard the voicemail.\n\n"
            "He listened to it twice. He called his mom. He played it for her. She was silent for a long time. Then she said, "
            "honey, that's the song you used to hum when you couldn't sleep. I had completely forgotten until just now.\n\n"
            "OP deleted the app. He changed his number. The voicemail is still saved. He doesn't open it. Subscribe if you've ever "
            "had a private memory return uninvited."
        ),
    },
    # 17
    {
        "title": "Night Shift At An Empty Hotel — Someone Kept Checking Into Room 217",
        "description": "It happened every night at the same time. There was never anyone there. #nosleep #creepy #scary #redditstories",
        "content": (
            "Worked the night audit at a small hotel. 1 AM to 7 AM. Most nights I was the only person in the building. Around 3:33 "
            "AM, every single night, the front desk computer would log a check in. Room 217. Same name every time, John Smith. The "
            "system would print the registration card. No one was at the desk. The lobby was empty. The cameras showed nothing. The "
            "front door never opened. The card key for Room 217 would dispense by itself. I'd go upstairs to check the room. The "
            "door was always locked. The room was always empty. The bed was always slightly indented. As if someone had been "
            "sitting on it. Always on the same side. The side facing the window."
        ),
        "script": (
            "Hotels remember things. Some hotels remember people. OP worked at one that remembered the same guest, every single "
            "night.\n\n"
            "OP worked the night audit shift at a small forty room hotel for two years. One a.m. to seven a.m. Mostly alone. He'd "
            "run the end of day reports, prep breakfast, check in the occasional late arrival, and read between calls.\n\n"
            "About a month into the job, he started noticing something at three thirty three a.m.\n\n"
            "Every single night at three thirty three, his computer would log a new check in. Room 217. The guest name was always "
            "John Smith. The registration card would print at the front desk. The card key encoder would activate on its own, "
            "encode a key, and dispense it.\n\n"
            "The lobby was empty. The front door, which made a chime every time it opened, never chimed. The cameras showed an "
            "empty lobby. There was no John Smith.\n\n"
            "The first time it happened, he panicked. He called the manager. The manager said, oh, ignore that, it's a glitch in "
            "the system. Just void the reservation and throw the key away.\n\n"
            "He did. The next night, three thirty three, the check in happened again. He voided it again. Threw the key away "
            "again.\n\n"
            "Eventually curiosity got the better of him. He took the key one night and walked up to room 217. He used his master "
            "card to open the door. The room was clean, bed made, untouched. Everything in its place.\n\n"
            "Except the bed was slightly indented. On the side of the bed facing the window. Like someone had been sitting on the "
            "edge. The pillow had a faint impression where a hand had rested.\n\n"
            "He smoothed the bedspread. He left.\n\n"
            "The next night, three thirty three. The check in happened. He walked up. The bed was indented again. Same side. Same "
            "impression.\n\n"
            "He started checking it every night. Same impression. Same side of the bed. Sometimes the closet door was open. "
            "Sometimes the bathroom light was on. He had been turning everything off the night before. Every time.\n\n"
            "He asked the manager about the history of the room. The manager went quiet. Then he said, off the record, a man "
            "checked in there in the eighties and didn't come out. They found him sitting on the edge of the bed, facing the "
            "window, hands folded in his lap. Heart attack. Likely happened around three a.m. He'd been there for two days before "
            "anyone found him.\n\n"
            "OP says he quit the job a few months later. He couldn't stop dreaming about the indented bedspread. The hotel still "
            "logs a check in at three thirty three a.m. every night. The new audit person voids it. The system never gets fixed.\n\n"
            "Subscribe if you've ever worked the night shift somewhere old."
        ),
    },
    # 18
    {
        "title": "Every Night, A Child Waves At Me From The Edge Of The Woods",
        "description": "He never moves any closer. He never moves any further. He just waves. Until last week. #nosleep #scarystories #creepy #redditstories",
        "content": (
            "We live on five acres backing up to dense woods. About a year ago I started noticing a small child standing at the "
            "edge of the tree line at dusk. Waving at me. Same kid. Same hour. Every night. Maybe seven years old. He never came "
            "closer. He never went further into the woods. He just waved until it was dark, then I couldn't see him anymore. I "
            "called the sheriff twice. They walked the woods. Nothing. The forest service said no one lives in that direction for "
            "thirty miles. Last week, for the first time, he came closer. Twenty feet from my porch. Still waving. Still smiling. "
            "I went inside, locked the door, looked back out. He was gone. There were no footprints in the wet grass."
        ),
        "script": (
            "If a child waves at you from the woods, you wave back, right? OP did. For a year. Until the child came closer than he "
            "should have been able to.\n\n"
            "OP and his wife live on five acres of rural land. The back of the property opens up into dense, deep woods that go on "
            "for miles. There is no other house in that direction for a long, long way.\n\n"
            "About a year ago, OP started noticing a small child at the tree line at dusk. The child stood right at the edge of "
            "the woods. About a hundred and fifty yards from the back porch. He was waving. A small, slow, friendly wave. Like he "
            "knew OP.\n\n"
            "Same kid every night. About seven years old, OP estimates. Light hair. Plain clothes. Always at dusk. Always for "
            "about fifteen minutes. As soon as it got fully dark, OP could no longer see him, and the next morning the tree line "
            "was empty.\n\n"
            "OP waved back the first few times. He felt strange about it. He stopped waving back. The child kept waving anyway.\n\n"
            "He called the county sheriff's office. They came out, walked the tree line, looked for tracks, looked for a missing "
            "child report. Nothing. Nobody matched. They asked if maybe a neighbor had a kid that wandered. The nearest neighbor "
            "with kids is two miles away.\n\n"
            "He called the forest service. The forest service confirmed that the direction the woods went, behind his property, "
            "was uninhabited public land for thirty miles. There was no settlement, no cabin, no campground. No child was living "
            "in that direction.\n\n"
            "He set up a trail cam pointed at the tree line. The trail cam caught movement. It caught deer. It caught raccoons. "
            "It never caught the child. Even on nights when OP watched the child wave for ten minutes from his porch, the trail "
            "cam recorded nothing at that time.\n\n"
            "He started to accept it. He'd see the child wave. He'd ignore him. He'd go inside. Life would go on. His wife had "
            "started to see the child too, by month three. They stopped talking about it.\n\n"
            "Last week, something changed.\n\n"
            "OP was on the back porch at dusk. The child appeared at the tree line. Waved. Then, for the first time in a year, "
            "the child started walking forward. Calmly. Steadily. Across the yard. Toward the porch.\n\n"
            "OP froze. The child kept walking. Past the trail cam. Past the fence line. Across the lawn. He stopped about twenty "
            "feet from the porch. Looked up at OP. Still smiling. Still waving.\n\n"
            "OP went inside. He locked the back door. He looked back out the window.\n\n"
            "The yard was empty. The child was gone. The grass had been wet from rain that afternoon. There were no footprints "
            "in it.\n\n"
            "OP says they're listing the house. Subscribe if you've ever seen something at your tree line."
        ),
    },
    # 19
    {
        "title": "Someone Has Been Leaving Handwritten Notes On My Car For A Month — I Just Found Out Why",
        "description": "Each note had one sentence. I thought it was a prank. The last note had a name. #letsnotmeet #creepy #scary #redditstories",
        "content": (
            "About a month ago I started finding notes tucked under my windshield wiper. Handwritten. One sentence each. The first "
            "said, 'be careful tonight.' I laughed. That night I almost got hit by a drunk driver. The next week, 'don't take the "
            "highway home.' I took the highway. There was a six car pileup ten minutes after I got off. The notes kept coming. Each "
            "one warned me about something that happened that day. I tried to catch the person. I installed a dash cam. The dash cam "
            "showed nothing. The notes appeared anyway. Last week the note said, 'tell your mother I love her, and that I am sorry.' "
            "It was signed with my father's name. He died when I was four."
        ),
        "script": (
            "Have you ever wanted to thank a stranger and not known how? OP spent a month trying to figure out who was leaving him "
            "notes. He never expected the answer.\n\n"
            "About a month ago, OP came out of work and found a small folded piece of paper tucked under his windshield wiper. "
            "Handwritten. Neat older handwriting. One sentence. Quote, be careful tonight.\n\n"
            "He laughed. He thought it was a prank. He drove home anyway. On the way home, a drunk driver ran a red light and "
            "missed his car by inches. He sat at that intersection for two full minutes after the light turned green, just trying "
            "to breathe.\n\n"
            "The next morning, another note. Same handwriting. Quote, you forgot to lock the back door yesterday. He had. He had "
            "forgotten when he ran out the night before. Nothing had been disturbed. But he had forgotten.\n\n"
            "The notes kept coming. Roughly one every other day. Each one warned him about something that turned out to be true. "
            "Quote, don't take the highway home today. He took it anyway out of curiosity. There was a six car pileup ten minutes "
            "after he got off the highway. Quote, the cough is getting worse, please go in. His wife had been coughing for a week. "
            "She had pneumonia.\n\n"
            "He tried to catch whoever was leaving the notes. He worked in a parking garage with cameras. He went back through the "
            "footage. No one approached his car on the days the notes appeared. The footage just had him walking to his car and "
            "finding the note. The note was never placed by a visible person.\n\n"
            "He installed a small dash cam pointed at his windshield. The dash cam ran twenty four seven. The morning after he "
            "installed it, the next note appeared. The dash cam footage showed nothing. The wiper was empty for hours. And then "
            "the note was just there. The footage skipped half a second. The note appeared in the skip.\n\n"
            "He stopped trying to figure it out. He started using the warnings. He took different routes. He listened. He told his "
            "wife to go to the doctor.\n\n"
            "Last week, the final note. Same handwriting. Slightly shakier this time. The note said, quote, tell your mother I "
            "love her, and that I am sorry. It was signed. The signature was a name. His father's name.\n\n"
            "His father died when OP was four years old. He doesn't remember him. He never knew his handwriting. He drove to his "
            "mother's house that night, brought the note inside, and asked her if she recognized the writing.\n\n"
            "She started crying before he had finished the question. She got up. She came back with a shoebox of old letters. She "
            "opened one and laid it next to OP's note.\n\n"
            "Same handwriting.\n\n"
            "She said his father had been writing her letters from his army post the year before he died. She had kept all of "
            "them.\n\n"
            "There have been no notes since. OP says he's not afraid. He says he's grateful. Subscribe if you've ever felt watched "
            "over."
        ),
    },
    # 20
    {
        "title": "My Reflection Smiled When I Didn't",
        "description": "I caught it in the bathroom mirror. Then it started happening more. #nosleep #paranormal #creepy #scary #redditstories",
        "content": (
            "Brushing my teeth one morning, my reflection smiled at me. I wasn't smiling. I stopped, stared. It looked normal again. "
            "Mirror was just a mirror. I told my wife. She said I was tired. Next morning, same thing. I caught it doing things I "
            "wasn't doing. Tilting its head a half second after I did. Blinking when I didn't. Eventually one night I stood in front "
            "of the mirror and didn't move. My reflection slowly raised its right hand. Both my hands were at my sides. I covered "
            "every mirror in the house with sheets. I sleep on the couch now. The bathroom mirror, under the sheet, has been making "
            "a soft tapping sound at 3 AM. From the inside."
        ),
        "script": (
            "Have you ever caught your reflection doing something you weren't? OP did. And it kept getting worse.\n\n"
            "OP was brushing his teeth one morning. Half asleep. He looked up at the bathroom mirror. His reflection was smiling at "
            "him. A real, full smile. He was not smiling. He had a toothbrush in his mouth and a neutral face.\n\n"
            "He froze. He stared at his reflection. The reflection's face slowly returned to normal. He stood there for a long "
            "minute, blinking, moving his head side to side, watching the mirror. Mirror behaved normally. Mirror was just a "
            "mirror.\n\n"
            "He told his wife at breakfast. She said, you've been tired. He laughed it off. Walked it back. Said it was probably "
            "just a weird half second hallucination.\n\n"
            "The next morning, it happened again. Brushing his teeth. The reflection blinked. He had not blinked. He blinked back. "
            "The reflection blinked again, a beat behind him.\n\n"
            "Over the next week, the lag got worse. His reflection started doing things a half second after he did them. Tilting "
            "its head. Lifting its hand. Then, sometimes, doing things slightly differently. Tilting the wrong direction. Raising "
            "the wrong hand.\n\n"
            "He stopped looking at the bathroom mirror as much. He started using a small handheld one to shave. The handheld was "
            "fine. The bathroom mirror was not.\n\n"
            "One night, around eleven p.m., he stood in front of the bathroom mirror to test it. He stood completely still. Hands "
            "at his sides. Face neutral. He stared at his reflection. He didn't move at all.\n\n"
            "His reflection slowly raised its right hand. To about chest height. Like it was waving slowly.\n\n"
            "Both of OP's hands were still at his sides. He hadn't moved. He couldn't even feel a twitch in his arm.\n\n"
            "He walked out of the bathroom. He didn't sleep. The next morning he bought a stack of bed sheets at Target. He came "
            "home and covered every mirror in the house. Bathroom mirror. Hallway mirror. Vanity. Even the small mirror in his "
            "wife's purse that she had been worrying about.\n\n"
            "His wife thought he was losing it. She let him do it anyway.\n\n"
            "He has been sleeping on the couch since. He says it just feels safer not to be in a room with a mirror, even covered.\n\n"
            "Three nights ago, he started hearing a soft tapping sound at three a.m. He tracked it to the bathroom. He stood in "
            "the hallway. The tapping was coming from behind the sheet over the bathroom mirror. Slow. Patient. Like a fingernail.\n\n"
            "From the inside.\n\n"
            "OP says he's calling a guy his pastor recommended. He'll update us in a week. Subscribe so you don't miss it. And "
            "please cover your mirrors tonight."
        ),
    },
    # 21
    {
        "title": "The Locked Shed Behind My New Lake Cabin Had A Lock With No Keyhole",
        "description": "The realtor said to ignore it. I should have. #nosleep #creepy #scary #redditstories",
        "content": (
            "Bought a small lake cabin. Behind it, about twenty yards into the trees, was a wooden shed. The lock on the door was "
            "thick iron and had no keyhole. The realtor said the previous owner asked it never be opened. I asked why. He just "
            "said, 'the previous owner asked it never be opened.' Four months in I broke the lock. Inside was a small wooden chair "
            "facing the back wall. On the wall, in neat handwriting, were dates and names. About a hundred of them. The last name "
            "was mine. Dated next week. I called the realtor. He said the previous owner asked it never be opened. I asked who the "
            "previous owner was. He said, 'you are.'"
        ),
        "script": (
            "When a realtor tells you not to open something, you should ask why. OP did not.\n\n"
            "OP bought a small lake cabin in the upper Midwest last fall. Beautiful little place. Two bedrooms. A dock. About a "
            "hundred yards from the water.\n\n"
            "Behind the cabin, about twenty yards into the trees, there was a wooden shed. Old. About six by six. One door. The "
            "door was secured with a lock that, when OP first saw it, looked weird. Thick. Iron. Old. Heavier than any shed lock "
            "needs to be. He looked at it closely. There was no keyhole. The lock had no opening. Nothing to put a key in.\n\n"
            "He asked the realtor about it during the walkthrough. The realtor was a quiet man. He just said, quote, the previous "
            "owner asked it never be opened. OP asked why. The realtor repeated, quote, the previous owner asked it never be "
            "opened. He would not say anything else.\n\n"
            "OP let it go. He moved in. He used the cabin on weekends. He forgot about the shed.\n\n"
            "Four months later, in the middle of a peaceful Saturday, OP got curious. He walked into the trees with bolt cutters. "
            "He spent twenty minutes working through the iron lock. It finally gave way. He pushed open the door.\n\n"
            "Inside was a single small wooden chair. Facing the back wall. The rest of the shed was empty.\n\n"
            "On the back wall, in neat black handwriting, were dates. And names. Hundreds of them. He stepped closer. The list "
            "went back to the late 1800s. Most names he didn't recognize. Each one was paired with a date.\n\n"
            "The most recent names were within the last decade. He didn't recognize them either.\n\n"
            "At the very bottom of the list, a name. His own. Spelled correctly. Full middle name. Even his nickname his wife uses "
            "in private.\n\n"
            "Next to his name was a date. The next Saturday.\n\n"
            "He stared at it for a long time. He took photos. He walked out of the shed. He drove to town. He called the realtor. "
            "Asked who the previous owner of the cabin had been. The realtor said, the previous owner asked it never be opened. "
            "OP said, but who is the previous owner. Tell me their name.\n\n"
            "The realtor was quiet for a long beat. Then he said, calmly, you are.\n\n"
            "OP looked at his deed. His name. He looked at the title history the realtor sent over. Just his name. Going back to "
            "the original deed in 1894. His name. The same name. Over and over.\n\n"
            "OP did not stay at the cabin that weekend. He has not been back since. The date next to his name has passed. He is "
            "still here. He doesn't know what it means. He doesn't want to know.\n\n"
            "He says he's selling the cabin to whoever will take it. But it is going to be his cabin again. Eventually. It always "
            "is. Subscribe and please leave locked things locked."
        ),
    },
    # 22
    {
        "title": "There Were Footprints In Fresh Snow Starting At My Front Door Going Outward",
        "description": "Nothing came in. Something walked out. #nosleep #paranormal #winter #creepy #redditstories",
        "content": (
            "Woke up to fresh snow. About four inches overnight. I opened the front door to get the paper and stopped. There were "
            "footprints in the snow. Starting at my front door. Walking outward. Toward the road. A single set. Bare feet. Adult "
            "sized. They went all the way to the road and then stopped in the middle of the street. No footprints came back. None "
            "came in. The snow had been undisturbed when it started falling, the camera confirmed. The first prints appeared at "
            "3:14 AM, walking out, with no person making them in the footage. I live alone."
        ),
        "script": (
            "Have you ever woken up to fresh snow and seen footprints? OP did. He just couldn't figure out who came in.\n\n"
            "OP lives alone in a small Midwestern town. Quiet neighborhood. He woke up one Saturday morning in early February to a "
            "fresh snowfall. About four inches had fallen overnight. He made coffee. He opened the front door to grab the "
            "newspaper from the porch.\n\n"
            "He stopped before he could pick it up.\n\n"
            "There were footprints in the fresh snow. Starting at his front door. Walking outward, down the porch steps, across "
            "the yard, all the way to the road. A single set. Adult sized. Bare feet.\n\n"
            "The footprints continued into the middle of the street. They stopped exactly in the middle of his lane. They did not "
            "continue in any direction. There were no other prints around them. No prints coming back.\n\n"
            "Nothing had walked toward his house. Something had walked away from it.\n\n"
            "OP has a doorbell camera that records continuously. He pulled up the footage. He scrubbed through the night. The snow "
            "started falling around midnight. It fell steadily until about three a.m.\n\n"
            "At 3:14 a.m., the first footprint appeared on his porch.\n\n"
            "Just appeared. Pressed itself into the snow. No person was visible in the footage. No shape. No shadow. Just a print, "
            "forming in the snow.\n\n"
            "A second print appeared. Then a third. Then a fourth. The prints continued, in real time, walking down the steps, "
            "across the yard, to the road. The whole thing took about ninety seconds.\n\n"
            "When the prints reached the middle of the road, they stopped. There was no figure to be seen leaving. The prints just "
            "ended.\n\n"
            "OP watched the footage three times. There was no glitch. The camera had not skipped. The prints had been pressed into "
            "the snow by something that was not visible.\n\n"
            "He looked back through previous nights of footage. He found other anomalies. About once a week, on the same camera, "
            "around three a.m., the door would briefly appear to be ajar. He never opened it at three a.m. He never came out. He "
            "had not seen the footage before because he had no reason to look.\n\n"
            "He called a friend who works in IT. They tested the camera. Camera was fine. They tested the snow with a thermal "
            "imager that afternoon. Nothing unusual. The footprints had melted with the rest of the snow.\n\n"
            "OP says he's been bolting his front door at night since. The footprints have not come back. But sometimes he wakes up "
            "and finds the deadbolt unlocked. He always locks it. He always finds it unlocked.\n\n"
            "He says he doesn't know if something has been leaving every night. Or just the one time. He's afraid to find out.\n\n"
            "Subscribe and please check your snow this winter."
        ),
    },
    # 23
    {
        "title": "My Uber Driver Took A Wrong Turn — Into A Neighborhood That Wasn't On The Map",
        "description": "He apologized. He kept driving. I didn't recognize a single street. #letsnotmeet #nosleep #creepy #redditstories",
        "content": (
            "Took an Uber home from the airport. Late flight, midnight pickup. Driver was a polite older man. About fifteen "
            "minutes from home he made a turn that wasn't right. He apologized and said his GPS had recommended it. The streets "
            "looked off. Houses were old. Wrong style for my city. No streetlights. No other cars. I checked my phone. The GPS "
            "showed our blue dot in the middle of an empty gray area. No streets. No labels. The driver kept driving. He said, "
            "'we just have to drive until the map comes back.' We drove for an hour. We did not pass another car. Eventually the "
            "map flickered back on and we were two miles from my apartment. He didn't charge me. He said, quietly, 'don't take "
            "rides after midnight.'"
        ),
        "script": (
            "Have you ever taken an Uber and felt like the driver knew something you didn't? OP's driver was the kindest man he had "
            "ever met. And he was very afraid.\n\n"
            "OP landed late on a Wednesday night. His flight was delayed two hours. He stood at the curb at midnight and ordered an "
            "Uber. The car arrived in about ten minutes. The driver was an older man. Polite. Soft spoken. Asked OP how his trip "
            "had been. They made small talk for about ten minutes.\n\n"
            "About fifteen minutes from his apartment, the driver made a left turn at a light. OP looked up from his phone. The "
            "turn was not right. They were not on the route OP knew. He pulled up his own map. The blue route on the rider app "
            "had also moved. It was now showing a different path back to his apartment. Longer.\n\n"
            "The driver said, I am so sorry, the GPS just rerouted me, I think there must be construction on the highway. He kept "
            "driving.\n\n"
            "The streets they were driving on did not look right. The houses were old. Wrong architectural style for OP's city. "
            "The neighborhood looked like it belonged in a different state. There were no streetlights. There were no cars on the "
            "road. None parked. None passing. No one walking. Every house was dark.\n\n"
            "OP looked at his phone again. His map was acting strange. The blue dot, which marks his location, was in the middle "
            "of a gray empty area. No streets were rendered. No labels. As if the GPS knew he was somewhere but had no map of "
            "where that was.\n\n"
            "He asked the driver to pull over. The driver said, sir, I am so sorry, but I can't. Then he said, very calmly, we "
            "just have to drive until the map comes back. He said it like he had done this before.\n\n"
            "They drove for an hour. OP says it felt like an hour. He couldn't tell. The clock on his phone seemed to be stuck. "
            "His phone had two bars but no data. They never passed another car. They never passed a streetlight. The houses kept "
            "going. Same style. Endless.\n\n"
            "At some point, the driver's map flickered. The screen on the dash refreshed. The blue route reappeared. The driver "
            "exhaled. They were two miles from OP's apartment, on a road OP recognized, like they had never left.\n\n"
            "The driver dropped him off. He did not charge him. The app showed the ride as a normal completed trip, billed at the "
            "originally quoted fare. The driver leaned over before OP got out and said, quietly, don't take rides after midnight. "
            "Then he drove away.\n\n"
            "OP tried to find the driver's profile in the app to message him. The profile was gone. The trip was the only one in "
            "his history that had no driver name attached.\n\n"
            "He doesn't take late flights anymore. Subscribe if you've ever felt your map lie to you."
        ),
    },
    # 24
    {
        "title": "The Basement Light Keeps Turning Itself On — I Don't Have A Basement",
        "description": "I rent a third floor apartment. The switch on my kitchen wall labeled basement turns something on. Somewhere. #nosleep #creepy #scary #redditstories",
        "content": (
            "I rent a third floor walk up. Old building. In the kitchen there is an old switch plate near the back door labeled "
            "in faded handwriting, 'basement.' My apartment has no basement. The building has no basement, my landlord says. The "
            "switch should be dead. Six months in, I flipped it. Just to see. I heard a click far below me, through the floor. A "
            "faint hum, like a bulb warming up. I went down to the lobby. There is no door to anything I haven't seen. The hum "
            "kept going. I flipped the switch off. Click. Hum stopped. I have not flipped it again. Now it flips itself on. At 3 "
            "AM. Every night. I sleep with the kitchen door closed. The hum is getting louder."
        ),
        "script": (
            "When you move into an old apartment, you accept that some things will be weird. OP's switch labeled basement is the "
            "weirdest thing I have ever read about.\n\n"
            "OP rents a third floor walk up in an older brownstone style building. Hundred year old building. Three units. He's on "
            "the top floor.\n\n"
            "In his kitchen, next to the back door, there is an old switch plate. Two switches. One controls the porch light. The "
            "other has a small handwritten label on the plate, faded but legible. It says, quote, basement.\n\n"
            "OP's apartment has no basement. He's on the third floor. He doesn't have any reason to control a basement. He assumed "
            "the switch was just a leftover from when the building was wired differently.\n\n"
            "He asked the landlord during his move in. The landlord laughed and said, oh, that switch hasn't done anything in "
            "decades. The building doesn't have a basement. We have a crawl space but no one goes down there.\n\n"
            "OP figured it was dead. He didn't think about it. He lived there for six months.\n\n"
            "Then, one Saturday afternoon, just curious, he flipped it.\n\n"
            "He heard a click. Far below him. Through the floor. Faint but unmistakable. Like a switch in another part of the "
            "building had engaged. And then a soft hum started. The kind of hum an old incandescent bulb makes when it's warming "
            "up.\n\n"
            "He stood in his kitchen, listening. The hum kept going. He pressed his ear to the floor. He could hear it, definitely, "
            "below him. Below his neighbor below him. Below the lobby. Coming from somewhere underneath the building.\n\n"
            "He went downstairs to the lobby. He walked the whole first floor. There is no door to a basement. There is a small "
            "utility closet, locked, but the landlord had shown him inside. It is full of pipes. There is no light. There is no "
            "switch.\n\n"
            "The hum kept going while he was in the lobby. He could hear it.\n\n"
            "He went back upstairs and flipped the switch off.\n\n"
            "Click. The hum stopped.\n\n"
            "He has not flipped it again. He decided whatever it was, he didn't need to know.\n\n"
            "Two weeks later, at three a.m., he woke up to the click. From his kitchen. He got out of bed. Walked to the kitchen. "
            "The basement switch was up. He had not touched it. He flipped it down. Click. The hum stopped.\n\n"
            "It flips itself on every night now. Always at three a.m. He has tried taping it down. The tape comes loose. He has "
            "tried unscrewing the switch plate. The switch is still operational beneath. He cannot find where the wire goes.\n\n"
            "The hum is getting louder.\n\n"
            "He sleeps with the kitchen door closed. He's looking for a new apartment. Subscribe and please don't flip mystery "
            "switches."
        ),
    },
    # 25
    {
        "title": "Every Night For A Week, A Stranger Has Been Sitting At My Kitchen Table At Exactly 4 AM",
        "description": "I have video. He doesn't move. He just sits. And he smiles when I see him. #nosleep #paranormal #scarystories #creepy #redditstories",
        "content": (
            "Seven nights ago I woke up at 4 AM thirsty. Walked to the kitchen. A man was sitting at my kitchen table. Bald. Late "
            "fifties. Wearing a dark robe. He was watching me. He smiled when our eyes met. I froze. Ran back to the bedroom. "
            "Locked the door. Called 911. Police came. Apartment was empty. No signs of entry. I set up a camera the next night. "
            "He showed up at 3:59 AM, walked in through the front door which never opened, sat in the same chair, smiled at the "
            "camera for sixty one minutes, and left through the wall. He has done this every night since. Last night he raised "
            "his hand and waved."
        ),
        "script": (
            "If a stranger appeared at your kitchen table every night at four a.m., what would you do? OP set up a camera. The "
            "footage is keeping him from sleeping.\n\n"
            "Seven nights ago OP woke up thirsty. Around four a.m. He got out of bed, padded toward the kitchen for water. He "
            "rounded the corner into the kitchen and stopped.\n\n"
            "There was a man sitting at his kitchen table.\n\n"
            "Bald. Late fifties. Wearing a dark robe. The man's hands were folded in his lap. He was sitting straight up, not "
            "slouched. He was watching the doorway. He was watching for OP.\n\n"
            "When their eyes met, the man smiled. A small, polite smile. He didn't move. He didn't speak. He just smiled.\n\n"
            "OP backed up. He ran to the bedroom. He locked the door. He called 911.\n\n"
            "Police arrived in eight minutes. They cleared the apartment. There was no one inside. The front door was locked. The "
            "windows were latched. The fire escape window had not been opened in months by the look of the paint. There were no "
            "signs of entry. The officers were polite but unconvinced. They wrote it up as a possible vivid nightmare.\n\n"
            "OP wasn't convinced. He set up a camera on his bookshelf the next night, pointed at the kitchen table. Wide angle. "
            "Night vision. Continuous recording. He locked his bedroom door and went to bed.\n\n"
            "He watched the footage the next morning. At three fifty nine a.m., the front door appeared on the side of the frame. "
            "The door did not open. The deadbolt did not move. But a man walked into the kitchen from the direction of the door. "
            "Same man. Same robe. Same posture.\n\n"
            "He walked to the kitchen table. He sat down in the same chair as the night before. He folded his hands in his lap. "
            "He looked directly at the camera. He smiled at it.\n\n"
            "He sat there, completely still, for sixty one minutes. The timer ticked from three fifty nine to five a.m. He didn't "
            "blink in a way OP could see. He didn't move his hands. He just sat. And smiled.\n\n"
            "At exactly five a.m., he stood up. He walked toward the wall on the right side of the kitchen. Not toward the door. "
            "Toward the wall. He walked into the wall. He didn't stop. He didn't push against it. He walked through it like it "
            "wasn't there. He was gone.\n\n"
            "This has happened every night since. Same arrival time. Same chair. Same smile. He leaves at exactly five a.m. He "
            "always exits through the same wall. On the other side of that wall is the apartment next door. OP knocked. The "
            "elderly woman who lives there has lived in that apartment for forty years. She let him in. She has no extra rooms. "
            "Her walls match her floor plan exactly.\n\n"
            "Last night, for the first time, the man raised his hand. He waved at the camera. Slowly. Once. Then he sat for the "
            "rest of the sixty one minutes and left.\n\n"
            "OP is moving out tomorrow. He's leaving the camera. He says he wants to know if the man follows or stays.\n\n"
            "Subscribe so we can both find out together."
        ),
    },
]


def main() -> None:
    out_path = Path(__file__).parent / "yt_reddit_stories.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["No", "Video Title", "Video Description", "Content", "Modified Script"])
        for i, s in enumerate(stories, start=1):
            writer.writerow([i, s["title"], s["description"], s["content"], s["script"]])
    print(f"Wrote {len(stories)} rows to {out_path}")


if __name__ == "__main__":
    main()
