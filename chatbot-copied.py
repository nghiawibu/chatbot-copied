import nltk 
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["I am a bot created by Analytics Vidhya. you can call me crazy!",]
    ],
    [
        r"how are you?",
        ["I'm doing goodnHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)",]
    ],
    [
        r"(.*) about (.*) organization",
        ["Our organization supports NGOs end wildlife trafficking.",]
    ],
    [
        r"(.*) wild animals",
        ["not tamed animals.",]
    ],
    [
        r"What is wildlife conservation?",
        ["Wildlife conservation is the practice of protecting wild species and their habitats in order to prevent species from going extinct. Major threats to wildlife include habitat destruction/degradation/fragmentation, over exploitation, poaching, pollution and climate change." ]
    ],
    [
        r"what (.*) endangered species in Vietnam?",
        ["Banded eagle rays, black-crested gibbons, Delacour's langur, great hammerhead","Indochinese tiger, siamese crocodile, Tam Dao salamander"]
    ],
    [
        r"(.*) can I donate?",
        ["you can donate by clicking ",]
    ],
    [
        r"what can I (.*) on the website?|how to use the website?|(.*) instructions?",
        ["log in and click the ... button to support NGOs",]
    ],
    [
        r"What is wildlife?",
        ["Wildlife means the native animals and vegetations of a region. Wildlife includes any animal, insect, aquatic, or land vegetation that forms a part of any habitat. This includes all varieties of flora and fauna, what is popularly known as biological diversity.",]
    ],   
    [
        r"How can I know if an organization is available?",
        ["it is shown on the NGO's description",]
    ],   
    [
        r"How (.*) find a (.*) that is suitable for me?",
        ["read the descriptions for each organization", ""]
    ],   
    [
        r"what (.*) features of the website?",
        ["You can find organizations to support, report criminal activities related to wildlife poaching, etc","You can help "]
    ],   
    [
        r"How long (.*) in existence?|How long (.*) existed?",
        ["We’re a newly established platform since 15th of November, 2021",]
    ],   
    [
        r"(.*) can see (.*) contributions?|Can (.*) see (.*) reports?",
        ["Only members allowed by the project managers can see the reports and contributions. You can only see your own contributions"]
    ],     
]

def chat():
    print("Hi! I am a chatbot")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
chat()
