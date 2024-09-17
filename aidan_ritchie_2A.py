#Research online some of the most common spam email messages
#and words. Create a list of 30 words and phrases commonly found
#in spam messages. Write an application in which the user enters an
# email message. Then your application will scan the message for each of
# the 30 keywords or phrases. For each occurrence of one of these within the
# message, add a point to the message's "spam score". Next, rate the likelihood
# that the message is spam, based on the number of points received.
# Display the user's spam score, the likelihood message that it is spam,
# and the words/phrases which caused it to be spam.

#create a list of 30 spam phrases


spam_phrases = ['free', 'you', 'winner', 'click here', 'claim', 'urgent', 'act now',
                'limited time', 'money', 'guaranteed', 'prize', 'risk-free', 'exclusive offer',
                'order now', 'credit card', 'cash', '100%', 'congratulations', 'as seen on',
                'no cost', 'trial', 'save big', 'investment', 'cheap', 'instant', 'bonus',
                'deal', 'subscribe', 'offer expires', 'apply now']

#create a function that will scan email and detect spam phrases

def email_scan(message):

#convert message to lowercase letters to accommodate for lowercase phrases
#use split to separate into individual words/phrases

    words_in_message = message.lower().split()

#store listed phrases and initialize variables

    detected_spam_words = []

    spam_count = 0

#begin to scan words in the email message and account for detected words

    for spam_word in spam_phrases:
         if spam_word in message.lower():
            spam_count += 1
            detected_spam_words.append(spam_word)

#initalize message risks using if and elif statements based on how many phrases are detected

    msg_risk = 'No Spam Detected.'

    if spam_count == 0:
        msg_risk = 'No Spam Detected.'
    elif 1 <= spam_count <= 5:
        msg_risk = 'Low Risk For Spam.'
    elif 6 <= spam_count <= 10:
        msg_risk = 'Medium Risk For Spam.'
    else:
        msg_risk = 'High Risk For Spam.'

#print spam score, risk level and the words detected using join function

    print(f'Risk Level: {msg_risk}')
    print(f'Spam Count: {spam_count}')
    if detected_spam_words:
     print(f'Spam Words/Phrases Detected: {', '.join(detected_spam_words)}')

#create brief code to ask user input before passing it through and calling the function

#email_message = input('Please enter an email message:')
#email_scan(email_message)

import time

def wrapper(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time Elapsed was', t2 - t1)
        return ret_val
    return wrapper

count_nums =  

email_message = input('Please enter an email message:')
email_scan(email_message)