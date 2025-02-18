def chatbot():
    print("Welcome to the College Assistant Chatbot! Type 'bye' to exit.")
    
    while True:
        # Accept user input and convert it to lowercase for easy comparison
        user_input = input("You: ").lower()  
        
        # Exit condition for the chatbot
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        # General greetings
        elif user_input in ["hi", "hello"]:
            print("Chatbot: Hello! How can I help you today?")
        # Response to "How are you?"
        elif user_input == "how are you?":
            print("Chatbot: I'm doing well, thank you for asking! How can I assist you today?")
        # Responses related to class and college schedule
        elif "what time is my next class?" in user_input:
            print("Chatbot: Your next class is at 10:00 AM in Room 205.")
        elif "when is the next holiday?" in user_input:
            print("Chatbot: The next holiday is on January 26th for Republic Day.")
        elif "what is the exam date?" in user_input:
            print("Chatbot: The exams start on February 10th.")
        elif "who is the dean?" in user_input:
            print("Chatbot: The current Dean is Dr. Smith.")
        elif "how can I contact the library?" in user_input:
            print("Chatbot: You can contact the library at library@srm.edu.")
        elif "where is the cafeteria?" in user_input:
            print("Chatbot: The cafeteria is on the 2nd floor near the main entrance.")
        elif "how many courses are available?" in user_input:
            print("Chatbot: There are 50+ courses available in the current semester.")
        elif "what is the grading system?" in user_input:
            print("Chatbot: The grading system is A, B, C, D, and F. A being the highest.")
        elif "when is the semester break?" in user_input:
            print("Chatbot: The semester break starts from December 15th and ends on January 5th.")
        elif "how do I register for courses?" in user_input:
            print("Chatbot: You can register for courses through the college portal or visit the registration desk.")
        elif "is there a student club for coding?" in user_input:
            print("Chatbot: Yes, we have a Coding Club that meets every Wednesday at 4 PM in Room 102.")
        # Catch-all response for any unknown queries
        else:
            print("Chatbot: Sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
chatbot()
