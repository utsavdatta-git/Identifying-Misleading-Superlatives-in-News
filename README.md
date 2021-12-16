# Identifying misleading superlatives in news

## What is wrong with the below news item?







# ***This is the luckiest house in the world, knowing the reason you will also believe***

'*Madrid: A house located among the mountains in Spain is being called the ‘lucky house’ in the world. The reason for this is that it remains safe even after the lava that came out after the eruption of the volcano. While the blazing lava took everything around, this small house remained safe. The people of Spain are considering it a miracle. At the same time, there is no place for the happiness of the owner of the house.*

*people had left everything
According to the report of ‘The Sun’, after the eruption of the volcano on the Atlantic island of La Palma, lava started pouring out of it. After this the administration evacuated people from La Palma and shifted them to a safe place. People left everything and went away to save their lives. No one expected that anything would be left of them, but a house stood as before even in the midst of this natural calamity.*

*More than 350 houses destroyed
The report said that the lava from the volcanic eruption destroyed more than 350 homes, but nothing happened to the house of the retired Danish couple. The mistress of the house said, ‘When we came to know, our tears came out due to happiness. We can’t believe that our home is safe. Let us tell you that most of the houses and schools in the area have been destroyed by the lava.*

*Lava slowed down
At the same time, officials said that the speed of lava has slowed down. Along with this, relief work has been intensified. However, he said that the threat is not completely over yet. He has appealed to the people to avoid going to the affected areas. On the other hand, the builder who built the house of the Danish couple is happy with his work. He hopes that his business will grow after this incident.*'

At first glance, it seems to be a completly harmless piece of news with an attractive headline except for the fact that it unncessarily uses a superlative without justifying its claim in the body that follows. Consider the words "this is luckiest house in the world", there is no justification, quatification or explanation for that claim anywhere in the 4 paragraphs that constitute the body of the news item. Clearly, the headline is an exaggerated one meant to serve as a clickbait!

On some further research across a few other news websites, I found few more such examples. For example, consider these:

*Prince Philip: the world’s luckiest man, yet he seethed with anger!*

*The 27 Best Ways to Train a Dog!*

This is just the tip of the iceberg when it comes to exaggerated and misleading headlines online. However, the specific problem of unnecessary/misleading use of superlatives in news headlines is even more rampant in the Hindi language (one the most widely spoken languages in india). Consider these examples:

*ये हैं दुनिया के सबसे खतरनाक द्वीप, जहां जाकर आप देंगे 'मौत को दावत'!*

*सर्दियों में होने वाली शादियों में इन पांच तरीकों को अपनाकर दिखेंगी सबसे 'स्टाइलिश'!*

*फेफड़े का कैंसर फैलने की सबसे बड़ी वजह बना वायु प्रदूषण!*

In all the above news headlines, the superlatives are neither justified through proper quantification nor they are supported or even mentioned again (proving they were just used to mislead), in their corresponding bodies.

Some justified use of superlatives in news headlines are given below:

***पीएम मोदी ने विश्‍व की सबसे लंबी सुरंग की राष्ट्र को समर्पित***

*प्रधानमंत्री नरेंद्र मोदी ने हिमाचल प्रदेश के रोहतांग में विश्‍व की सबसे लंबी अटल सुरंग का उद्घाटन किया। 9.02 किलोमीटर की इस टनल के शुरु होने से मनाली और लेह के बीच सड़क की दूरी 46 किलोमीटर कम हो जाएगी। समुद्र तल से 10 हजार फुट की ऊंचाई पर अत्याधुनिक तकनीक और इलेक्टो-मैक्निकल प्रणाली से इसका निर्माण किया गया है।*


***चंद्रग्रहण लगा, 580 साल में सबसे लंबी अवधि का ग्रहण***

*स्पेस डॉट कॉम के मुताबिक इस चंद्र ग्रहण की अवधि सबसे ज़्यादा ध्यान खींचने वाली है. चंद्र ग्रहण तीन घंटे, 28 मिनट और 24 सैकेंड तक रहेगा और यह 580 सालों में सबसे लंबा आंशिक ग्रहण बन जाएगा.*

As a result of this observation, I wanted to explore the possibility of Deep Learning models (especially Recurrent Neural Networks for Natural Language Processing use cases) to identify such misleading headlines and highlight them to the readers to enable them make an informed choice. The rest of the notebook describes the exploration of various techniques to solve this problem with a demo of the model being used on some real-life news articles at the end.
