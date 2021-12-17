# Identifying misleading superlatives in news

## What is wrong with the below news item?


![image](https://user-images.githubusercontent.com/54985804/146585456-8c09be2c-e508-4157-ad3f-1b86df08da05.png)




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



# Some real-world examples

The model outputs probability of a headline being misleading (due to misuse of superlatives) given each of the paragraphs constituting its body. A probability of less than 0.5 means the superlatives used in the headlines is NOT misleading and at least one paragraph justifies the superlative, as a result the headline-paragraph pair gets marked green. For anything higher than that, it gets marked red. Here are some predictions on real-worls news articles:

Example article 1


![image](https://user-images.githubusercontent.com/54985804/146522148-b53cf495-9552-4b4f-a872-527328828c36.png)

Example article 2


![image](https://user-images.githubusercontent.com/54985804/146522769-f0c7cffd-e4c5-4e11-a53a-ee61470f9e28.png)

Example article 3


![image](https://user-images.githubusercontent.com/54985804/146522960-6243b02b-a99e-49f9-8ff4-ee0e12ce254b.png)


