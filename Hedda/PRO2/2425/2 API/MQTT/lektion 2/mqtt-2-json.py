import paho.mqtt.client as mqtt
import time
import random
from datetime import date, datetime

import math

def on_connect(client, userdata, flags, reason_code, properties): # Called on connect
    print("Connected with result code "+str(reason_code))
    #send()

def send_1():
    # Send data to the broker
    topic = "cake"
    x = 0
    while True:
        time.sleep(random.randint(0,10))
        now = datetime.now()
        message = {"id": x,
                   "value": math.cos(now.microsecond)}
        client.publish(topic, str(message))
        x += 1

def send_2():
    topic = "cake"
    i = 0
    while True:
        time.sleep(0.1)
        message = data[i%len(data)]
        topic = "cake"
        client.publish(topic, message)
        i += 1
        
        
            
# Define the client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
#client.on_message = on_message

text = """The Allowable Rhyme
By H. P. Lovecraft


“Sed ubi plura nitent in carmine, non ego paucis
Offendar maculis.”
—Horace.

The poetical tendency of the present and of the preceding century has been divided in a manner singularly curious. One loud and conspicuous faction of bards, giving way to the corrupt influences of a decaying general culture, seems to have abandoned all the proprieties of versification and reason in its mad scramble after sensational novelty; whilst the other and quieter school, constituting a more logical evolution from the poesy of the Georgian period, demands an accuracy of rhyme and metre unknown even to the polished artists of the age of Pope.
     The rational contemporary disciple of the Nine, justly ignoring the dissonant shrieks of the radicals, is therefore confronted with a grave choice of technique. May he retain the liberties of imperfect or “allowable” rhyming which were enjoyed by his ancestors, or must he conform to the new ideals of perfection evolved during the past century? The writer of this article is frankly an archaist in verse. He has not scrupled to rhyme “toss’d” with “coast”, “come” with “Rome”, or “home” with “gloom” in his very latest published efforts, thereby proclaiming his maintenance of the old-fashioned poets as models; but sound modern criticism, proceeding from Mr. Rheinhart Kleiner and from other sources which must needs command respect, has impelled him here to rehearse the question for public benefit, and particularly to present his own side, attempting to justify his adherence to the style of two centuries ago.
     The earliest English attempts at rhyming probably included words whose agreement is so slight that it deserves the name of mere “assonance” rather than that of actual rhyme. Thus in the original ballad of “Chevy-Chase”, we encounter “King” and “within” supposedly rhymed, whilst in the similar “Battle of Otterbourne” we behold “long” rhymed with “down”, “ground” with “Agurstonne”, and “name” with “again”. In the ballad of “Sir Patrick Spense”, “morn” and “storm”, and “deep” and “feet” are rhymed. But the infelicities were obviously the result not of artistic negligence, but of plebeian ignorance, since the old ballads were undoubtedly the careless products of a peasant minstrelsy. In Chaucer, a poet of the Court, the allowable rhyme is but infrequently discovered, hence we may assume that the original ideal in English verse was the perfect rhyming sound.
     Spenser uses allowable rhymes, giving in one of his characteristic stanzas the three distinct sounds of “Lord”, “ador’d”, and “word”, all supposed to rhyme; but of his pronunciation we know little, and may justly guess that to the ears of his contemporaries the sounds were not conspicuously different. Ben Jonson’s employment of imperfect rhyming was much like Spenser’s; moderate, and partially to be excused on account of a chaotic pronunciation. The better poets of the Restoration were also sparing of allowable rhymes; Cowley, Waller, Marvell, and many others being quite regular in this respect.
     It was therefore upon a world unprepared that Samuel Butler burst forth with his immortal “Hudibras”, whose comical familiarity of diction is in grotesqueness surpassed only by its clever licentiousness of rhyming. Butler’s well-known double rhymes are of necessity forced and inexact, and in ordinary single rhymes he seems to have had no more regard for precision. “Vow’d” and “would”, “talisman” and “slain”, “restores” and “devours” are a few specimens selected at random.
     Close after Butler came John Oldham, a satirist whose force and brilliancy gained him universal praise, and whose enormous crudity both in rhyme and in metre was forgotten amidst the splendour of his attacks. Oldham was almost absolutely ungoverned by the demands of the ear, and perpetrated such atrocious rhymes as “heads” and “besides”, “devise” and “this”, “again” and “sin”, “tool” and “foul”, “end” and “design’d”, and even “prays” and “cause”.
     The glorious Dryden, refiner and purifier of English verse, did less for rhyme than he did for metre. Though nowhere attaining the extravagances of his friend Oldham, he lent the sanction of his great authority to rhymes which Dr. Johnson admits are “open to objection”. But one vast difference betwixt Dryden and his loose predecessors must be observed. Dryden had so far improved metrical cadence, that the final syllables of heroic couplets stood out in especial eminence, displaying and emphasising every possible similarity of sound; that is, lending to sounds in the first place approximately similar, the added similarity caused by the new prominence of their perfectly corresponding positions in their respective lines.
     It were needless to dwell upon the rhetorical polish of the age immediately succeeding Dryden’s. So far as English versification is concerned, Pope was the world, and all the world was Pope. Dryden had founded a new school of verse, but the development and ultimate perfection of this art remained for the sickly lad who before the age of twelve begged to be taken to Will’s Coffee-House, that he might obtain one personal view of the aged Dryden, his idol and model. Delicately attuned to the subtlest harmonies of poetical construction, Alexander Pope brought English prosody to its zenith, and still stands alone on the heights. Yet he, exquisite master of verse that he was, frowned not upon imperfect rhymes, provided they were set in faultless metre. Though most of his allowable rhymes are merely variations in the breadth and nature of vowel sounds, he in one instance departs far enough from rigid perfection to rhyme the words “vice” and “destroys”. Yet who can take offence? The unvarying ebb and flow of the refined metrical impulse conceals and condones all else.
     Every argument by which English blank verse or Spanish assonant verse is sustained, may with greater force be applied to the allowable rhyme. Metre is the real essential of poetical technique, and when two sounds of substantial resemblance are so placed that one follows the other in a certain measured relation, the normal ear cannot without cavilling find fault with a slight want of identity in the respective dominant vowels. The rhyming of a long vowel with a short one is common in all the Georgian poets, and when well recited cannot but be overlooked amidst the general flow of the verse; as, for instance, the following from Pope:
"""

data = text.split()

client.connect("broker.emqx.io", 1883)
#client.loop_forever()
send_1()
#print(len(data))
#send_2()
