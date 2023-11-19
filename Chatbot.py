import random

answers = {
    "Machine learning": "Machine learning is a field of artificial intelligence that focuses on developing algorithms allowing computers to learn and improve performance on tasks without being explicitly programmed.",
    "Supervised learning": "Supervised learning involves training a model on a labeled dataset, where inputs are paired with corresponding correct outputs, aiming to make predictions on new, unseen data.",
    "Unsupervised learning": "Unsupervised learning involves training a model on an unlabeled dataset, allowing it to discover patterns, relationships, or groupings within the data without explicit instructions.",
    "Deep learning": "Deep learning is a subset of machine learning using deep neural networks with multiple layers to automatically learn and represent complex patterns in data.",
    "Neural Network": "A neural network is a computational model inspired by the human brain, composed of interconnected nodes organized into layers, used for tasks like pattern recognition and decision-making.",
    "Natural Language Processing" : "NLP is a field of AI focused on enabling computers to understand, interpret, and generate human language, facilitating communication between humans and machines.",
    "Computer Vision": "Computer Vision involves the development of algorithms that enable machines to interpret and make decisions based on visual data, such as images or videos.",
    "Reinforcement Learning" : "Reinforcement Learning is a type of machine learning where an agent learns to make decisions by interacting with an environment. It receives feedback in the form of rewards or penalties to improve its decision-making over time."
}

possible_words_ML = ["what is machine learning", "machine learning", "mchone learning", "learning machine", 'machine learn', "robot learn", "do robots learn", "do machines learn", "machin learning", "machine leanring", "machine leanrning", "maching learning", "machien learning", "machine learing", "macine learning", "machinr learning", "machune learning", "machine lerning"]
possible_words_SL = ["what's supervised learning?", "can you explain how supervised learning works?", "tell me about supervised learning", "i'm new to this, what's the deal with supervised learning?", "explain supervised learning in simple terms", "how does supervised learning differ from other types?", "give me the basics of supervised learning", "break down supervised learning for me", "what happens in supervised learning?", "i've heard about it, but what exactly is supervised learning?", "suprevised learning", "surpevised learning", "can i supervise a robot?", "supervised learnings", "supervised leanring", "supervised leanrning", "superivsed learning", "supervsied learning", "supervisied learning", "supervised learing", "supervized learning", "supervsied leanring", "supervisied leanrning", "supervised lenring", "supervised learning"]
possible_words_UL = ["what's unsupervised learning?", "can you explain how unsupervised learning works?", "tell me about unsupervised learning", "i'm new to this, what's the deal with unsupervised learning?", "explain unsupervised learning in simple terms", "how does unsupervised learning differ from other types?", "give me the basics of unsupervised learning", "break down unsupervised learning for me", "what happens in unsupervised learning?", "i've heard about it, but what exactly is unsupervised learning?", "unsuprevised learning",  "unsuperivsed learning", "can I unsupervise a robot?", "unsupervised learnings", "unsupervised leanring", "unsupervised leanrning", "unsuperivsed learning", "unsupervsied learning", "unsupervisied learning", "unsupervised learing", "unsupervized learning", "unsupervsied leanring", "unsupervisied leanrning", "unsupervised lenring", "unsupervised learning"]
possible_words_DL = ["what's deep learning?", "can you explain how deep learning works?", "tell me about deep learning", "i'm new to this, what's the deal with deep learning?", "explain deep learning in simple terms", "how does deep learning differ from other types?", "give me the basics of deep learning", "break down deep learning for me", "what happens in deep learning?", "i've heard about it, but what exactly is deep learning?", "deep learnings", "deep leanring", "deep leanrning", "depp learning", "deep lerning", "deep learing", "deap learning", "deep lenring", "deep learning"]
possible_words_NN = ["neural network", "what is a neural network", "how does a neural network work", "explain neural network", "neural network basics", "neural network definition", "neural network", "neural netwrok", "neural netowrk", "neural nwtwork", "neural ntework"]
possible_words_NLP = ["nlp", "natural language proccesisng", "what is natural language processing", "explain nlp in simple terms", "how does nlp work", "give me examples of nlp applications", "tell me about language processing in ai", "what are the uses of natural language processing", "nlp applications in real life", "natural langauge processing", "nlp explanantion", "nlp appplications", "explain nlp in simple term", "what are the uses of natural langauge processing"]
possbile_words_CV = ["computer vision", "what is computer vision", "explain how computer vision algorithms work",  "give examples of computer vision applications", "how do machines recognize objects in images", "tell me about image recognition in ai", "computer vision in everyday life", "applications of visual recognition", "computer visionn", "computer vision algoritms", "computer vision applicatins", "how do machines recognize objects in imagess"]
possible_words_RL=["reinforcement learning", "what is reinforcement learning", "explain how reinforcement learning algorithms work", "give examples of reinforcement learning in real-world scenarios", "how do agents learn through reinforcement", "tell me about reinforcement learning applications", "reinforcement learning in games", "examples of reward-based learning", "reinforcment learning", "explain reinforcement learing algorithms", "reinforcement learning scenarious", "how do agents learn through reinforcemnt"]
possible_bot_responses = ["Anything else? if not just press 0 or exit to leave ", "Don't forget i know some other things also, but if you want to stop just press 0 or type exit ", "I hope my definitions are of use to you, you can the other topics i know also or if you want to leave just press 0 or type exit ", "If you have more questions, feel free to ask! Otherwise, you can type 0 or 'exit' to leave ", "I'm here to assist you with any other inquiries. Press 0 or type 'exit' whenever you're ready to leave ", "Need information on another AI-related topic? Just ask! To end, simply type 0 or 'exit' "]

exit = 0

print("Hello, my name is Claudiu. I'm a chatbot designed to answer all your AI-related questions.")

def check_answer(q):
    q = q.lower()
    if q in possible_words_NN:
        print(answers["Neural Network"])
    elif q in possible_words_ML:
        print(answers["Machine learning"])
    elif q in possible_words_SL:
        print(answers["Supervised learning"])
    elif q in possible_words_UL:
        print(answers["Unsupervised learning"])
    elif q in possible_words_DL:
        print(answers["Deep learning"])
    elif q in possible_words_NLP:
        print(answers["Natural Language Processing"])
    elif q in possbile_words_CV:
        print(answers["Computer Vision"])
    elif q in possible_words_RL:
        print(answers["Reinforcement Learning"])   
    else:
        print("I don't know that, please check your typing or try asking me something else. These are the topics I know:")
        for i, key in enumerate(answers.keys(), 1):
            print(f"{i} - {key}")

def main():
    player_answer = input("Please feel free to ask me anything regarding AI. If you want to leave, just say 'exit' or press 0: ")
    while exit == 0:
        try:
            if player_answer.lower() == "exit" or player_answer == "0":
                print("I hope I was of use today!")
                break
            check_answer(player_answer)
            player_answer = input(random.choice(possible_bot_responses))
        except Exception as e:
            print("Something went wrong. Please restart program again.")
            break

if __name__ ==  "__main__":
    main()
