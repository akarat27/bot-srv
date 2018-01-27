#Python libraries that we need to import for our bot
import random
from flask import Blueprint, request
from pymessenger.bot import Bot
from pythainlp.tokenize import word_tokenize
from pythainlp.tokenize import isthai

#app = Flask(__name__)
apibot = Blueprint('apibot', __name__ , template_folder='templates')

ACCESS_TOKEN = 'EAAa4H2ZBzw9oBAMBuXnrVv6ZAGbAXbzwYHbxUe7UvlFzbOrSzfZC2h8mH81qZCIi2gb2OXEhXlrmeLy0qlZC2ij5797xwZAZAbbqTcU7RJzBs22oVeeuf0o7KTHewafKWOiPTHVC17XVs4CdwowIm6gZC4G6qH0bZADkLumTunimyIwZDZD'
VERIFY_TOKEN = 'noxma434'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint
@apibot.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          print(event)
          messaging = event['messaging'] #messaging
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    msg_input = message['message'].get('text')
                    dict_count_thai = isthai(msg_input)
                    response_sent_text = get_message()
                    if dict_count_thai['thai'] > 0:
                        list_tokenized = word_tokenize(msg_input,engine='newmm')
                        response_sent_text = ' '.join(list_tokenized)
                    send_message(recipient_id, response_sent_text)
                    #send_message("1834191463278166", response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)" ,"ส่งมาอีก" ,"ลองอีกครั้ง" ,"ไม่ใช่ล่ะ ลองใหม่" ,"โอเคเลยค่ะ ใช่แล้ว"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"
