import time

# List of spam phrases
spam_phrases = ['free', 'you', 'winner', 'click here', 'claim', 'urgent', 'act now',
                'limited time', 'money', 'guaranteed', 'prize', 'risk-free', 'exclusive offer',
                'order now', 'credit card', 'cash', '100%', 'congratulations', 'as seen on',
                'no cost', 'trial', 'save big', 'investment', 'cheap', 'instant', 'bonus',
                'deal', 'subscribe', 'offer expires', 'apply now']


#create make_timer function
def make_timer():
    start_time = time.time()  # Record the start time

    def timer():
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        return elapsed_time

    return timer


# Function to scan email and detect spam phrases
def email_scan(message):
    # Convert message to lowercase and split into words
    words_in_message = message.lower().split()

    # Initialize detected phrases and variables
    detected_spam_words = []
    spam_count = 0

    # Begin scanning for spam phrases while incorporating sleep function
    for spam_word in spam_phrases:
        time.sleep(0.1)  # makes a small delay for each spam word check
        if spam_word in message.lower():
            spam_count += 1
            detected_spam_words.append(spam_word)

    # Determine message risk level
    msg_risk = 'No Spam Detected.'
    if spam_count == 0:
        msg_risk = 'No Spam Detected.'
    elif 1 <= spam_count <= 5:
        msg_risk = 'Low Risk For Spam.'
    elif 6 <= spam_count <= 10:
        msg_risk = 'Medium Risk For Spam.'
    else:
        msg_risk = 'High Risk For Spam.'

    # Print spam score, risk level, and detected words
    print(f'Risk Level: {msg_risk}')
    print(f'Spam Count: {spam_count}')
    if detected_spam_words:
        print(f'Spam Words/Phrases Detected: {", ".join(detected_spam_words)}')


# Main block to run the spam scanner
if __name__ == "__main__":
    timer = make_timer()  # Create the timer

    # Prompt user for email message
    email_message = input("Please enter the email message to scan: ")

    print("Scanning email for spam...")
    email_scan(email_message)  # Call the email scan function
    elapsed = timer()  # Get the elapsed time
    print(f"Total time taken for scanning: {elapsed:.2f} seconds")
